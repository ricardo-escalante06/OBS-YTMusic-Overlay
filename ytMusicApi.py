from ytmusicapi import YTMusic
from ytmusicapi.auth.oauth import OAuthCredentials
import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id=client_id, client_secret=client_secret))

def get_Song_title():
    current_name = ytmusic.get_history()[0]["title"]
    return current_name

def get_Song_thumbnail():
    current_thumbnail_URL = ytmusic.get_history()[0]["thumbnails"][0]["url"]
    return current_thumbnail_URL

def download_thumbnail(url, save_path="thumbnail.jpg"):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Thumbnail saved as {save_path}")
    else:
        print("Failed to download thumbnail")

def delete_thumbnail(file_path="thumbnail.jpg"):
        os.remove(file_path)


# URL = get_Song_thumbnail()
# download_thumbnail(URL)