# backend/llm/llm.py

from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def send_complex_query(self, query: str, history: dict) -> dict:
        pass

    @abstractmethod
    def get_subtasks_and_tools(self, query: str, history: dict) -> dict:
        pass

    @abstractmethod
    def execute_subtask(self, subtask: dict, history: dict) -> dict:
        pass
