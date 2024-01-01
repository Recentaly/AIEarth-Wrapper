# ----------------------------------- IMPORTS ----------------------------------- #

# flask to create a web app
from flask import Flask, request, jsonify, Response
from flask_cors import CORS # to allow cross-origin requests

# json module to parse json data
import json

# api class
from assets.src.api import API

# typing module for type hinting
from assets.src.typing import Messages, Any

# two formats - streamed and non-streamed
from assets.src.formats.openai_streamed import get_streamed_chunk, get_streamed_last
from assets.src.formats.openai_non_streamed import get_non_streamed_response

# ----------------------------------- CONFIGURE SERVER ----------------------------------- #

# create flask app
app = Flask(__name__)

# enable cross-origin requests
CORS(app)

# ----------------------------------- READING FROM CONFIG FILE ----------------------------------- #
with open("assets/config.json", "r") as config_file:

    CONFIG = json.load(config_file)

    # parse host, port, debug from config file
    HOST: str = CONFIG["host"]
    PORT: int = CONFIG["port"]
    DEBUG: bool = CONFIG["debug"]

    # check if user wants server to be hosted on a global url
    if CONFIG["global"]:

        # import necessary modules
        from flask_cloudflared import run_with_cloudflared

        # run flask app with cloudflared
        run_with_cloudflared(app)

# ----------------------------------- API CLASS INSTANCE ----------------------------------- #
Api = API()

# ----------------------------------- ROUTES ----------------------------------- #

# main route for chat completions
@app.route("/chat/completions", methods=["POST"])
def chat() -> str:

    """Chat route"""

    # get data from request
    data: dict[str, Any] = request.get_json()

    # get messages from data
    messages: Messages = data["messages"]

    # get model from data
    model: str = data["model"]

    # get temperature from data
    temperature: int = data["temperature"]

    # get presence penalty from data
    presence_penalty: int = data["presence_penalty"]

    # get frequency penalty from data
    frequency_penalty: int = data["frequency_penalty"]

    # get top p from data
    top_p: int = data["top_p"]

    # this route is used if streaming is enabled
    def streaming():

        # generate completion
        for chunk in Api.chat(messages, model, temperature, presence_penalty, frequency_penalty, top_p):

            # yield chunk
            yield b'data: ' + str(get_streamed_chunk(model, chunk)).encode('utf-8') + b'\n\n'

        # yield last chunk
        yield b'data: ' + str(get_streamed_last(model)).encode('utf-8') + b'\n\n'

        # signal streaming end
        yield b'data: [DONE]'

    # check if streaming is enabled
    if data["stream"]:

        # return streamed response
        return Response(streaming(), mimetype='text/event-stream')
    
    else:

        # variable to store response
        response: str = ""

        # generate completion
        for chunk in Api.chat(messages, model, temperature, presence_penalty, frequency_penalty, top_p):

            # append chunk to response
            response += chunk
    
        # return non-streamed response
        return jsonify(get_non_streamed_response(model, response)), 200

# route to get openai models
@app.route("/models", methods=["GET"])
def get_model() -> str:

    """Get model used"""

    return jsonify(Api.get_models())

# root to check if server is running
@app.route("/", methods=["GET"])
def root() -> str:

    """Root route"""

    return "<h2>Server is running</h2>"

# ----------------------------------- STARTING THE SERVER ----------------------------------- #

if __name__ == "__main__":

    # run flask app
    app.run(host=HOST, port=PORT, debug=DEBUG)
