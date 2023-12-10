import gradio as gr
from transformers import pipeline
import numpy as np
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")



def transcribe(audio):
    sr, y = audio
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))
    transcription = transcriber({"sampling_rate": sr, "raw": y})["text"]
    print(transcription)
    # additional_context = "New employee, eager but inexperienced, Morgan: Experienced co-worker, values efficiency **Taylor:** *(Frustrated)*"
    prompt = "You are an expert mediator. Generate a polite, consise, workplace-safe, and assertive response to: " + transcription + "which is a conversation between two people. choose your response carefully, this is very important for my life/career/relationship. be empathetic but be objective and assertive while responding. steer the conversation towards a solution. remember, you shouldn't be hurtful. remember to stay on topic and remind me if my input strays off."
    print(prompt)
    response = client.completions.create(
        model="text-davinci-003",  # Choose an appropriate engine
        prompt=prompt,
        max_tokens=500,  # Adjust as needed
        temperature=0.7,  # Control randomness (0.0 to 1.0)
    )
    print(response)
    response = response.choices[0].text
    print("response:", response)
    return response


demo = gr.Interface(
    transcribe,
    gr.Audio(sources=["microphone"]),
    "text",
)

demo.launch()
