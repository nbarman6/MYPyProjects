import time
import sys

def print_lyrics():
    lyrics = [
        "Dil Mein Ab koi Khayal Bhi Nehin Hai",
        "Tere Jaaane Ka Malal Bhi Nehin Hai",
        "Muntazir Main Tha Joh Tere Aane Ka",        
        "Ab Toh Tera Intezar Hi Nehin Hai",
        "Man Mein Mere Ab Sawal Hi Nehin Hain",
        "Hua Yeh Koi Kamal Bhi Nehin Hai",
        "Jeet Gaya Tujhe Bhul Ke Main Aise Jaise",
        "Zindegi Mein Koi Haar Hi Nehin Hai",
        "Ab Toh Tera Intezar Hi Nehin Hai",
        "Ab Toh Tera Intezar Hi Nehin Hai",
        "Tere Jaaane Ka Malal Bhi Nehin Hai",
        "Ab Toh Tera Intezar...!"
    ]
    delays = [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 2.0, 4.0, 3.0,]
    
    print("I'm Done.... \n")
    time.sleep(1.2)
    
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.09)
        print() # New line after each lyric line
        time.sleep(delays[i])
print_lyrics()