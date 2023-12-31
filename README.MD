# AIEarth-Wrapper

Welcome to **AIEarth-Wrapper**, your local Flask server serving as a reverse proxy for OpenAI's GPT-3.5-turbo model hosted at [https://chat.aiearth.dev](https://chat.aiearth.dev).

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Legal](#legal)
- [License](#license)
- [Google Colab](#Colab)

## Description

*AIEarth-Wrapper* is a Flask-based server that acts as a reverse proxy for the OpenAI GPT-3.5-turbo model. It enables you to interact with the model through a local server, providing an easy and flexible interface for generating responses based on user messages.

## Features

- **Flask Server**: Utilizes Flask to create a web app for hosting the OpenAI reverse proxy.
- **Cross-Origin Requests**: CORS support for allowing cross-origin requests.
- **Streaming Support**: Provides both streamed and non-streamed responses based on user preferences.
- **Configurability**: Easily configurable through a `config.json` file, allowing customization of host, port, and other settings.
- **Educational Purpose**: Designed strictly for educational purposes, allowing users to explore and learn about OpenAI's GPT-3.5-turbo model.
- **Tools**: The model supports web browsing, web searching and has an inbuilt calculator.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/AIEarth-Wrapper.git
    cd AIEarth-Wrapper
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:

    ```bash
    python app.py
    ```

## Usage

Once the server is running, you can interact with the OpenAI GPT-3.5-turbo model through the provided routes:

- **Chat Completions**: `/chat/completions` (POST)
- **Get Model Information**: `/models` (GET)
- **Check Server Status**: `/` (GET)

### Example Request Body

To make a chat completion request, send a POST request to `/chat/completions` with the following JSON body:

```json
{
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."},
        {"role": "assistant", "content": "Why did the chicken cross the road?"}
    ],
    "model": "gpt-3.5-turbo",
    "temperature": 0.6,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "top_p": 1,
    "stream": false
}
```

Modify the content of the messages according to your conversation flow.

## Configuration

Modify the `config.json` file to configure the server according to your preferences:

```json
{
    "host": "0.0.0.0",
    "port": 5000,
    "debug": false,
    "global": true
}
```

## Legal

Please review the [LEGAL.MD](LEGAL.MD) file for important legal information, disclaimers, and terms of use associated with this repository.

## License

This project is licensed under the [MIT License](LICENSE.md). See the LICENSE.md file for details.

## Colab

This project is also hosted on [Google Colab](https://colab.research.google.com/drive/1R1FUZKDgYloF4iD6-ZZi8fxGZvbLy1-0?usp=sharing)

---
