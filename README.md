# Translator

translation_db contains the every translation done with this script to prevent redundant calls to the Google Translate API. Script checks there first to see if a string was translated before.

Calls to Google Translate API is sent through google_translator, for that module to work you need to install requests (https://2.python-requests.org/en/master/)

key.txt holds the translate API Key, google_translator reads it before requesting translations.

To translate csv files: copy your files into the csv_to_translate folder
To translate json files: copy your files into the json_to_translate folder

After doing this run the translate_csv or translate_json script depending on the format of the files you want to translate.

**IMPORTANT**: Script edits the files directly, backup your data in case anything goes wrong.