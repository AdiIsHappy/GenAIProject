# backend/modules/task_manager.py

from llm.gemini import Gemini
from pymongo import MongoClient
import datetime
import os
import json

class TaskManager:
    def __init__(self):
        self.llm = self.initialize_llm()
        self.client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017/"))
        self.db = self.client["company_db"]

    def initialize_llm(self):
        # Choose LLM based on configuration or preference
        # For example, using ChatGPT
        return Gemini()

    def breakdown_query(self, query: str) -> dict:
        history = self.get_history()
        response = self.llm.get_subtasks_and_tools(query, history)
        print(f'Response: {response}')
        subtasks = json.loads(response)  # Assuming LLM returns JSON
        self.update_history(query, subtasks)
        return subtasks

    def get_history(self):
        history_records = self.db.history.find().sort("timestamp", -1).limit(10)
        history = [record for record in history_records]
        return history

    def update_history(self, query: str, subtasks: dict):
        self.db.history.insert_one({
            "query": query,
            "subtasks": subtasks,
            "timestamp": datetime.utcnow()
        })
