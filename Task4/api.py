from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import csv
from flask_jsonpify import jsonpify
import pandas as pd
import json
app = Flask(__name__)
import re
import collections



def doA():
    x = []
    with open('task2.csv', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        count = 1
        for rows in csvReader:
            a = rows['text']
            lofa = a.split('\n')
            a.replace('\\n', ' ')

            words = re.findall(r'\w+', a)
            most_common = collections.Counter(words).most_common(1000)
            x.append(most_common)
            count += 1

    return json.dumps(x,indent=16)





def getData():
    # x=[]
    # with open('task2.csv', newline='\n')as csvfile:
    #     out = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in out:
    #         x.append(row)

    data = {}

    # Open a csv reader called DictReader
    with open('task2.csv', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        count=0
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = count
            data[key] = rows
            count+=1

            # Open a json writer, and use the json.dumps()
    response = json.dumps(data ,indent=4)

    # function to dump data
    # with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    #     jsonf.write(json.dumps(data, indent=4))
    return response

@app.route('/')
def apiOne():
    return render_template("view.html",data=getData())

@app.route('/w')
def apiTwo():
    return render_template("view.html",data=doA())


if __name__ == '__main__':
    app.run(debug=True)