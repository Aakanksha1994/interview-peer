'use client';

interface FeedbackDisplayProps {
  feedback: {
    message: string;
    score: number;
    suggestions: string[];
  };
}

export default function FeedbackDisplay({ feedback }: FeedbackDisplayProps) {
  return (
    <div className="mt-8 space-y-6">
      <div className="bg-gray-50 p-4 rounded-lg">
        <h3 className="text-lg font-medium text-gray-900 mb-2">Feedback</h3>
        <p className="text-gray-700 whitespace-pre-line">{feedback.message}</p>
      </div>

      <div className="bg-gray-50 p-4 rounded-lg">
        <h3 className="text-lg font-medium text-gray-900 mb-2">Score</h3>
        <div className="flex items-center">
          <div className="text-3xl font-bold text-indigo-600">{feedback.score}</div>
          <div className="ml-2 text-gray-500">/ 10</div>
        </div>
      </div>

      <div className="bg-gray-50 p-4 rounded-lg">
        <h3 className="text-lg font-medium text-gray-900 mb-2">Suggestions for Improvement</h3>
        <ul className="list-disc list-inside space-y-2 text-gray-700">
          {feedback.suggestions.map((suggestion, index) => (
            <li key={index}>{suggestion}</li>
          ))}
        </ul>
      </div>
    </div>
  );
} 