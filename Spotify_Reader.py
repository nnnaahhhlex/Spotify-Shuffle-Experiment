#import csv

# Be able to fetch the current song playing
# Write the name if the song and artist ans such to a csv file
# Change the song and iterate for a user determined amount of time

import requests
import time

from pprint import pprint


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_NEXT_TRACK_URL = 'https://api.spotify.com/v1/me/player/next'
ACCESS_TOKEN = 'BQDlHm-cyrd79iGs4c-k2az_nTuVsFfbiOQyI4N5nqyZKBLcqW_7zWw4Pchby-K0xMFQIU4sQvh4wPW1opDcpamRVeliB8P5oopczzoUKeKupSvAC_YVzixoPTe0PWNfIRDBr46uNyjr6na2TZEj_Nvc0vpe'


def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link
    }

    return current_track_info


def next_song(access_token):



def main():
	current_track_id = None
	while True:
	    current_track_info = get_current_track(ACCESS_TOKEN)

	    if current_track_info['id'] != current_track_id:
		    pprint(
		    	current_track_info,
		    	indent=4,
		    )
		    print('\n')
		    current_track_id = current_track_info['id']

	    time.sleep(1)


if __name__ == '__main__':
    main()