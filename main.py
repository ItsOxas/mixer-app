import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="206df14e1b6c482abe4620a51d172c50",
                                               client_secret="206df14e1b6c482abe4620a51d172c50",
                                               redirect_uri="http://example.com",
                                               scope="user-library-read"))