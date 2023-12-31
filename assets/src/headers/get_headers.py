from ..typing import Headers, User_Agent

def get_headers(user_agent: User_Agent, content_length: int) -> Headers | dict[str, str]:

    return {

        "Authority": "chat.aiearth.dev",
        "Host": "chat.aiearth.dev",
        "User-Agent": f"{user_agent}",
        "Accept": "text/event-stream",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Content-Length": f"{content_length}",
        "Referer": "https://chat.aiearth.dev/",
        "x-requested-with": "XMLHttpRequest",
        "Origin": "https://chat.aiearth.dev",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Authorization": "Bearer nk-freegpt3", # default (free) api key
        "Connection": "keep-alive",
        "Alt-Used": "chat.aiearth.dev",
        "TE": "trailers"
}

# Path: src/headers/get_headers.py