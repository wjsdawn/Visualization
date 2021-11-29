import pymongo


def get_coll():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.CarRoute
    collection = db.get_collection("cars")
    return collection


