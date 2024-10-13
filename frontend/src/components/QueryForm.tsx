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
    <form
      onSubmit={handleSubmit}
      className="space-y-4 mr-8 flex flex-col h-full"
    >
      <label
        htmlFor="query"
        className="block text-lg font-medium text-gray-700"
      >
        Enter Your Query Here:
      </label>
      <textarea
        id="query"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Type your query here..."
        required
        className="flex-1 w-full p-4 text-lg border-2 border-black rounded-sm shadow-md focus:ring-indigo-500 focus:border-indigo-500"
        rows={5}
      ></textarea>
      <button
        type="submit"
        className="px-6 py-2 font-bold  text-black bg-white rounded-sm border-2 border-black shadow hover:bg-gray-300"
        disabled={loading}
      >
        {loading ? "Processing..." : "Submit"}
      </button>
    </form>
  );
};

export default QueryForm;
