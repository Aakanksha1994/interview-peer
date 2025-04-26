'use client';

import { useState } from 'react';
import ChatInterface from './components/ChatInterface';
import FeedbackDisplay from './components/FeedbackDisplay';

export default function Home() {
  const [conversationId, setConversationId] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState<Array<{role: 'user' | 'assistant', content: string}>>([]);

  const handleSubmit = async (message: string) => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/interview', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message,
          conversation_id: conversationId,
        }),
      });
      const result = await response.json();
      
      if (!conversationId) {
        setConversationId(result.conversation_id);
        // Set the initial message from the assistant
        setMessages([{ role: 'assistant', content: result.message }]);
      } else {
        // Add the assistant's response to messages
        setMessages(prev => [...prev, { role: 'assistant', content: result.message }]);
      }
      
      if (result.is_feedback) {
        setFeedback(result);
      }
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  const addUserMessage = (message: string) => {
    setMessages(prev => [...prev, { role: 'user', content: message }]);
  };

  return (
    <main className="min-h-screen p-8 bg-gray-50">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8 text-gray-800">
          PM Mock Interview
        </h1>
        <div className="bg-white rounded-lg shadow-lg p-6">
          <ChatInterface 
            onSubmit={handleSubmit} 
            loading={loading} 
            messages={messages}
            addUserMessage={addUserMessage}
          />
          {feedback && <FeedbackDisplay feedback={feedback} />}
        </div>
      </div>
    </main>
  );
} 