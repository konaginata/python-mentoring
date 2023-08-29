import csv
import json

with open('cars.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = [row for row in reader]

json_data = json.dumps(data, indent=2)

with open('cars.json', 'w') as json_file:
    json_file.write(json_data)
