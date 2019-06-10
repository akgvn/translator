import requests

targetLocale = 'en'
querySentence = 'merhaba'

# Read key from a text file.
apiKeyRead = open('key.txt')
key = apiKeyRead.read()
apiKeyRead.close()

print(key)

query = {
    "key" : key, # API Key
    "target" : targetLocale, # Target locale
    "q": querySentence # String to translate
}

baseURL = 'https://translation.googleapis.com/language/translate/v2'

def translate(q : dict):
    # TODO gotta send get requests.
    r = requests.get(baseURL, params=query)
    print(r.text) # in JSON format

translate(query)