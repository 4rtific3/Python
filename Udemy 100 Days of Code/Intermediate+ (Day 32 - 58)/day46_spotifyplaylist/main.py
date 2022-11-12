from bs4 import BeautifulSoup
import requests, spotipy, configparser
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

config_obj = configparser.ConfigParser()
config_obj.read("../../config.ini")
ID = config_obj["ids"]["SPOTIFY"]
SECRET = config_obj["api keys"]["SPOTIFY"]
URI = config_obj["uris"]["SPOTIFY"]
ACCESS_TOKEN = config_obj["tokens"]["SPOTIFY"]



BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100"
SPOTIFY_ENDPOINT = "https://api.spotify.com/v1"

SPOTIFY_HEADERS = {
    "Authorization": ACCESS_TOKEN,
}

date = input("What date do you want to get the top 100 songs from? YYYY-MM-DD\n")

response = requests.get(f"{BILLBOARD_ENDPOINT}/{date}/")
soup = BeautifulSoup(response.text, "html.parser")

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(ID, SECRET, URI, scope=scope))
user_id = sp.me()["id"]

user_playlists = sp.current_user_playlists()
user_playlist_names = [playlist["name"] for playlist in user_playlists["items"]]

if f"{date} Billboard 100" not in user_playlist_names:
    
    raw_titles = soup.find_all("h3", class_="a-no-trucate")
    titles = [title.getText().strip() for title in raw_titles]

    raw_artists = soup.find_all("span", class_="a-no-trucate")
    artists = [artist.getText().strip().replace(".", "") for artist in raw_artists]

    song_uri_list = []
    missed_songs = []

    for i in range(100):
        track = sp.search(q=f"{titles[i]}%20artist:{artists[i]}", limit=1)
        try:
            song_uri_list.append(track["tracks"]["items"][0]["uri"])
        except IndexError:
            missed_songs.append(f"{titles[i]}, {artists[i]}")
            continue

    print(f"I missed these songs: {missed_songs}")

    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, description="Top 100 songs from specified date. Made using Python and Spotipy")
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uri_list)
    print("Remember to add the new playlist to your profile!")
else:
    print(f"You already have [{date} Billboard 100] in your playlist.")