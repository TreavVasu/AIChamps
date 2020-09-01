import collections
import pandas as pd
import csv
import re
import json
import matplotlib.pyplot as plt
# %matplotlib inline
# Read input file, note the encoding is specified here
# It may be different in your text file

def doAcount(row):
    a = row
    lofa = a.split('\n')
    a.replace('\\n',' ')

    words = re.findall(r'\w+', a)
    most_common = collections.Counter(words).most_common(100)
    print(json.dumps(most_common,indent=4))

x=[]
with open('../../task2.csv', encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    count = 1
    for rows in csvReader:
        x.append(rows)
        doAcount(rows['text'])
        count+=1

