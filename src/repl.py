from spotipy import Spotify
import pickle


def run(sp, username):
    user = sp.current_user()
    displayName = user['display_name']
    followers = user['followers']['total']

    while True:
        print()
        print(f">>> Welcome to Spotipy {displayName}!")
        print(f">>> You have {str(followers)} followers.")
        print()
        print("0 - Get Playlist Metadata")
        print("1 - Exit")
        print()
        choice = input("Your choice: ")

        # Search for the artist
        if choice == "0":
            playlists = sp.user_playlists(username)
            n = 0

            for playlist in playlists['items']:
                if playlist['owner']['id'] == username:
                    title = playlist['name']
                    n_tracks = playlist['tracks']['total']
                    print(f'{n}. {title} : {n_tracks} tracks')
                    n += 1

            while True:
                pl = input("Enter a playlist number to download its metadata. (or 'x' to exit) ")
                if pl == "x":
                    break
                playlist_id = playlists['items'][int(pl)]['id']
                playlist_name = playlists['items'][int(pl)]['name']
                results = sp.user_playlist(username, playlist_id,
                                          fields="tracks,next")

                tracks = results['tracks']
                n = 0
                with open(f'{playlist_name}{n}.pkl', 'wb') as dumpfile:
                    pickle.dump(tracks, dumpfile)
                while tracks['next']:
                    n += 1
                    tracks = sp.next(tracks)
                    with open(f'{playlist_name}{n}.pkl', 'wb') as dumpfile:
                        pickle.dump(tracks, dumpfile)

                '''
                Now explore the track files... there are 100 tracks per file,
                and the files are named Zoukables0.pkl, Zoukables1.pkl, etc

                Figure out what useful metadata is in this dataset.
                Next, find out how to look up audio features for the track
                and pull more useful metadata from there.
                Finally, pull the metadata for each track in the playlist,
                format it, and insert it into a database.

                import pickle
                with open('Zoukables0.pkl', 'rb') as zpkl:
                    tracks = pickle.load(zpkl)
                tracks.keys()
                tracks['items'][0].keys()
                tracks['items'][0]['track'].keys()
                '''


        # End the program
        if choice == "1":
            break

        # Debug mode: download audio analysis and audio features for a song
        if choice == "2":
            crying = '1SJtlNRJDeYHioymcvsqev'
            analysis = sp.audio_analysis(crying)
            features = sp.audio_features([crying])
            with open('Crying_Analysis.pkl', 'wb') as dumpfile:
                pickle.dump(analysis, dumpfile)
            with open('Crying_Features.pkl', 'wb') as dumpfile:
                pickle.dump(features, dumpfile)
            break
