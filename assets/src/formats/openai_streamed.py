# json dumps to convert the data to json
from json import dumps

def get_streamed_chunk(model: str, delta_content: str):

    return dumps({
        "object": "chat.completion.chunk",
        "model": f"{model}",
        "choices": [
            {
            "index": 0,
            "delta": {
                "content": f"{delta_content}",
            },
            "finish_reason": None
        }]
    })

def get_streamed_last(model: str):

    return dumps({
        "object": "chat.completion.chunk",
        "model": f"{model}",
        "choices": [
            {
            "index": 0,
            "delta": {},
            "finish_reason": "stop"
        }]
    })