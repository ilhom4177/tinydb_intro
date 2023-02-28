from tinydb import TinyDB
from tinydb.database import Document
db = TinyDB('db.json', indent=4)


# doc = {
#     "name":"bananas",
#     "price":12
# }
# db.insert(doc)
print(db.all())