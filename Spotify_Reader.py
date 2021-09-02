
# Be able to fetch the current song playing
# Write the name of the song and artist and such to a csv file
# Change the song and iterate for a user determined amount of time

import requests
import time
import csv
from pprint import pprint


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_NEXT_TRACK_URL = 'https://api.spotify.com/v1/me/player/next'
ACCESS_TOKEN = 'BQCI3O-LbZxaInSyZ2AQ9qokC-UR0OEHKxHRv5sM_lpprAtr0AQE_ZyBOAkW5F8CgBlG8AHpE2maoz6OX0GgnqNvomg_4x_f6gn7XTrDJm5HmGKJ8oC0kijxTY5hm7_gSiOPq7SnB-myWBkL7GonrJHe7n5H'
MAX_VALUE = 1000

#Will need to get a different access code 

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
	response = requests.post(
		SPOTIFY_NEXT_TRACK_URL,
		headers={
			"Authorization": f"Bearer {access_token}"
		}
	)
	print(response) # 204 means success

	
def initiate_csv():
	file = open('Data.csv','w', newline='')
	csv_writer = csv.writer(file,delimiter = ',')
	csv_writer.writerow(['Row Number','Artist Names','Track Names'])
	file.close()


def add_csv(current_track_info,row):
	file = open('Data.csv','a', newline='',encoding="utf-8")
	csv_writer = csv.writer(file,delimiter = ',')
	csv_writer.writerow([row,current_track_info['artists'],current_track_info['track_name']])
	file.close()


def main():
	
	initiate_csv()

	current_track_id = None
	for row in range(0,MAX_VALUE):
		current_track_info = get_current_track(ACCESS_TOKEN)
		
		if current_track_info['id'] != current_track_id:
			pprint(
			current_track_info,
				indent=4,
				
			)
			print('\n')
			current_track_id = current_track_info['id']
		
		add_csv(current_track_info,row)
		next_song(ACCESS_TOKEN)
		time.sleep(1)        
		
		

if __name__ == '__main__':
	main()

