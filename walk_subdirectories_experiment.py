# Source: https://stackoverflow.com/questions/2922783/how-do-you-walk-through-the-directories-using-python
# TODO Glob modülü neymiş oku!

import os
import json

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()+"\\json_to_translate"):
    for filename in filenames:
        if filename.endswith('.json'):
            list_of_files[filename] = os.sep.join([dirpath, filename])
            print("dirpath:", dirpath.replace(os.getcwd()+"\\json_to_translate", "")) # Subdirectories of json_to_translate
            print("filename:", filename)

fil = open("things.json", "w")

sorted(list_of_files)

# print(list_of_files)

fil.write(json.dumps(list_of_files, indent=4, ensure_ascii=False))

# TODO Walk through subdirectories of json_to_translate and while walking, make directories in results file 