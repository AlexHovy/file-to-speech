from file_to_text import FileToText
from merge_speech import MergeSpeech
from text_to_speech import TextToSpeech

pdf_file_path = 'C:\\Users\\alexs\\Downloads\\domain-driven-design-tackling-complexity-in-the-heart-of-software.pdf'
file_to_text = FileToText(pdf_file_path)
for index in range(file_to_text.page_count):
    page_text = file_to_text.get_text_by_index(index)
    if (page_text != ''):
        speech_file_path = f'speech-{index}.mp3'
        TextToSpeech.convert(speech_file_path, page_text, 'en')
        MergeSpeech.merge(speech_file_path, 'speech.mp3')
