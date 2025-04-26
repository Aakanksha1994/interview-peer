from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class InterviewRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

class InterviewResponse(BaseModel):
    message: str
    conversation_id: str
    is_feedback: bool
    score: Optional[int] = None
    suggestions: Optional[List[str]] = None

# Store conversations in memory (in production, use a database)
conversations: Dict[str, List[Dict[str, str]]] = {}

# Initialize OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_case_study():
    prompt = """
    Generate a realistic Product Management case study interview question.
    The case should be about a real-world product challenge that a PM might face.
    Include:
    1. A clear problem statement
    2. Relevant context about the company and product
    3. Specific metrics or data points
    4. A clear question for the candidate to answer
    
    Format the response as a conversation starter.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Product Management expert creating interview case studies."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def get_interview_response(conversation_history: List[Dict[str, str]], user_message: str):
    messages = [
        {"role": "system", "content": """You are a Product Management interviewer conducting a case study interview.
        Your role is to:
        1. Ask probing questions about the candidate's answer
        2. Challenge assumptions when necessary
        3. Guide the conversation to cover key PM skills
        4. Provide feedback at appropriate moments
        5. Keep the conversation natural and engaging"""}
    ]
    messages.extend(conversation_history)
    messages.append({"role": "user", "content": user_message})
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content

@app.post("/interview", response_model=InterviewResponse)
async def conduct_interview(request: InterviewRequest):
    try:
        if not request.conversation_id:
            # Start new conversation
            conversation_id = os.urandom(16).hex()
            case_study = generate_case_study()
            conversations[conversation_id] = [
                {"role": "assistant", "content": case_study}
            ]
            return InterviewResponse(
                message=case_study,
                conversation_id=conversation_id,
                is_feedback=False
            )
        else:
            # Continue existing conversation
            conversation_id = request.conversation_id
            if conversation_id not in conversations:
                raise HTTPException(status_code=404, detail="Conversation not found")
            
            # Add user message to conversation
            conversations[conversation_id].append(
                {"role": "user", "content": request.message}
            )
            
            # Get AI response
            ai_response = get_interview_response(
                conversations[conversation_id],
                request.message
            )
            
            # Add AI response to conversation
            conversations[conversation_id].append(
                {"role": "assistant", "content": ai_response}
            )
            
            # Check if it's time for feedback
            is_feedback = len(conversations[conversation_id]) >= 6  # Provide feedback after 3 exchanges
            
            if is_feedback:
                feedback_prompt = f"""
                Based on the following conversation, provide:
                1. Specific feedback on the candidate's performance
                2. A score from 1-10
                3. 3 specific suggestions for improvement
                
                Conversation:
                {conversations[conversation_id]}
                """
                
                feedback_response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a Product Management expert providing interview feedback."},
                        {"role": "user", "content": feedback_prompt}
                    ]
                )
                
                feedback_text = feedback_response.choices[0].message.content
                score = 7  # Default score, parse from feedback in production
                suggestions = ["Improve your structure", "Add more metrics", "Be more specific"]  # Parse from feedback in production
                
                return InterviewResponse(
                    message=feedback_text,
                    conversation_id=conversation_id,
                    is_feedback=True,
                    score=score,
                    suggestions=suggestions
                )
            
            return InterviewResponse(
                message=ai_response,
                conversation_id=conversation_id,
                is_feedback=False
            )
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 