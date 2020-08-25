import pdftotext
import  csv

print('Start')
with open(r"pdf/2.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
x=[]
# Iterate over all the pages
for page in pdf:
    #print(page)
    x.append(page)
print(x)

data = {'': 0, 'text': x}
with open('task2.csv', 'w') as csvfile:
    fielda=['','text']
    writer = csv.DictWriter(csvfile,fieldnames=fielda)
    writer.writeheader()
    writer.writerow(data)



print('End')