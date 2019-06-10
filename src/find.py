# Finds the key - value pairs in a JSON file to translate.
# Usually key is "tr"

import json

jsonFileName: str = 'test.json'
targetLocale = "en"

json_file = open(jsonFileName)

file_data = json_file.read()
file_data = json.loads(file_data)

output = open("out.json", "w")

json_file.close()

def translate(stri):
    return "Translated: " + stri # TODO the real thing

def traverseAndPrint(file_data):
    if isinstance(file_data, list):
        for elem in file_data:
            traverseAndPrint(elem)
    else:
        for key in iter(file_data):
            data = file_data[key]

            if isinstance(data, list):
                traverseAndPrint(data)
            elif key == "title":
                # TODO stuff
                if isinstance(data, str):
                    title_dict = {"tr" : data}
                else:
                    title_dict = data
                
                title_dict[targetLocale] = translate(title_dict["tr"])
                
                file_data[key] = title_dict
            elif key == "tr":
                file_data[targetLocale] = translate(file_data["tr"])

traverseAndPrint(file_data)

output.write(json.dumps(file_data, indent=4, ensure_ascii=False))