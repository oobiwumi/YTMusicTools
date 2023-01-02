# IMPORTS ######################################################################
from ytmusicapi import YTMusic
import make_playlist_clean

# main #########################################################################
def main():
    yt = YTMusic('headers_auth.json')
    make_playlist_clean.make_clean(yt, "Bumpin'", "BumpinClean")


# get_songs_in_playlist_ytm ----------------------------------------------------
def get_songs_in_playlist_ytm(yt, name):
    all_playlists = yt.get_library_playlists()
    requested_playlist = None
    for playlist in yt.get_library_playlists():
        if playlist["title"] == name:
            requested_playlist = playlist
            break
    playlist_id = requested_playlist["playlistId"]
    songs = yt.get_playlist(playlist_id, limit=None)["tracks"]
    return songs, [get_song_info_ytm(song) for song in songs]

# get_song_info_ytm ------------------------------------------------------------
def get_song_info_ytm(song):
    song_info = {"title": song["title"],
                 "artist": song["artists"][0]["name"],
                 "album": song["album"]["name"]}
    return song_info


# ##############################################################################
if __name__ == '__main__':
    main()
