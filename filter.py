import json
import csv
import os
from typing import List, Dict, Any, Generator


def read_json_file(json_file: str) -> List[Dict[str, Any]]:
    if not os.path.exists(json_file):
        print("Файл не найден")
        return []

    with open(json_file, "r") as file:
        return json.load(file)


def filter_data(user_data: List[Dict[str, Any]]) -> Generator[Dict[str, Any], None, None]:
    for user in user_data:
        if (user["phoneNumber"].startswith("+1") or 
            user["phoneNumber"].startswith("1")) and "4.0 Safari" in user["userAgent"]:
            yield user


def write_csv_file(user_data: Generator[Dict[str, Any], None, None], csv_file: str) -> None:
    fieldnames = ["name", "email", "address"]

    with open(csv_file, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        
        for data in user_data:
            writer.writerow({name: data[name] for name in fieldnames})


def main() -> None:
    json_data = read_json_file("in.json")
    filtered_data = filter_data(json_data)
    write_csv_file(filtered_data, "output.csv")
    print("Данные фильтрации сохранены в новом файле: " "output.csv")

if __name__ == "__main__":
    main()
