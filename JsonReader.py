import json

def Read_Json_File(fileName: str):
    dataToReturn = None

    try:
        with open(fileName, "r", encoding="utf-8-sig") as file:
            data = json.load(file)
            dataToReturn = data
    except Exception as e:
        print("Ein Fehler ist aufgetreten: " + str(e))

    return dataToReturn