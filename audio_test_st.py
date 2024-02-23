import os
import speech_recognition as sr
from openai import OpenAI
import dotenv
dotenv.load_dotenv()

# Set your OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = "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"

# Obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

# Use OpenAI to transcribe the audio file
client = OpenAI()

audio_file_path = "microphone-results.wav"
with open(audio_file_path, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )

# Print the transcription
print("Transcription:")
print(transcript)
