import requests
import time
import csv
from pprint import pprint


PLAYLIST_ID = '7iXqUa7mZJFCzlNpHfuQWs'
SPOTIFY_GET_PLAYLIST_URL = 'https://api.spotify.com/v1/playlists/7iXqUa7mZJFCzlNpHfuQWs/tracks'
ACCESS_TOKEN = 'BQB4eHEW3nfZjgqLLoqDPuwMSka2ZqZDln-XnnTv1P1LdPj6PGuKlbWnU9Czjr1RtV8n25eb4YK6laCoWM3kX3v8q1nW2-6XIDsTn4tF-MB4HCLbuhlt2snFSDPfkV_5f7w31L9FJODDk7gTcM900mvXB_c5BgEB_1iGw8A'
MAX_VALUE = 1000

#Will need to get a different access code 

def get_playlist(access_token):
	response = requests.get(
		SPOTIFY_GET_PLAYLIST_URL,
		headers={
			"Authorization": f"Bearer {access_token}"
		}
	)
	json_resp = response.json()
	#print(json_resp)
	tracks_list = []
	artist_list = []
	counter = 0
	for i in json_resp['items']:
		#print(i["track"]['artists'][0]['name'])
		print(i["track"]['name'])
		counter+= 1
	print(counter)
	'''
		tracks_list += (i['track']['name'] + ' , ')
		artist_list += (i['artists']['name']  + ' , ')
	tracks_list = tracks_list[:-1]
	artist_list = artist_list[:-1]
	print(tracks_list)
	print(artist_list)
	'''
	'''
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
	'''

def initiate_csv():
	file = open('Playlist_Data.csv','w', newline='')
	csv_writer = csv.writer(file,delimiter = ',')
	csv_writer.writerow(['Row Number','Artist Names','Track Names'])
	file.close()


def add_csv(current_track_info,row):
	file = open('Playlist_Data.csv','a', newline='',encoding="utf-8")
	csv_writer = csv.writer(file,delimiter = ',')
	csv_writer.writerow([row,current_track_info['artists'],current_track_info['track_name']])
	file.close()


def main():
	get_playlist(ACCESS_TOKEN)
	'''
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
	'''
		

if __name__ == '__main__':
	main()