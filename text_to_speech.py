import webbrowser
from gtts import gTTS

class TextToSpeech:
    def convert(file_path, text, lang):
        text_to_speech_object = gTTS(text=text, lang=lang, slow=False)
        text_to_speech_object.save(file_path)
        webbrowser.open(file_path)