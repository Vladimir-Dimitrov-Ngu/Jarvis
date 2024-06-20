from TTS.api import TTS

device = "cpu"
tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True
).to(device)


def text_to_speech(text: str):
    tts.tts_to_file(
        text,
        speaker_wav="voice_clone/stalin_converted.wav",
        language="ru",
        file_path="voice_clone/outputs/output.ogg",
    )
