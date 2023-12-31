# json dumps is needed to convert the data to json
from json import dumps

def get_non_streamed_response(model: str, message_content: str):

    """Get non-streamed response in OpenAI format"""

    return {
        "object": "chat.completion",
        "model": f"{model}",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": f"{message_content}",
                },
            "finish_reason": "stop"
        }],
    }