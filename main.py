import csv
from tinydb import TinyDB
from tinydb.database import Document
db = TinyDB('db.json', indent=4)

f=open('fruits.csv','r')
data=csv.reader(f)
for i in data:
    key=i[0]
    value=i[1]
    doc={'name':f'{key}',
         'price':f'{value}'}
    db.insert(doc)
    print(doc)

print(db.all())