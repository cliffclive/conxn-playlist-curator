# conXn's Playlist Curator

## There's not much to see here just yet. I'm still working on v0.0.0

My endgame is to build a webapp that can log a user into their Spotify account, allow them to select a playlist to work with, and 

## Reqs

python3, atom

```bash
$ sudo pip install spotipy
```

## Register Spotify App

Go to developer.spotify.com/dashboard

Dashboard -> create app

Application Name, Description, Agree to terms

Edit Settings: Set a Redirect URI _WHY?_

Save Client ID and Secret

## Write Python Code

Erase cache and prompt for user permission _WHY?_

```python
try:
	token = spotipy.util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
  	token = util.prompt_for_user_token(username)

```

Create Spotify Object

```python
spotify_object = spotipy.Spotify(auth=token)
```

Print JSON data

```python
print(json.dumps(VARIABLE, sort_keys=True, indent=4))
```

Create some terminal variables

```bash
$ export SPOTIPY_CLIENT_ID='<spotify app Client ID>'
$ export SPOTIPY_CLIENT_SECRET='<spotify app Client Secret>'
$ export SPOTIPY_REDIRECT_URI='<spotify app redirect uri>'
```
(These have to be exported again when the terminal is restarted...
	would we want to save them permanently?
	Probably something to do in a Heroku Procfile.)

## Code Walkthrough

## Let's take a look at what we got

Now explore the track files... there are 100 tracks per file,
and the files are named Zoukables0.pkl, Zoukables1.pkl, etc

Figure out what useful metadata is in this dataset.
Next, find out how to look up audio features for the track
and pull more useful metadata from there.
Finally, pull the metadata for each track in the playlist,
format it, and insert it into a database.
```
import pickle
with open('Zoukables0.pkl', 'rb') as zpkl:
		tracks = pickle.load(zpkl)
tracks.keys()
tracks['items'][0].keys()
tracks['items'][0]['track'].keys()
```


## Read The Docs

spotipy.readthedocs.io

github.com/plamere/spotipy
