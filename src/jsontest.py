import json

f_test = open('test.json', 'r')
f_write = open('nt.json', 'w')

data = f_test.read() # Reads the data as string, I guess?

j_data = json.loads(data) # Deserializes the data into a Dictionary-like structure.

print(j_data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"])