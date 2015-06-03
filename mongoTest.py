from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')
db = client.sc_database
employees = db["employees"]

employees.insert({"name": "Lucas Hightower", 'gender':'m', 'phone':'520-555-1212', 'age':8})
employees.insert({"name": "Alpha Centauri", 'gender':'m', 'phone':'520-532-1222', 'age':98})
employees.insert({"name": "Bainsley Altmore", 'gender':'f', 'phone':'512-668-4512', 'age':37})
employees.insert({"name": "Carrey Moore", 'gender':'m', 'phone':'420-533-4394', 'age':42})
employees.insert({"name": "Albricht Fulmore", 'gender':'f', 'phone':'132-515-0912', 'age':31})
employees.insert({"name": "Marcus Waynright", 'gender':'m', 'phone':'520-555-1212', 'age':14})


cursor = db.employees.find()
for employee in db.employees.find():
    print employee

print '\n >>> continue to query <<<\n'

print employees.find({"name":"Alpha Centauri"})[0]


#cursor = employees.find({"age": {"$lt": 35}})
#for employee in cursor:
#     print "under 35: %s" % employee


bainsley = employees.find_one({"_id":ObjectId("556f3bdbacef4a705bbcdd0c")})
print "Bainsley -- %s" % bainsley['age']
