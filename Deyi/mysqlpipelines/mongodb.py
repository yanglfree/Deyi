import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost',port=27017)


db = client.deyi

db1 = client['deyi']




collection = db.articles


# collection.insert([student,student1,student2])

# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)


# result = collection.find_one({'name':'Liang'})
# print(type(result))
# print(result)


# result = collection.find_one({'_id':ObjectId('5ae96b3b5f43b8247e138915')})
# print(result)


# results = collection.find({'age':20})
# print(results)
# for result in results:
#     print(result)


# results = collection.find({'age':{'$gte':20}})
# print(results)
# for result in results:
#     print(result)

# results = collection.delete_many({'age':{'$gt':19}})
# print(results)

results = collection.find()
print(results)

# condition = {'name':'Liang'}
# selectedStudent = collection.find_one(condition)
# selectedStudent['age'] = 25
# updateResult = collection.update_one(condition,{'$set':selectedStudent})
# print(updateResult.matched_count,updateResult.modified_count)

# resultDe = collection.find_one_and_delete({'name':'Yang'})
# print(resultDe)


