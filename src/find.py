# Finds the key - value pairs in a JSON file to translate.
# Usually key is "tr"

import html

import json

import translator

from tag_stripper import strip_tags

jsonFileName: str = 'test.json'
targetLocale = "en"

json_file = open(jsonFileName, encoding='utf8')

file_data = json_file.read()
file_data = json.loads(file_data)

output = open("out.json", "w", encoding='utf8')

json_file.close()

def translate(stri):
    # TODO don't try to translate the empty strings!
    
    stri = strip_tags(stri)
    stri = html.unescape(stri)

    translator = translator.Translator()

    return translator.translate(stri) # TODO the real thing

def traverseAndPrint(file_data):
    # Recursive implementation to find strings in a JSON file for translating.

    if isinstance(file_data, list):
        for elem in file_data:
            traverseAndPrint(elem)
    else:
        for key in iter(file_data):
            data = file_data[key]

            if isinstance(data, list):
                traverseAndPrint(data)
            elif (isinstance(data, dict)) and ("tr" in data.keys()):
                data[targetLocale] = translate(data["tr"])  # Do the translation
            elif key == "title":
                if isinstance(data, str):
                    title_dict = {"tr" : data}
                elif isinstance(data, dict):
                    title_dict = data
                
                title_dict[targetLocale] = translate(title_dict["tr"]) # Do the translation
                file_data[key] = title_dict # Append translation to the dictionary

traverseAndPrint(file_data)

output.write(json.dumps(file_data, indent=4, ensure_ascii=False)) # Dump the dictionary into a JSON file