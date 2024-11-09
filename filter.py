import json
import csv

# Загрузка данных из файла JSON
with open('in.json', 'r') as file:
    data = json.load(file)

# Генератор для фильтрации пользователей
def filter(entries):
    for entry in entries:
        if ('+1' in entry['phoneNumber'] or entry['phoneNumber'].startswith('1')) and '4.0 Safari' in entry['userAgent']:
            yield entry

# Сохранение данных в CSV файл
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'email', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for user in filter(data):
        writer.writerow({'name': user['name'], 'email': user['email'], 'address': user['address']})
        
print("Данные фильтрации сохранены в новом файле: output.csv")
