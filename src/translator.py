import requests
import json

class Translator:
    baseURL = 'https://translation.googleapis.com/language/translate/v2'
    _key = ''
    query = {}
    _targetLocale =''
    
    def __init__(self, targetLocale = 'en'):
        
        apiKeyRead = open('key.txt')
        _key = apiKeyRead.read()
        apiKeyRead.close()

        _targetLocale = targetLocale

    def translate(querySentence):
        # TODO gotta send get requests.

        query = {
            "key" : _key, # API Key
            "target" : _targetLocale, # Target locale
            "q": querySentence # String to translate
        }

        r = requests.get(baseURL, params=query)
        r = json.loads(r.text)
        translated = r["data"]["translations"][0]["translatedText"] #{'data': {'translations': [{'translatedText': 'Hello there', 'detectedSourceLanguage': 'tr'}]}}
        return translated