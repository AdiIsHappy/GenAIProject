# backend/modules/response_aggregator.py

from llm.gemini import Gemini
from pymongo import MongoClient
import os
import datetime

class ResponseAggregator:
    def __init__(self):
        self.llm = Gemini()
        self.client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017/"))
        self.db = self.client["company_db"]

    def aggregate_responses(self, results: list, query: str) -> str:
        history = self.get_history()
        prompt = self.construct_prompt(results, query, history)
        response = self.llm.send_complex_query(prompt, history)
        self.update_history(query, results, response)
        return response

    def get_history(self):
        history_records = self.db.history.find().sort("timestamp", -1).limit(10)
        history = [record for record in history_records]
        return history

    def construct_prompt(self, results: list, query: str, history: dict):
        return [
            {"role": "system", "content": "You are an assistant that aggregates subtask results into a final response."},
            {"role": "user", "content": f"History: {history}"},
            {"role": "user", "content": f"Query: {query}"},
            {"role": "user", "content": f"Subtask Results: {results}"}
        ]

    def update_history(self, query: str, results: list, final_response: str):
        self.db.history.insert_one({
            "query": query,
            "subtasks_results": results,
            "final_response": final_response,
            "timestamp": datetime.utcnow()
        })
