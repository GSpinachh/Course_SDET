import json
import csv

with open('in.json', 'r') as file:
    data = json.load(file)

def filter(entries):
    for entry in entries:
        if ('+1' in entry['phoneNumber'] or entry['phoneNumber'].startswith('1')) and '4.0 Safari' in entry['userAgent']:
            yield entry

with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'email', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for user in filter(data):
        writer.writerow({'name': user['name'], 'email': user['email'], 'address': user['address']})
        
print("Данные фильтрации сохранены в новом файле: output.csv")
