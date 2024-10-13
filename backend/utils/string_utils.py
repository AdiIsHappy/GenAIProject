import json
import mistune

def parse_response_to_json(text: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass  # It's not raw JSON, so continue to check for Markdown code block
    
    # Fallback: Parse as Markdown to extract JSON from code block
    markdown = mistune.create_markdown()
    parsed_content = markdown(text)

    # Check for code blocks and extract JSON
    start_idx = text.find('```json')
    if start_idx != -1:
        end_idx = text.find('```', start_idx + 3)
        if end_idx != -1:
            json_str = text[start_idx + 7:end_idx].strip()
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                return {}

    return {}