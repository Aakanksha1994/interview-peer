# PM Mock Interview AI

An AI-powered platform for practicing Product Management case study interviews with real-time feedback.

![PM Mock Interview Demo](./Peer%20mock.jpeg)

## 🚀 Features

- **Interactive PM Case Studies**: Realistic product management interview scenarios
- **Real-time Feedback**: Get immediate analysis of your responses
- **Performance Scoring**: Receive a numerical score to track your improvement
- **Improvement Suggestions**: Actionable tips to enhance your PM interview skills
- **Modern UI**: Clean, responsive interface that works on all devices

## 🛠️ Tech Stack

- **Frontend**: Next.js, React, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python
- **AI**: OpenAI GPT-4o models

## 🚦 Getting Started

### Prerequisites

- Node.js (v18+)
- Python (v3.8+)
- OpenAI API key

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. Start the backend server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

## 📝 Usage Guide

1. When you first open the application, you'll be presented with a case study scenario
2. Type your response to the prompt in the chat interface
3. The AI interviewer will ask follow-up questions to test your thinking
4. After 2-3 exchanges, you'll receive detailed feedback on your performance
5. Use the feedback to improve and try another case study

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [OpenAI](https://openai.com/) for providing the AI models
- [NextJS](https://nextjs.org/) for the frontend framework
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [Tailwind CSS](https://tailwindcss.com/) for styling

## 📧 Contact

Project Link: [https://github.com/yourusername/pm-mock-interview](https://github.com/yourusername/pm-mock-interview)

---

Made with ❤️ by [Your Name] 