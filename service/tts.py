from TTS.api import TTS


device = 'cpu'
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True).to(device)

def text_to_speech(text: str):
    tts.tts_to_file(text, speaker_wav="voice_clone/stalin_converted.wav", language="ru", file_path="voice_clone/outputs/output.ogg")
#tts.tts_to_file("C'est le clonage de la voix.", speaker_wav="my/cloning/audio.wav", language="fr-fr", file_path="output.wav")
#tts.tts_to_file("Isso é clonagem de voz.", speaker_wav="my/cloning/audio.wav", language="pt-br", file_path="output.wav")