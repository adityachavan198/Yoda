
# Yoda: Conversation Co-Pilot

This repository contains the code for Yoda, a Conversation Co-Pilot application that utilizes Gradio for audio transcription and response generation based on OpenAI models.

## Table of Contents

- [About](#about)
- [Features](#features)
- [API Stack](#api-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## About

Yoda is a Conversation Co-Pilot that assists users in transcribing spoken audio and generating context-aware, polite, and assertive responses to facilitate workplace conversations.

## Features

- Audio transcription using OpenAI's Whisper ASR model.
- Response generation for workplace scenarios using OpenAI's GPT-based models.
- Real-time interaction through Gradio's user-friendly interface.

## Stack

- Hugging Face (HugginFace) for transformer models
- Whisper for Automatic Speech Recognition (ASR)
- TogetherAI for collaborative features
- LangChain for language processing

## Prerequisites

Ensure you have the following prerequisites installed before using Yoda:

- Python 
- Gradio
- Transformers library
- OpenAI API key

## Installation

Clone the repository:
`git clone https://github.com/fzinnah17/Yoda`

Install the required dependencies:
`pip install -r requirements.txt`

Set your Open AI API Key:
`export OPENAI_API_KEY = "your-api-key-here"`

Run Yoda, the Conversation Co-Pilot:
`python app.py`


## Demo

https://github.com/fzinnah17/Yoda/assets/35609659/a1de4833-1239-44b2-9d6c-4a73cb595d54







## Slide Deck
[Pitch Deck](https://shorturl.at/ghnot "Pitch Deck")

## Dev Post
[Devpost](https://devpost.com/software/llmediator "Devpost")

## Usage

Launch Yoda by running the provided command.
Speak into the microphone to trigger audio transcription.
Experience real-time, context-aware response generation based on workplace scenarios.


## Future Work

The future work for Yoda, the Conversation Co-Pilot, includes:

 - Implementing a vector database to store entire conversations.
 - Allowing the Language Model (LLM) to reference back to the stored conversations.
 - Summarizing chat history and providing access to the most recent dialogue.




## Contributing

If you like to contribute to Yoda, the Conversation Co-Pilot, please follow the guidelines outlined in the CONTRIBUTING.md file.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
