import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]

mycollection = mydb["products"]

filter = {"name":"Samsung S5"}

# result = mycollection.find_one(filter)
# result = mycollection.find_one({"_id": ObjectId("639c201c0a4d344e8290a5ad")})

# result = mycollection.find({
#     "name": {
#         "$eq": ["Samsung S5","Samsung S6"]
#     }
# })

result = mycollection.find({
    "name" : {"$regex":"^S" }})

# result = mycollection.find[{
#     "price" : {
#         "$gt":200 #gt greather than gte gt equal
#         }
# }]
for i in result:
    print(i)

# result = mycollection.find(filter)

# for i in result:
#     print(i)

# MONGODB OPERATORLERE İNTERNETTEN BAKABİLİRSİN !!!!!!!!!1
# MONGODB OPERATORLERE İNTERNETTEN BAKABİLİRSİN !!!!!!!!!1
# MONGODB OPERATORLERE İNTERNETTEN BAKABİLİRSİN !!!!!!!!!1
# MONGODB OPERATORLERE İNTERNETTEN BAKABİLİRSİN !!!!!!!!!1
# MONGODB OPERATORLERE İNTERNETTEN BAKABİLİRSİN !!!!!!!!!1
# MONGODB OPERATORLERE İNTERNETTEN BAKABİLİRSİN !!!!!!!!!1
# MONGODB OPERATORLERE İNTERNETTEN BAKABİLİRSİN !!!!!!!!!1
# MONGODB OPERATORLERE İNTERNETTEN BAKABİLİRSİN !!!!!!!!!1