from ytmusicapi import YTMusic
from ytmusicapi.auth.oauth import OAuthCredentials
from dotenv import load_dotenv
import os
import time

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id=client_id, client_secret=client_secret))

On = True

def printCurrentSong():

    last_name = ytmusic.get_history()[0]["title"]
    last_id = ytmusic.get_history()[0]["videoId"]

    print(last_name)

    while On:
        current_id = ytmusic.get_history()[0]["videoId"]

        if current_id != last_id:
            print(ytmusic.get_song(current_id)["videoDetails"]["title"])
            last_id = current_id
            print("Song Changed!")
        else:
            print("No Change")
    
        time.sleep(2)