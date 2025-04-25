import { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeHighlight from 'rehype-highlight';

export default function Home() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setResponse('');
    setLoading(true);

    try {
      const res = await fetch('https://literate-space-pancake-97wxjg9v5xxv37w66-8000.app.github.dev/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });

      if (!res.ok) throw new Error(`Server responded with status ${res.status}`);
      const data = await res.json();
      setResponse(data.answer);
    } catch (err: any) {
      console.error('Fetch error:', err);
      setError('❗ Failed to get answer. Please make sure the backend is running and reachable.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-white p-6 font-sans">
      <div className="max-w-3xl mx-auto bg-white shadow-lg rounded-xl p-8 space-y-6">
        <h1 className="text-4xl font-bold text-center text-indigo-700">GenQAChat</h1>
        <p className="text-center text-sm text-gray-500 italic">
          🧠 AI-powered QA Knowledge Assistant • LangChain • FastAPI • HuggingFace • FAISS VectorStore (Semantic Search)
        </p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="text"
            className="w-full border border-gray-300 rounded px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
            placeholder="Ask your QA question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            required
          />
          <button
            type="submit"
            className="bg-indigo-600 text-white font-semibold px-6 py-2 rounded hover:bg-indigo-700 transition"
            disabled={loading}
          >
            {loading ? '🔄 Asking...' : 'Ask'}
          </button>
        </form>

        {loading && (
          <div className="text-center text-gray-500 italic">⏳ Generating answer...</div>
        )}

        {response && (
          <div className="prose max-w-none bg-green-50 p-4 rounded">
            <strong className="text-green-700">Answer:</strong>
            <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeHighlight]}>
              {response}
            </ReactMarkdown>
          </div>
        )}

        {error && (
          <div className="bg-red-50 border border-red-200 rounded p-4 text-red-700">
            <strong>Error:</strong> {error}
          </div>
        )}
      </div>

      <footer className="mt-10 text-center text-xs text-gray-500">
        Open-source AI Project by Sankarraj • GenQAChat © 2025
      </footer>
    </div>
  );
}
