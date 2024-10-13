# backend/modules/task_manager.py

from llm.gemini import Gemini
import datetime
import json
from tools.db_tools import getToolsInfo

class TaskManager:
    def __init__(self):
        self.llm = self.initialize_llm()
        self.history = []

    def initialize_llm(self):
        # Choose LLM based on configuration or preference
        # For example, using ChatGPT
        return Gemini()

    def breakdown_query(self, query: str) -> dict:
        history = self.get_history()
        tools = getToolsInfo()
        subtasks = self.llm.get_subtasks_and_tools(query, history, tools)
        self.update_history(query, subtasks)
        return subtasks

    def get_history(self):
        return self.history[-10:]  # Return the last 10 history records

    def update_history(self, query: str, subtasks: dict):
        self.history.append({
            "query": query,
            "subtasks": subtasks,
            "timestamp": datetime.datetime.utcnow()
        })
