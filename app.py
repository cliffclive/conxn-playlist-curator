import os
import sys
import spotipy
import spotipy.util as util
from src.repl import run

def authenticate(username):
    # Erase cache and prompt for user permission
    try:
        token = util.prompt_for_user_token(username)
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username)
    return token

def main():
    # Get the username from terminal (mine is 'djconxn')
    username = sys.argv[1]
    # Sign in to Spotify
    token = authenticate(username)
    # Create our spotifyObject
    client = spotipy.Spotify(auth=token)

    run(client, username)

if __name__ == '__main__':
    main()
