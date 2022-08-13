from file_to_text import FileToText
from text_to_speech import TextToSpeech

pdf_file_path = 'C:\\Users\\alexs\\Downloads\\domain-driven-design-tackling-complexity-in-the-heart-of-software.pdf'
pdf_text = FileToText.pdf_to_text(pdf_file_path)

speech_file_path = 'speech.mp3'
TextToSpeech.convert(speech_file_path, pdf_text, 'en')