import requests
import json

class Translator:
    baseURL = 'https://translation.googleapis.com/language/translate/v2'
    _key = ''
    _targetLocale = ''
    translations_in_hand = {}
    
    def __init__(self, targetLocale):
        
        apiKeyRead = open('key.txt', encoding='utf8')
        self._key = apiKeyRead.read()
        apiKeyRead.close()

        self._targetLocale = targetLocale

        prepared_translations = open("translation_db/locale-"+targetLocale+".json", "r", encoding='utf8')
        self.translations_in_hand = prepared_translations.read()
        self.translations_in_hand = json.loads(self.translations_in_hand)

    def translate(self, querySentence):
        if (querySentence in self.translations_in_hand.keys()):
            print("Already in db\n") # FIXME might delete later
            return self.translations_in_hand[querySentence]

        query = {
            "key" : self._key, # API Key
            "target" : self._targetLocale, # Target locale in 2 letters standard form
            "q": querySentence # String to translate
        }

        r = requests.get(self.baseURL, params=query)
        print("Sent a request.\n") # FIXME might delete later
        r = json.loads(r.text)

        try:
            translated = r["data"]["translations"][0]["translatedText"] # {'data': {'translations': [{'translatedText': 'Hello there', 'detectedSourceLanguage': 'tr'}]}}
            translated = translated.strip()
            self.translations_in_hand[querySentence] = translated
            return translated
        except:
            print(r)
            exit

    def close(self):
        prepared_translations = open("translation_db/locale-"+self._targetLocale+".json", "w", encoding='utf8')
        prepared_translations.write(json.dumps(self.translations_in_hand, indent=4, ensure_ascii=False)) # Dump the dictionary into a JSON file
        prepared_translations.close()