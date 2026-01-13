from transformers import MBartForConditionalGeneration, MBart50Tokenizer
import torch
import whisper
from gtts import gTTS
import os

MODEL_PATH = "./translator_model"
AUDIO_DIR = "audio"

os.makedirs(AUDIO_DIR, exist_ok=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

# Translation model
tokenizer = MBart50Tokenizer.from_pretrained(MODEL_PATH)
model = MBartForConditionalGeneration.from_pretrained(MODEL_PATH).to(device)
model.eval()

# Speech-to-text model
stt_model = whisper.load_model("base")


def translate(text, src_lang, tgt_lang):
    tokenizer.src_lang = src_lang
    encoded = tokenizer(text, return_tensors="pt").to(device)
    with torch.no_grad():
        tokens = model.generate(
            **encoded,
            forced_bos_token_id=tokenizer.lang_code_to_id[tgt_lang],
            max_length=128
        )
    return tokenizer.decode(tokens[0], skip_special_tokens=True)


def english_to_hindi_to_japanese(text):
    hindi = translate(text, "en_XX", "hi_IN")
    japanese = translate(hindi, "hi_IN", "ja_XX")
    return hindi, japanese


def speech_to_text(audio_path):
    result = stt_model.transcribe(audio_path)
    return result["text"]


def text_to_speech(text, lang, filename):
    tts = gTTS(text=text, lang=lang)
    path = os.path.join(AUDIO_DIR, filename)
    tts.save(path)
    return path
