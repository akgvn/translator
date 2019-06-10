import requests
import json

class Translator:
    baseURL = 'https://translation.googleapis.com/language/translate/v2'
    _key = ''
    _targetLocale = ''
    
    def __init__(self, targetLocale = 'en'):
        
        apiKeyRead = open('key.txt', encoding='utf8')
        self._key = apiKeyRead.read()
        apiKeyRead.close()

        print(self._key)

        self._targetLocale = targetLocale

    def translate(self, querySentence):
        # TODO If a translation is done before, don't do it again.

        query = {
            "key" : self._key, # API Key
            "target" : self._targetLocale, # Target locale
            "q": querySentence # String to translate
        }

        r = requests.get(self.baseURL, params=query)
        r = json.loads(r.text)

        try:
            translated = r["data"]["translations"][0]["translatedText"] # {'data': {'translations': [{'translatedText': 'Hello there', 'detectedSourceLanguage': 'tr'}]}}
            return translated
        except:
            print(r)
            exit

        