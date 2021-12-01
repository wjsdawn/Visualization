import json
import pickle
import time
import pandas
import Database
import GH.MapMatching as matcher

timer = 0


def encapsulate():
    global timer
    coll = Database.get_coll()
    data = coll.find()
    for car in data:
        print(str(timer) + ":" + car["name"])
        df = pickle.loads(car["route"])
        arr_point = df.to_json(orient="values")
        arr = json.loads(arr_point)
        body = {
            'ak': matcher.read_key("../public/user_key"),
            'point_list': matcher.create_point_json(arr),
            'rectify_option': "need_mapmatch:1|transport_mode:driving|denoise_grade:1|vacuate_grade:1",
            'supplement_mode': "driving",
            'coord_type_output': "gcj02"
        }

        url = "https://api.map.baidu.com/rectify/v1/track?"
        res_json = matcher.request_post(url, body)
        time_points = matcher.get_matching_time_points(res_json)
        with open('./output.txt', 'a', encoding='utf-8') as fp:
            for point in time_points:
                line = car["name"]+" "+str(point[0])+" "+str(point[1])+" "+str(point[2])+'\n'
                fp.write(line)
        time.sleep(5)
        fp.close()
        timer = timer+1


# encapsulate()
pd = pandas.read_csv("./output.txt", delimiter=" ")
group = pd.groupby('id')
for key, value in group:

    data = value.loc[:, ['lon', 'lat']].to_json(orient="values")
    arr = json.loads(data)
    print(arr)
    for point in arr:
        point[0] = matcher.gcj02_to_wgs84(point[0], point[1])[0]
        point[1] = matcher.gcj02_to_wgs84(point[0], point[1])[1]
    route = json.dumps(arr)
    print(route)
    break