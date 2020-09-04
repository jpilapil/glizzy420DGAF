import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser

""""OAUTH"""
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="bd6d9259112c490390244c7832f7bea2", client_secret="7ed4f02f5bca4974a3752a3bc18b575d",
                                               redirect_uri="http://google.com/", username="12762708", scope="user-top-read"))

def getTrackUri():
    """"Get Track URI"""
    results = sp.current_user_top_tracks(limit=1, time_range="medium_term")
    
    #loop through obj extracting track URI to be used for analysis
    track_ids = []
    for item in results['items']:
        track = item['uri']
        track_ids.append(track[-22:])
      
    return track_ids

def getTrackAnalysis(li):
    """Audio Features Analysis"""
    #init dict where features will be stored and required features, spotipy method to get track features 
    playlist_audio_features = {}
    required_features = ["danceability", "energy", "speechiness", "valence", "tempo"]
    track_features = sp.audio_features(li)

    ###loop through each item in track features list then loop through k, v in each item
    for t in track_features:
        for k, v in t.items():
            ###extract required Features in each item and assign to playlist_audio_features
            if k in required_features:
                temp = playlist_audio_features.get(k, 0.0) + v
                playlist_audio_features[k] = temp
    # Calculate average for each audio feature   
    for feature in required_features:
        temp = playlist_audio_features.get(feature)
        playlist_audio_features[feature] = "{:.3f}".format(temp / 1)
    
    return playlist_audio_features

ids = getTrackUri()
userTasteProfile = getTrackAnalysis(ids)
print(userTasteProfile)










