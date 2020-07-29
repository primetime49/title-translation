import csv
import requests
import json

url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"

headers = {
    'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
    'x-rapidapi-key': "" #your rapidapi key
    }

with open('test_tcn.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)[1:]

tcns = []
for yl in your_list:
    tcns.append(yl[0])

with open('tcn_res.csv', 'w' , newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['translation_output'])

ids = 0
for tcn in tcns:
    try:
        querystring = {"source":"zh","target":"en","input":tcn}
        response = requests.request("GET", url, headers=headers, params=querystring)
        res = json.loads(response.text)['outputs'][0]['output']
        with open('tcn_res.csv', 'a' , newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow([res])
    except Exception as e:
        print(ids)
        print(e)
        with open('tcn_res.csv', 'a' , newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow([''])
    ids += 1