import csv
import requests
import json
from googletrans import Translator

def main():

    translator = Translator()

    with open('test_tcn.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)[1:]

    tcns = []
    for yl in your_list:
        tcns.append(yl[0])

    with open('tcn_res.csv', mode='w') as rest_file:
        rest_writer = csv.writer(rest_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rest_writer.writerow(['translation_output'])

    translations = translator.translate(tcns, dest='en')

    with open('tcn_res.csv', mode='a') as rest_file:
        rest_writer = csv.writer(rest_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for translation in translations:
            print(translation.origin)
            rest_writer.writerow([translation.text])

if __name__ == "__main__":
    main()