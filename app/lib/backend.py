import pdftotext
import csv
import re
import collections
import json
class Feat(object):
    def acceptFile(self,pdf):
        #Accept pdf function
        #pdf to text
        x = ''
        y = []
        for page in pdf:
            x += page
        y.append(x)
        return x

    def writeInCSV(self,data):
        #write content to task.csv
        with open('../task2.csv', 'a') as csvfile:
            fielda = ['', 'text']
            writer = csv.DictWriter(csvfile, fieldnames=fielda)
            # writer.writeheader()
            writer.writerow(data)
        csvfile.close()

    def processText(self,yList):
        #re works here process it
        a=yList
        a.replace('\\n', ' ')

        words = re.findall(r'\w+', a)
        most_common = collections.Counter(words).most_common(100)
        print(json.dumps(most_common, indent=4))

