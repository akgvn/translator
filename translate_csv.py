# Reads csv files and translates them to the target lang.

import google_translator
import sys
import os


translator = google_translator.Translator("en")

def translation_handler(to_translate):
    to_translate = to_translate.strip()

    if (not to_translate):
        return ""

    return translator.translate(to_translate)

if __name__ == "__main__": # Doesn't execute when called from another file.
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()+"\\csv_to_translate"): # Search for CSV files in that folder.
        for filename in filenames:
            if filename.endswith('.csv'):
                filename = os.sep.join([dirpath, filename]) # get file location

                print("\nFile to translate:", filename)

                csvFileName = filename
                targetLocale = 'en' # Target Locale, change this when needed.

                to_translate: list = []

                with open(csvFileName, "r", encoding='cp1254') as csv_file:
                    csv_data = csv_file.read().split("\n")
                    for row in csv_data:
                        row = row.split("|")
                        to_translate.append(row)

                row_count = 0
                for rows in to_translate:
                    col_count = 0
                    for col in rows:
                        if col_count > 8:
                            break
                        if row_count > 0:
                            to_translate[row_count][col_count] = translation_handler(col)
                        col_count += 1
                    row_count += 1

                # print(to_translate) # All rows and columns are read.

                with open(csvFileName, "w", encoding='utf8') as csv_file:
                    for rows in to_translate:
                        csv_file.write("|".join(rows) + "\n")

                translator.close()
    print("Done!")