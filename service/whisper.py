# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="lorenzoncina/whisper-small-ru")


def preprocess_audio(path):
    with open(path, "rb") as f:
        audio_bytes = f.read()
    text = pipe(audio_bytes)["text"]
    return text
