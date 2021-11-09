import pymongo
import pandas
import pickle

origin_destination = "./public/data/order-uniq-20180501.txt"
route_file = "./public/data/gps-20180501.txt"

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.CarRoute
collection = db.get_collection("cars")

class Car:
    name = ""
    begin_pos = {}
    end_pos = {}
    route = pandas.DataFrame()

    def covert_json(self):
        b_pos = str(self.begin_pos)
        e_pos = str(self.end_pos)
        data = {
            "_id": self.name,
            "name": self.name,
            "begin_pos": b_pos,
            "end_pos": e_pos,
            "route": pickle.dumps(self.route)
        }
        return data


ori_data = pandas.read_csv(origin_destination, header=None)
r_data = pandas.read_csv(route_file, header=None)
print(len(ori_data))
ori_list = ori_data[0].to_list()
group = r_data.groupby(0)
for key, value in group:
    try:
            pos = ori_list.index(key)
            car = Car()
            car.name = key
            car.begin_pos = {
                "time": ori_data[1][pos],
                "longitude": ori_data[3][pos],
                "latitude": ori_data[4][pos]
            }
            car.end_pos = {
                "time": ori_data[2][pos],
                "longitude": ori_data[5][pos],
                "latitude": ori_data[6][pos]
            }
            car.route = value.drop(0, axis=1)
            collection.insert_one(car.covert_json())
    except ValueError:
        print(key)
        continue






