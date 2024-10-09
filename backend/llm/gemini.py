from .llm import LLM
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting
from google.api_core.exceptions import GoogleAPIError


class Gemini(LLM):
    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]

    def __init__(self) -> None:
        self.initialize("genai-436917", "us-central1", "gemini-1.5-flash-002")  # Initialize with empty project, location, and model name

    def initialize(self, project: str, location: str, model_name: str):
        try:
            vertexai.init(project=project, location=location)
            self.model = GenerativeModel(model_name)
            return True
        except GoogleAPIError as e:
            print(f"Error initializing Gemini model: {e}")
            return False  # Indicate failure

    def generate_content(self, prompt: str) -> str:
        try:
            print(f"Raw Prompt {prompt}")
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config,
                safety_settings=self.safety_settings,
            )
            print(f"Raw Response: {response}")
            return response.text  # Use response.text for direct access to the generated text

        # except GoogleAPIError as e:
        #     print(f"Error generating content: {e}")
        #     return ""  # Return empty string on error

        # except AttributeError as e:
        #     print(f"Error accessing response content: {e}. Is the model initialized correctly?")
        #     return ""
        
        except Exception as e:
            print(f"Error generating content: {e}")
            return ""

    def send_complex_query(self, query: str, history: dict) -> dict:
        """Break down a complex query into subtasks and identify tools"""
        prompt = self.construct_task_breakdown_prompt(query, history)
        response = self.generate_content(prompt)
        if response:
            return self.parse_response_to_json(response)
        else:
            return {}

    def get_subtasks_and_tools(self, query: str, history: dict) -> dict:
        """Get subtasks and tools needed for the complex query"""
        print("Query:", query)
        print("History:", history)
        prompt = self.construct_subtask_prompt(query, history)
        response = self.generate_content(prompt)
        print(f'Res: {response}')
        if response:
            return self.parse_response_to_json(response)
        else:
            return {}

    def execute_subtask(self, subtask: dict, history: dict) -> dict:
        """Execute a subtask"""
        prompt = self.construct_execution_prompt(subtask, history)
        response = self.generate_content(prompt)
        if response:
            return self.parse_response_to_json(response)
        else:
            return {}

    def construct_task_breakdown_prompt(self, query: str, history: dict) -> str:
        """Constructs the prompt to break down a complex task"""
        return (
            "You are an intelligent assistant that can decompose complex tasks into manageable subtasks "
            "and identify the necessary tools to accomplish each subtask.\n\n"
            f"History: {history}\n"
            f"Complex Query: \"{query}\"\n"
            "Break down the query into subtasks, specifying the tools required for each."
        )

    def construct_subtask_prompt(self, query: str, history: dict) -> str:
        """Constructs the prompt to get subtasks and tools"""
        return (
            "You are an intelligent assistant that can analyze tasks and provide the necessary subtasks "
            "along with tools required to complete each task.\n\n"
            f"History: {history}\n"
            f"Query: \"{query}\"\n"
            "Break down the query into subtasks, specifying the tools required for each."
        )

    def construct_execution_prompt(self, subtask: dict, history: dict) -> str:
        """Constructs the prompt to execute a subtask"""
        return (
            "You are an intelligent assistant that can execute subtasks with the tools available.\n\n"
            f"History: {history}\n"
            f"Subtask: \"{subtask}\"\n"
            "Execute the subtask using the appropriate tools."
        )

    def parse_response_to_json(self, response: str) -> dict:
        """Parses the response text into a JSON dictionary"""
        try:
            # Assuming the model response is JSON-like or can be parsed as such
            return eval(response)  # Caution: You may want to use a safer parser like `json.loads`
        except Exception as e:
            print(f"Error parsing response to JSON: {e}")
            return {}
