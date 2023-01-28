import json

if __name__ == '__main__':
    dict_data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    with open("02_json_data.json", "w", encoding="utf8") as f:
        json.dump(dict_data, f)
