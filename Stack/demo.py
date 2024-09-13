'''def firstOccurence(arr,key):
    start = 0
    end = len(arr) - 1
    ans = -1

    while start<=end:
        mid = (start+end)//2
        if(arr[mid]>=key):
            ans = mid
            end = mid - 1
       
        else:
            start = mid + 1
    
    return ans

def LastOccurence(arr,key):
    start = 0
    end = len(arr) - 1
    ans = -1

    while start<=end:
        mid = (start+end)//2
        if(arr[mid]>key):
            ans = mid - 1
            end = mid - 1
        
        else:
            start = mid + 1
    
    return ans





ar = [1,2,3]

x = 1

d = firstOccurence(ar,x)

print(d)


f = LastOccurence(ar,x)
print(f)'''



#find out correct pivot position
'''def pivot_place(arr,first,last):
    pivot = arr[first]
    left = first + 1
    right = last


    while True:

        while left<=right and arr[left]<=pivot:
            left+=1
        
        while left<=right and arr[right]>= pivot:
            right-=1

        
        if right < left :
            break
        else:
            arr[left],arr[right] = arr[right],arr[left]
    
    arr[first],arr[right] = arr[right],arr[first]
    return right


def Quicksort(arr,first,last):

    if first<last:

        p = pivot_place(arr,first,last)
        Quicksort(arr,first,p-1)
        Quicksort(arr,p+1,last)
    


    


                  
a = [5,4,3,2,1]
length = len(a) - 1
Quicksort(a,0,length)
print(a)


'''

"""dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"



word = sentence.split()


for i in range(len(word)):
    for word_dict in dictionary:
        if word[i].startswith(word_dict):
            word[i] = word_dict
            break





res = ' '.join(word)


print(res)


"""



'''def fact(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return int(result)

print(fact(5))





n = 5
r = 2



equ1 = fact(n)
equ2 =  fact(r) * fact(n-r)


combination = int(equ1/equ2)

permutation = int(equ1) / fact(n-r)

print(combination)
print(permutation)


'''

import tkinter as tk
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
    user_input = entry.get().lower()  # Convert input to lowercase for case insensitivity

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

    # Check if user wants party mood songs
    if 'party' in user_input or 'celebrate' in user_input or 'festive' in user_input:
        emotion = "party"

    # Print detected emotion in the console
    print(f"Detected Emotion: {emotion}")

    # Display detected emotion in a message box (optional)
    messagebox.showinfo("Detected Emotion", f"Detected Emotion: {emotion}")

    # Fetch music recommendations based on the detected emotion from Spotify
    # Example: Fetching tracks based on detected emotion and filtering for Hindi Bollywood
    if emotion == "party":
        results = sp.search(q=f"genre:party", limit=5, type='track')
    else:
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
label = tk.Label(root, text="Enter your current emotion or specify 'party' for party mood:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create a button to trigger fetching recommendations
button = tk.Button(root, text="Fetch Recommendations", command=fetch_recommendations)
button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
