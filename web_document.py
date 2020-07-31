import csv

with open('tcn_doc.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    your_list = list(reader)[1:]

with open('doc_res.csv', 'w' , newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['translation_output'])

for yl in your_list:
    if yl[0] == 'text':
        continue
    with open('doc_res.csv', 'a' , newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow([yl[0]])