'''import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize Spotipy client with your credentials
client_id = '3733588945814514b72d65d67dc5d622'
client_secret = '6889a08e5103486285d15f0e78d94afa'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Function to handle button click event for fetching recommendations
def fetch_recommendations():
    # Get user input from the text entry field
    user_input = entry.get()

    # Perform sentiment analysis using TextBlob
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity

    # Determine emotion based on sentiment polarity
    if sentiment > 0.5:
        emotion = "happy"
    elif sentiment < -0.5:
        emotion = "sad"
    else:
        emotion = "neutral"

    # Print detected emotion in the console
    print(f"Detected Emotion: {emotion}")

    # Display detected emotion in a message box (optional)
    messagebox.showinfo("Detected Emotion", f"Detected Emotion: {emotion}")

    # Fetch music recommendations based on the detected emotion from Spotify
    # Example: Fetching tracks based on detected emotion and filtering for Hindi Bollywood
    results = sp.search(q=f"mood:{emotion} Hindi Bollywood", limit=5, type='track')
    for track in results['tracks']['items']:
        print(f"Track: {track['name']} - Artist: {track['artists'][0]['name']}")
        # You can also add functionality to play these tracks if desired

    # Display message if no tracks found (optional)
    if not results['tracks']['items']:
        messagebox.showinfo("No Recommendations", f"No {emotion} Hindi Bollywood songs found.")

# Create a Tkinter window
root = tk.Tk()
root.title("Emotion-aware Music Recommendation")

# Create a label and text entry for user input
label = tk.Label(root, text="Enter your current emotion:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create a button to trigger fetching recommendations
button = tk.Button(root, text="Fetch Recommendations", command=fetch_recommendations)
button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
'''

import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import cv2
import numpy as np

# Initialize Spotipy client with your credentials
client_id = '3733588945814514b72d65d67dc5d622'
client_secret = '6889a08e5103486285d15f0e78d94afa'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Function to handle button click event for fetching recommendations based on face emotion
def fetch_recommendations():
    # Load pre-trained face detection and emotion recognition models
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    emotion_model = None  # Replace with your emotion recognition model initialization

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Process each detected face
        for (x, y, w, h) in faces:
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Extract face region for emotion recognition (if using a CNN model)
            face_roi = gray[y:y+h, x:x+w]
            # Perform emotion recognition (replace with actual model prediction)
            # Example:
            # detected_emotion = predict_emotion(face_roi, emotion_model)
            detected_emotion = "happy"  # Replace with actual emotion prediction

            # Display detected emotion in a message box
            messagebox.showinfo("Detected Emotion", f"Detected Emotion: {detected_emotion}")

            # Fetch music recommendations based on the detected emotion from Spotify
            # Example: Fetching tracks based on detected emotion (replace with actual Spotify API calls)
            results = sp.search(q=f"mood:{detected_emotion}", limit=5, type='track')
            for track in results['tracks']['items']:
                print(f"Track: {track['name']} - Artist: {track['artists'][0]['name']}")

            # Exit loop after processing the first detected face
            break

        # Display the frame with detected faces
        cv2.imshow('Face Emotion Detection', frame)

        # Break the loop on pressing 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Create a Tkinter window
root = tk.Tk()
root.title("Emotion-aware Music Recommendation")

# Create a button to trigger fetching recommendations based on face emotion
button = tk.Button(root, text="Detect Emotion and Fetch Recommendations", command=fetch_recommendations)
button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
