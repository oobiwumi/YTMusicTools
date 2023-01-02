# #####################################################################################################################
# make_playlist_clean.py - Replaces explicit songs in playlist with clean versions
# Olufemi Obiwumi
# #####################################################################################################################
import utility

# make_clean -----------------------------------------------------------------------------------------------------------
def make_clean(yt, playlist_name, new_playlist_name):
    # Get the playlist
    playlist = utility.get_playlist_from_library(yt, playlist_name)

    # Get list of tracks to add to the new playlist
    clean = 0
    dirty = 0
    cleaned = 0
    tracks_to_add = []
    for track in playlist["tracks"]:
        if not track["isExplicit"]:
            clean += 1
            tracks_to_add.append(track["videoId"])
        else:
            dirty += 1
            # Find a clean version of the album
            track_album_id = track["album"]["id"]
            track_album = yt.get_album(track_album_id)
            if "other_versions" in track_album:
                for version in track_album["other_versions"]:
                    if version["title"] == track_album["title"] and not version["isExplicit"]:
                        clean_album = yt.get_album(version["browseId"])
                        # Find the track in the clean version of the album
                        for clean_track in clean_album["tracks"]:
                            if clean_track["title"] == track["title"]:
                                cleaned += 1
                                tracks_to_add.append(clean_track["videoId"])
                                break

    # Make new playlist
    new_playlist_id = yt.create_playlist(new_playlist_name, "cleaned", privacy_status=playlist["privacy"], video_ids=tracks_to_add)
    return new_playlist_id, dirty-cleaned