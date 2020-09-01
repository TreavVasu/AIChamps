import pdftotext
import csv

#All for getting pdf file data

def getPdfData(pdf):
    #pdf argument here is open()
    print('Method Print:')
    x=''
    y=[]
    for page in pdf:
        x+=page
    y.append(x)
    return y

# CSV file data entry
def csvWork(index,datum):
    # data = {'': 0, 'text': getPdfData()}
    data={'':index,'text':datum}
    print('CSV Work')
    # For changing to append insted of overwrite replace 'w' with 'a'
    with open('../../task2.csv', 'a') as csvfile:
        fielda = ['', 'text']
        writer = csv.DictWriter(csvfile,fieldnames=fielda)
        # writer.writeheader()
        writer.writerow(data)
    csvfile.close()
    print('Done!')

def formatString(x):
    y= x.replace("|", "")
    y= x.replace(" ", "")
    return y.encode('UTF-8')

count=0



#Initializetion for earlier automation
# for i in range(2,51):
#     count+=1
#     with open(r"pdf/"+str(i)+".pdf", "rb") as f:
#         pdf=pdftotext.PDF(f)
#         x = getPdfData(pdf)
#         y = formatString(x[0])
#         print(y)
#         csvWork(i-1,y)
#     f.close()
#     print(count)

#
# with open(r"", "rb") as f:
#     pdf = pdftotext.PDF(f)