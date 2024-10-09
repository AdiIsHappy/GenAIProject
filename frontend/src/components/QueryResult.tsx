// components/QueryResult.tsx

interface QueryResultProps {
  response: string;
}

const QueryResult: React.FC<QueryResultProps> = ({ response }) => {
  return (
    <div className="mt-6 p-4 bg-gray-100 rounded-md shadow-md">
      <h3 className="text-xl font-semibold text-gray-800">Response</h3>
      <p className="mt-2 text-gray-700">
        {response || "Your response will appear here."}
      </p>
    </div>
  );
};

export default QueryResult;
