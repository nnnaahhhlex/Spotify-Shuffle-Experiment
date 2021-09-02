import csv
data = open('Data_1000.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data)
count_artist = {}
for line in data_lines[1:]:
     #print(line[1])
     if line[1] in count_artist:
     	count_artist[line[1]] += 1
     else:
     	count_artist[line[1]] = 1

sorted_count_artist = sorted(count_artist.items(), key = lambda t:t[1]) 
fliped_count_artist = [ele for ele in reversed(sorted_count_artist)]
print(fliped_count_artist)

