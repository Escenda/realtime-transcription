import whisper
import torch
import torchaudio
import numpy as np


class Transcribe:
	default_model_name = "large-v3"

	def __init__(self, model_name=default_model_name):
		self.model_name = model_name
		self.model = None
		self.transcriber = None
	
	def load_model(self):
		self.model = whisper.load_model(self.model_name)
	
	def transcribe(self, audio):
		segments, info = self.model.transcribe(
			audio=audio,
			language="ja",
			initial_prompt="音声が小さかったり、音質が悪いと、文字起こしすることができません。",
			beam_size=5,
			word_timestamps=True,
			condition_on_previous_text=True
		)
		return list(segments)
	
	def ts_words(self, segments):
		words = []
		for segment in segments:
			for word in segment["words"]:
				words.append(word)
		return words