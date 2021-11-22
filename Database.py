import pandas
import pymongo
from io import StringIO
import pickle

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.CarRoute
collection = db.get_collection("cars")

x = collection.find_one()
print(x)
b_pos = eval(x["begin_pos"])
e_pos = eval(x["end_pos"])
nTime = e_pos["time"] - b_pos["time"]
df = pickle.loads(x["route"])
df.reset_index(drop=True, inplace=True)
print(df)
print(df.loc[0:20, :])
print(df.loc[:, 2:3])
print(nTime/60)
str = df.to_json(orient="values")
print(str)

