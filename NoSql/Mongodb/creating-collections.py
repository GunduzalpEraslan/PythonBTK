import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]

mycollection = mydb["products"]

# product = {"name": "Samsung S5", "price": 2000}

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id)

productList = [
    {"name": "Samsung S6", "price": 3000, "description":"iyi telefon"},
    {"name": "Samsung S7", "price": 4000,"categories":["telefon","elektronik"]},
    {"name": "Samsung S8", "price": 5000},
    {"name": "Samsung S9", "price": 6000},
    {"name": "Samsung S10", "price":7000},
    {"name": "Samsung S11", "price": 8000},
    
    ]
result = mycollection.insert_many(productList)
print(result.inserted_ids)