from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from model import (
    english_to_hindi_to_japanese,
    speech_to_text,
    text_to_speech
)
import shutil
import os

app = FastAPI(title="Voice Translator API")

class TextRequest(BaseModel):
    text: str


@app.post("/translate-text")
def translate_text(req: TextRequest):
    hindi, japanese = english_to_hindi_to_japanese(req.text)

    hi_audio = text_to_speech(hindi, "hi", "hindi.mp3")
    ja_audio = text_to_speech(japanese, "ja", "japanese.mp3")

    return {
        "english": req.text,
        "hindi": hindi,
        "japanese": japanese,
        "hindi_audio": hi_audio,
        "japanese_audio": ja_audio
    }


@app.post("/translate-audio")
def translate_audio(file: UploadFile = File(...)):
    audio_path = f"temp_{file.filename}"

    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    english_text = speech_to_text(audio_path)
    hindi, japanese = english_to_hindi_to_japanese(english_text)

    hi_audio = text_to_speech(hindi, "hi", "hindi.mp3")
    ja_audio = text_to_speech(japanese, "ja", "japanese.mp3")

    os.remove(audio_path)

    return {
        "english": english_text,
        "hindi": hindi,
        "japanese": japanese,
        "hindi_audio": hi_audio,
        "japanese_audio": ja_audio
    }
