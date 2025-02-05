from pydub import AudioSegment
from pydub.utils import which

# Explicitly set the path to ffmpeg
AudioSegment.converter = which(r"C:\Users\jyoji\Downloads\ffmpeg-2024-09-09-git-9556379943-full_build\ffmpeg-2024-09-09-git-9556379943-full_build\bin")  # Change to your actual ffmpeg path

import speech_recognition as sr

# Convert MP4 audio to WAV format
def convert_audio_to_wav(audio_file):
    if audio_file.endswith(".mp4"):
        audio = AudioSegment.from_file(audio_file, format="mp4")
        wav_file = audio_file.replace(".mp4", ".wav")
        audio.export(wav_file, format="wav")
        return wav_file
    return audio_file

# Transcribe audio file to Japanese text
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    audio_file = convert_audio_to_wav(audio_file)
    
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        
        try:
            print("Transcribing audio...")
            text = recognizer.recognize_google(audio, language="ja-JP")
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio"
        except sr.RequestError:
            return "API unavailable or quota exceeded"

# Specify the path to your MP4 audio file
audio_file_path = r"C:\Users\jyoji\Downloads\新規録音 9.mp4"  # Update to the correct path
transcription = transcribe_audio(audio_file_path)

print("Transcription: ", transcription)
