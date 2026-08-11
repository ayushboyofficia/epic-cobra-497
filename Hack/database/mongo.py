import os
from pymongo import MongoClient

URI=os.getenv("MONGO_URI","")
client=MongoClient(URI)if URI else None
db=client["sessionhack"]if client else None

def col(name):return db[name]if db else None
def ins(c,d):
 col_=col(c)
 return col_.insert_one(d)if col_ else None
def fnd(c,q):
 col_=col(c)
 return list(col_.find(q))if col_ else[]
