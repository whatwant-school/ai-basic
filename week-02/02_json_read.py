import json

if __name__ == '__main__':
    with open("02_json_example.json", "r", encoding="utf8") as f:
        contents = f.read()
        json_data = json.loads(contents)

    # print(json_data["employees"])
    for employee in json_data["employees"]:
        print(employee["firstName"], employee["lastName"])
