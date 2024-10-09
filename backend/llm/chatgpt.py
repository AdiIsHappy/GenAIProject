# backend/llm/chatgpt.py

import os
import openai
from .llm import LLM

class ChatGPT(LLM):
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def send_complex_query(self, query: str, history: dict) -> dict:
        prompt = self.construct_prompt(query, history)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=prompt,
            max_tokens=1500
        )
        return response.choices[0].message['content']

    def get_subtasks_and_tools(self, query: str, history: dict) -> dict:
        prompt = self.construct_prompt(query, history)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=prompt,
            max_tokens=1500
        )
        return response.choices[0].message['content']

    def execute_subtask(self, subtask: dict, history: dict) -> dict:
        # Implement execution logic
        pass

    def construct_prompt(self, query: str, history: dict):
        # Construct a detailed prompt including history
        return [
            {"role": "system", "content": "You are an assistant that breaks down complex tasks into subtasks and identifies necessary tools."},
            {"role": "user", "content": f"History: {history}"},
            {"role": "user", "content": f"Complex Query: {query}"}
        ]
