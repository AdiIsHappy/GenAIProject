# backend/app.py

import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from modules.task_manager import TaskManager
from modules.tool_executor import ToolExecutor
from modules.response_aggregator import ResponseAggregator
import json

# Setup logger
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

app = FastAPI()

task_manager = TaskManager()
tool_executor = ToolExecutor()
response_aggregator = ResponseAggregator()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    final_response: str

@app.post("/process_query", response_model=QueryResponse)
def process_query(request: QueryRequest):
    try:
        # logger.debug(f"Received request to process query: {request.query}")
        # Step 1: Breakdown the query into subtasks
        subtasks = task_manager.breakdown_query(request.query)
        # logger.debug(f"Subtasks generated: {json.dumps(subtasks, indent=2)}")
        print(subtasks)
        return QueryResponse(final_response=json.dumps(subtasks, indent=2))
        # Step 2: Execute each subtask
        results = []
        for subtask in subtasks.get("subtasks", []):
            tool = subtask.get("tool")
            params = subtask.get("params", {})
            # logger.debug(f"Executing subtask with tool: {tool} and params: {params}")
            result = tool_executor.execute_tool(tool, params)
            # logger.debug(f"Result for subtask: {result}")
            results.append(result)

        # Step 3: Aggregate the results into a final response
        final_response = response_aggregator.aggregate_responses(results, request.query)
        # logger.debug(f"Final aggregated response: {final_response}")

        return QueryResponse(final_response=final_response)

    except Exception as e:
        # logger.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail=str(e))
