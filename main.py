from ytmusicapi import YTMusic
from ytmusicapi.auth.oauth import OAuthCredentials  # Make sure to import OAuthCredentials

ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id="your_client_id", client_secret="your_client_secret"))

print(ytmusic.get_history()[0]["title"])