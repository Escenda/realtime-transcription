import speech_recognition as sr
import pyaudio
import numpy as np

from libraries.transcribe import Transcribe


def get_microphone_index():
	p = pyaudio.PyAudio()
	for i in range(p.get_device_count()):
		info = p.get_device_info_by_index(i)
		print(info)
	return None

def listen(microphone_index, callback):
	p = pyaudio.PyAudio()

	stream = p.open(
		format=pyaudio.paInt16,
		channels=1,
		rate=16000,
		input=True,
		frames_per_buffer=16384,
		input_device_index=microphone_index
	)

	while True:
		try:
			audio_data = stream.read(16384)
			data = np.frombuffer(audio_data, dtype=np.int16)
			callback(data)

		except Exception as e:
			print(f"エラーが発生しました: {e}")
		except KeyboardInterrupt:
			print("終了します。")
			break
		
	# ストリームを終了
	stream.stop_stream()
	stream.close()
	p.terminate()