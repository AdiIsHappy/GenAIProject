// components/QueryResult.tsx

import React from "react";

interface QueryResultProps {
  response: string;
}

const QueryResult: React.FC<QueryResultProps> = ({ response }) => {
  let prettyResponse;
  try {
    const jsonResponse = JSON.parse(response);
    prettyResponse = JSON.stringify(jsonResponse, null, 2);
  } catch (e) {
    prettyResponse = "Invalid JSON response.";
  }

  return (
    <div className="bg-gray-100 rounded-md shadow-md h-full flex flex-col">
      <h3 className="text-xl font-semibold text-black mb-2">
        Current Breakdown of the tasks are as follow
      </h3>
      <pre className="p-4 flex-1 mt-2 text-black text-sm border-2 border-black rounded-sm shadow-md whitespace-pre-wrap">
        {prettyResponse || "Your response will appear here."}
      </pre>
    </div>
  );
};

export default QueryResult;
