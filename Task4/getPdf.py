import csv

def getData():
    x=[]
    with open('task2.csv', newline='\n')as csvfile:
        out = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in out:
            x.append(row)
    return x

with open('task2.csv',newline='\n')as csvfile:
    out=csv.reader(csvfile,delimiter=' ', quotechar='|')

    for row in out:
        x.append(row)
        # print(','.join(row))

z=getData(x)
