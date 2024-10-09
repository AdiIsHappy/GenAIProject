// components/QueryForm.tsx

import { useState } from "react";
import axios from "axios";

interface QueryFormProps {
  setResponse: (response: string) => void;
}

const QueryForm: React.FC<QueryFormProps> = ({ setResponse }) => {
  const [query, setQuery] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await axios.post("/api/process_query", {
        query,
      });
      setResponse(res.data.final_response);
    } catch (error) {
      console.error("Error submitting query:", error);
      setResponse("There was an error processing your request.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <label
        htmlFor="query"
        className="block text-lg font-medium text-gray-700"
      >
        Enter a complex query:
      </label>
      <textarea
        id="query"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Type your query here..."
        required
        className="w-full p-4 text-lg border rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
        rows={5}
      ></textarea>
      <button
        type="submit"
        className="px-4 py-2 font-semibold text-white bg-indigo-600 rounded-md shadow hover:bg-indigo-700"
        disabled={loading}
      >
        {loading ? "Processing..." : "Submit"}
      </button>
    </form>
  );
};

export default QueryForm;
