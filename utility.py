# #####################################################################################################################
# utility.py - useful methods
# Olufemi Obiwumi
# #####################################################################################################################

# get_playlist_from_library - returns the playlist if it exists -------------------------------------------------------
def get_playlist_from_library(yt, name):
    requested_playlist = None
    for playlist in yt.get_library_playlists():
        if playlist["title"] == name:
            requested_playlist = playlist
            break
    return yt.get_playlist(requested_playlist["playlistId"])