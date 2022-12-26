import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

# mycollection.update_one(
#     {'name': 'Samsung S6'}, 
#     {'$set': {
#         'name': 'IPhone 7',
#         'price': 5000
#     }}    
# )
query = {'name': 'Samsung S7'}

newvalues = {'$set': {
                'name': 'IPhone 8',
                'price': 5000
            }} 

result = mycollection.update_many(query, newvalues)

print(f'{result.modified_count} adet kayıt güncellendi.')

for i in mycollection.find():
    print(i)