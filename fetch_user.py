import pymongo
import pickle
import os
import multiprocessing
logname = os.path.basename(__file__) + '.log'

if os.path.exists(logname):
  os.remove(logname)

manager = multiprocessing.Manager()
# stopwordset = manager.dict({word : 0 for word in stopwords.words('english')})
# # 建立mongodb连接
client = pymongo.MongoClient(host='localhost', port=27017)

db = client.tiktok

# # 创建一个daily集合，类似于MySQL中“表”的概念
# group = db['group']

features = db.users
document = db.document
with open('usernames.pkl', 'rb') as f:
    usernames = pickle.load(f)
print(usernames)