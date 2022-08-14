import ffmpeg
import os

class MergeSpeech:
    def merge(input_file_path, output_file_path):
        input = ffmpeg.input(input_file_path)
        output = ffmpeg.input(output_file_path)
        ffmpeg.concat(input, output).output('speech-merge.mp3').run()