import csv

data = open('Shuffled_Dataset.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data) #Converts each row into a list inside of a list
count_artist = {}
for line in data_lines[1:]:
     #print(line[1])
     split_line = line[1].split(', ')
     for name in split_line:
          if name in count_artist:
               count_artist[name] += 1
          else:
               count_artist[name] = 1

sorted_count_artist = sorted(count_artist.items(), key = lambda t:t[1]) 
flipped_count_artist = [ele for ele in reversed(sorted_count_artist)]
print(flipped_count_artist)


def initiate_csv():
     file = open('Sorted_shuffled_songs.csv','w', newline='')
     csv_writer = csv.writer(file,delimiter = ',')
     csv_writer.writerow(['Artist Names','Artist Appearence'])
     file.close()
     
     file = open('Sorted_playlist.csv','w', newline='')
     csv_writer = csv.writer(file,delimiter = ',')
     csv_writer.writerow(['Artist Names','Artist Appearence'])
     file.close()


def add_csv(file_name,data):
     file = open(f'{file_name}.csv','a', newline='',encoding="utf-8")
     csv_writer = csv.writer(file,delimiter = ',')
     csv_writer.writerow([row,current_track_info['artists'],current_track_info['track_name']])
     file.close()


def main():
     file1 = 'Sorted_shuffled_songs'
     file2 = 'Sorted_playlist'

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
            
          
          

if __name__ == '__main__':
     main()