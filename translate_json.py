# Finds the key - value pairs in a JSON file to translate.
# Usually key is "tr" and "title"

import html
import json
import google_translator
from tag_stripper import strip_tags
import sys
import os
from collections.abc import Iterable

translator = google_translator.Translator("en")

def translation_handler(to_translate):
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
        if (not isinstance(file_data, Iterable) or isinstance(file_data, str)):
            # Can't translate nor traverse.
            return

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

if __name__ == "__main__": # Doesn't execute when called from another file.
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()+"\\json_to_translate"): # Search for JSON files in that folder.
        for filename in filenames:
            if filename.endswith('.json'):
                filename = os.sep.join([dirpath, filename]) # get file location

                print("File to translate:", filename)

                jsonFileName = filename
                targetLocale = 'en' # Target Locale, change this when needed.

                json_file = open(jsonFileName, 'r+', encoding='utf8')
                file_data = json_file.read()
                file_data = json.loads(file_data)

                translator = google_translator.Translator(targetLocale)

                try:
                    traverseAndTranslate(file_data)

                    json_file.seek(0)

                    json_file.write(json.dumps(file_data, indent=4, ensure_ascii=False)) # Dump the dictionary into a JSON file

                    json_file.close()
                finally:
                    translator.close() # Even if there is an error, save the translations to translation db.

    print("\nDone!\n")