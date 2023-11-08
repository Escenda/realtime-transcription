from libraries.realtime import listen, get_microphone_index
from libraries.transcribe import Transcribe


def callback(tb: Transcribe, audio):
	text = tb.transcribe(audio)
	print(text)


def main():
	tb = Transcribe()
	tb.load_model()

	listen(microphone_index=2, callback=lambda audio: callback(tb, audio))


if __name__ == "__main__":
	# print(get_microphone_index())
	main()