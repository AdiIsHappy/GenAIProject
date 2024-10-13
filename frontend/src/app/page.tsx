// app/page.tsx
"use client";

import { useState } from "react";
import QueryForm from "@/components/QueryForm";
import QueryResult from "@/components/QueryResult";

const HomePage = () => {
  const [response, setResponse] = useState<string>("");

  return (
    <div className="w-full h-full flex flex-col py-4">
      <h1 className="text-4xl font-bold text-black-600 mb-8">
        LLM Task Breakdown Tool
      </h1>
      <div className="flex-1 flex flex-row h-full pb-8">
        <div className="h-full flex-1">
          <QueryForm setResponse={setResponse} />
        </div>
        <div className="flex-1 h-full">
          <QueryResult response={response} />
        </div>
      </div>
    </div>
  );
};

export default HomePage;
