import speech_recognition as sr
from transformers import pipeline
from pydub import AudioSegment
import re
import nltk
from nltk.corpus import stopwords

# Install necessary packages if not already installed:
# pip install transformers tf-keras pydub nltk

# Function to convert .m4a to .wav
def convert_m4a_to_wav(m4a_path, wav_path):
    try:
        audio = AudioSegment.from_file(m4a_path, format="m4a")
        audio.export(wav_path, format="wav")
        print(f"Converted {m4a_path} to {wav_path}")
    except Exception as e:
        print(f"Error converting file: {e}")

# Function to transcribe audio
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Audio not clear enough to transcribe"
    except sr.RequestError:
        return "API unavailable or quota exceeded"

# Function to preprocess text
def preprocess_text(text):
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    sentiment = sentiment_pipeline(text)
    return sentiment

# Example usage
if __name__ == "__main__":
    # File paths
    wav_path = r'C:\Users\ashis\Downloads\Real-State-Lead-Gen-1.wav'

    # Step 1: Convert M4A to WAV

    # Step 2: Transcribe Audio
    transcribed_text = transcribe_audio(wav_path)
    print("Transcribed Text:", transcribed_text)

    # Step 3: Preprocess Text
    if "Audio not clear enough to transcribe" not in transcribed_text and "API unavailable or quota exceeded" not in transcribed_text:
        preprocessed_text = preprocess_text(transcribed_text)
        print("Preprocessed Text:", preprocessed_text)

        # Step 4: Analyze Sentiment
        sentiment = analyze_sentiment(preprocessed_text)
        print("Sentiment Analysis:", sentiment)
    else:
        print("Transcription issue:", transcribed_text)
