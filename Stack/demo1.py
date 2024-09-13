import tkinter as tk
from tkinter import messagebox, scrolledtext
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

# Download stopwords and punkt tokenizer if not already done
nltk.download('stopwords')
nltk.download('punkt')

# Initialize Spotify client
client_id = '3733588945814514b72d65d67dc5d622'  # Replace with your Spotify client ID
client_secret = '6889a08e5103486285d15f0e78d94afa'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Load the pre-trained emotion classifier model
emotion_classifier = pipeline('sentiment-analysis', model='bhadresh-savani/distilbert-base-uncased-emotion')

# Get the list of English stopwords
stop_words = set(stopwords.words('english'))

# Function to clean input text by removing stopwords
def clean_text(text):
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    cleaned_text = ' '.join(filtered_text)
    return cleaned_text

# Function to handle button click event for fetching recommendations
def fetch_recommendations():
    # Get user input from the text entry field
    user_input = entry.get()

    # Get selected genre preference
    genre = genre_var.get()
    genre_keyword = "Hindi Bollywood" if genre == "Bollywood" else "Hollywood"
    
    # Clean the text by removing stopwords
    cleaned_input = clean_text(user_input)
    print(f"Cleaned Text: {cleaned_input}")

    # Get emotion predictions using the pre-trained model
    predictions = emotion_classifier(cleaned_input)
    detected_emotion = predictions[0]['label']
    confidence = predictions[0]['score']

    # Print detected emotion and confidence in the console
    print(f"Detected Emotion: {detected_emotion} with confidence {confidence:.2f}")

    # Display detected emotion in a message box
    messagebox.showinfo("Detected Emotion", f"Detected Emotion: {detected_emotion} with confidence {confidence:.2f}")

    # Based on detected emotion, adjust Spotify search queries (e.g., using 'happy', 'sad', 'neutral')
    query_emotion = genre_keyword  # Default to selected genre

    if detected_emotion in ['joy', 'love']:
        query_emotion = f"happy {genre_keyword}"
    elif detected_emotion in ['sadness', 'fear']:
        query_emotion = f"sad {genre_keyword}"
    elif detected_emotion == 'anger':
        query_emotion = f"angry {genre_keyword}"
    elif detected_emotion == 'surprise':
        query_emotion = f"surprise {genre_keyword}"

    # Fetch music recommendations based on the detected emotion from Spotify
    results = sp.search(q=query_emotion, limit=10, type='track')

    # Clear the recommendations display
    recommendations_display.delete(1.0, tk.END)

    if not results['tracks']['items']:
        messagebox.showinfo("No Recommendations", f"No {query_emotion} songs found.")
    else:
        # Display each track with a clickable link
        for track in results['tracks']['items']:
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            track_url = track['external_urls']['spotify']

            # Insert the track info into the display
            track_info = f"Track: {track_name} - Artist: {artist_name}\n"
            recommendations_display.insert(tk.END, track_info)

            # Create a clickable link
            link = tk.Label(recommendations_display, text="Listen on Spotify", fg="blue", cursor="hand2")
            link.bind("<Button-1>", lambda e, url=track_url: webbrowser.open(url))
            recommendations_display.window_create(tk.END, window=link)
            recommendations_display.insert(tk.END, "\n\n")

# Function to fetch and display top artists and top tracks
def fetch_top_artists_and_tracks():
    # Fetch top artists
    top_artists = sp.search(q="top artists", limit=10, type='artist')
    
    # Fetch top tracks
    top_tracks = sp.search(q="top tracks", limit=10, type='track')

    # Clear the recommendations display
    recommendations_display.delete(1.0, tk.END)
    
    # Display top artists
    recommendations_display.insert(tk.END, "Top Artists:\n")
    for artist in top_artists['artists']['items']:
        artist_name = artist['name']
        artist_url = artist['external_urls']['spotify']

        # Insert the artist info into the display
        artist_info = f"Artist: {artist_name}\n"
        recommendations_display.insert(tk.END, artist_info)

        # Create a clickable link
        link = tk.Label(recommendations_display, text="Listen on Spotify", fg="blue", cursor="hand2")
        link.bind("<Button-1>", lambda e, url=artist_url: webbrowser.open(url))
        recommendations_display.window_create(tk.END, window=link)
        recommendations_display.insert(tk.END, "\n\n")

    # Display top tracks
    recommendations_display.insert(tk.END, "Top Tracks:\n")
    for track in top_tracks['tracks']['items']:
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        track_url = track['external_urls']['spotify']

        # Insert the track info into the display
        track_info = f"Track: {track_name} - Artist: {artist_name}\n"
        recommendations_display.insert(tk.END, track_info)

        # Create a clickable link
        link = tk.Label(recommendations_display, text="Listen on Spotify", fg="blue", cursor="hand2")
        link.bind("<Button-1>", lambda e, url=track_url: webbrowser.open(url))
        recommendations_display.window_create(tk.END, window=link)
        recommendations_display.insert(tk.END, "\n\n")

# Create a Tkinter window
root = tk.Tk()
root.title("Emotion-aware Music Recommendation")

# Create a label and text entry for user input
label = tk.Label(root, text="Enter your current emotion or specify 'party' for party mood:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create radio buttons to select between Bollywood and Hollywood
genre_var = tk.StringVar(value="Bollywood")
bollywood_radio = tk.Radiobutton(root, text="Bollywood", variable=genre_var, value="Bollywood")
hollywood_radio = tk.Radiobutton(root, text="Hollywood", variable=genre_var, value="Hollywood")
bollywood_radio.pack(pady=5)
hollywood_radio.pack(pady=5)

# Create buttons to trigger fetching recommendations and top artists/tracks
button = tk.Button(root, text="Fetch Recommendations", command=fetch_recommendations)
button.pack(pady=10)
top_artists_tracks_button = tk.Button(root, text="Fetch Top Artists and Tracks", command=fetch_top_artists_and_tracks)
top_artists_tracks_button.pack(pady=10)

# Create a scrolled text widget to display recommendations
recommendations_display = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD)
recommendations_display.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
