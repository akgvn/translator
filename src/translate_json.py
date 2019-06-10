# Finds the key - value pairs in a JSON file to translate.
# Usually key is "tr" and "title"

import html

import json

import google_translator

from tag_stripper import strip_tags

import sys

def translation_handler(to_translate):
    # TODO don't try to translation_handler the empty strings!
    
    to_translate = strip_tags(to_translate)
    to_translate = str(html.unescape(to_translate))
    to_translate = to_translate.strip()

    if (not to_translate):
        return ""

    return translator.translate(to_translate)

def traverseAndTranslate(file_data):
    # Recursive implementation to find strings in a JSON file for translating.

    if isinstance(file_data, list):
        for elem in file_data:
            traverseAndTranslate(elem)
    else:
        for key in iter(file_data):
            data = file_data[key]

            if isinstance(data, list):
                traverseAndTranslate(data)
            elif (isinstance(data, dict)) and ("tr" in data.keys()):
                data[targetLocale] = translation_handler(data["tr"])  # Do the translation
            elif key == "title":
                if isinstance(data, str):
                    title_dict = {"tr" : data}
                elif isinstance(data, dict):
                    title_dict = data
                
                title_dict[targetLocale] = translation_handler(title_dict["tr"]) # Do the translation
                file_data[key] = title_dict # Append translation to the dictionary

if __name__ == "__main__":
    jsonFileName = 'test.json'
    targetLocale = "en"

    if len(sys.argv) > 2:
        targetLocale = sys.argv[1]
        jsonFileName = sys.argv[2]
    
    json_file = open(jsonFileName, encoding='utf8')
    file_data = json_file.read()
    file_data = json.loads(file_data)
    json_file.close()

    output = open("out.json", "w", encoding='utf8')
    
    translator = google_translator.Translator(targetLocale)
    
    traverseAndTranslate(file_data)
    
    output.write(json.dumps(file_data, indent=4, ensure_ascii=False)) # Dump the dictionary into a JSON file

    output.close()

    translator.close()