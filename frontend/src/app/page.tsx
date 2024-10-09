// app/page.tsx
"use client";

import { useState } from "react";
import QueryForm from "@/components/QueryForm";
import QueryResult from "@/components/QueryResult";

const HomePage = () => {
  const [response, setResponse] = useState<string>("");

  return (
    <div className="max-w-4xl mx-auto py-12">
      <h1 className="text-4xl font-bold text-center text-indigo-600 mb-8">
        LLM Task Breakdown Tool
      </h1>
      <QueryForm setResponse={setResponse} />
      <QueryResult response={response} />
    </div>
  );
};

export default HomePage;
