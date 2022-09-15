# https://pythonbasics.org/transcribe-audio/


import speech_recognition as sr
from pydub import AudioSegment


def main():
    AUDIO_FILE = "transcript.wav"

    # Load & convert mp3 to wav format saving it
    sound = AudioSegment.from_mp3("audio.MP3")
    sound.export(AUDIO_FILE, format="wav")

    # Feed file to speech recognition system
    r = sr.Recognizer()
    # Convert audio file to text
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read entire audio file
        print(f"Transcription: {r.recognize_google(audio, language='es')}")

    # Save text to txt file
    ...


if __name__ == "__main__":
    main()
