# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# club:..., country:...., city.....
# Your code starts here:
import json
file = open("csv_file.txt", "r")
data = [x.strip() for x in file.readlines()]

file.close()

jsonFile = []
for i in range(0, len(data)):
    club, city, country = data[i].split(",")
    aux = {'club': club, 'country': country, 'city':city}
    jsonFile.append(aux)

file = open("json_file.txt", "w")
json.dump(jsonFile, file)

print(data)

