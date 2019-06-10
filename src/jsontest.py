import json

f_test = open('test.json', 'r')
f_write = open('nt.json', 'w')

data = f_test.read() # Reads the data as a string, I guess?

j_data = json.loads(data) # Deserializes the data into a Dictionary structure.

for d in iter(j_data.values()):
    print(d)
    f_write.write(json.dumps(d, indent=4)) # Writes to file, indent=4 prettifies the json file.