import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping part
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
songs = soup.find_all(name="h3", class_="a-no-trucate")
songs_list = [song.text.strip() for song in songs]

# Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",  # Scope for modifying playlist
        redirect_uri="http://example.com",
        client_id=os.environ.get("CLIENTID"),
        client_secret=os.environ.get("CLIENTSECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)


user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
