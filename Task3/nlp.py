import collections
import pandas as pd
import csv
import re
import matplotlib.pyplot as plt
# %matplotlib inline
# Read input file, note the encoding is specified here
# It may be different in your text file

def doA(row):
    a = row
    lofa = a.split('\n')
    a.replace('\\n',' ')

    words = re.findall(r'\w+', a)
    most_common = collections.Counter(words).most_common(100)
    print(most_common)
    print()

x=[]
with open('task2.csv', encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    count = 1
    for rows in csvReader:
        x.append(rows)
        doA(rows['text'])
        # print(rows['']) => 1,2,3,4

        # print(rows['text'])
        count+=1

