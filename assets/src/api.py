# ----------------------------------- IMPORTS ----------------------------------- #

# requests module to send http requests
import requests

# fake_useragent module to generate random user agents
from fake_useragent import UserAgent

# json module to parse json data
import json

# module to get headers
from .headers.get_headers import get_headers

# typing module for type hinting
from .typing import Headers, Messages, Any

# secrets module for random numbers
from secrets import randbelow

# logging module to log errors
import logging

# ----------------------------------- LOGGING CONFIG ----------------------------------- #

# get logger
logger: logging.Logger = logging.getLogger(__name__)

# set logging level
logger.setLevel(logging.DEBUG)

# basic config
logging.basicConfig(
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)

# ----------------------------------- API CLASS ----------------------------------- #

class API(object):

    # constructor
    def __init__(self) -> None:

        """API class constructor"""

        # url to send http requests to
        self.url: str = "https://chat.aiearth.dev/api/langchain/tool/agent/edge"

        # get headers
        self.headers: Headers | dict[str, str] = get_headers(UserAgent().random, randbelow(10000))

        # log
        logger.info(f"Headers successfully generated.\n")

        # pre-made config for data
        self.base_url: str = "/api/openai"
        self.use_tools: list[str] = ["web-search", "calculator", "web-browser"]
        self.max_iterations: int = 10
        self.use_intermediate_steps: bool = True

        # log 
        logger.info(f"Config successfully generated.\n")

        # pre-make a session
        self.session: requests.Session = requests.Session()
    
    # this method retrieves a list of available models
    def get_model(self) -> dict[str, dict[str, str]]:

        """Get model used"""

        # logging info
        logger.info(f"Getting model used...\n")

        return {"data": [
            {"id": "gpt-3.5-turbo"},
        ]}

    # this method allows you to chat with chatgpt
    def chat(self,
             messages: Messages,
             model: str,
             temperature: int = 0.6,
             presence_penalty: int = 0,
             frequency_penalty: int = 0,
             top_p: int = 1,
            ) -> str:

        """Chat with ChatGPT"""

        # logging info
        logger.info(f"Chat requested...\n")

        # data to send
        data: dict[str, Any] = {
            "baseUrl": f"{self.base_url}",
            "messages": messages,
            "stream": True,
            "model": model,
            "temperature": temperature,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty,
            "top_p": top_p,
            "maxIterations": self.max_iterations,
            "returnIntermediateSteps": self.use_intermediate_steps,
            "useTools": self.use_tools
        }

        # logging info
        logger.info(f"Data successfully generated.\n")

        # send http request with session
        with self.session.post(self.url, headers=self.headers, json=data) as response:

            # logging info
            logger.info(f"Http request successfully sent.\n")

            # raise exception if http request failed
            response.raise_for_status()

            # logging info
            logger.info(f"Http request successfully received.\n")

            # iterate over response
            for line in response.iter_lines():

                # check if line is not empty
                if line:

                    # parse json data
                    delta_chunk: dict[str, Any] = json.loads(line.decode('utf-8').removeprefix("data: "))

                    # yield message
                    yield delta_chunk["message"]

        # regenerate session
        self.session = requests.Session()