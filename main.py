import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="206df14e1b6c482abe4620a51d172c50",
                                               client_secret="d385007c9b7f450fa6138030ff02a83c",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read"))
user_profile = sp.current_user()
print("User ID:", user_profile['id'])
print("Display Name:", user_profile['display_name'])
print("Email:", user_profile.get('email', 'Not Available'))
print("Profile Image URL:", user_profile['images'][0]['url'] if user_profile['images'] else "No Image")