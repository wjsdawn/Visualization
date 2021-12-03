import json
import pickle
import time
import pandas
import Database
import GH.MapMatching as matcher

timer = 10229
err_count = 0
key_pos = 0


def encapsulate_daidu():
    global timer
    global err_count
    global key_pos
    coll = Database.get_coll()
    data = coll.find()
    count = coll.count_documents(filter={})
    ak = "iDU5Gn9U217Lf8O5FcyRZMtOFml2RWvU"
    while timer <= count:
        print(str(timer) + ":" + data[timer]["name"]+"----"+ak)
        df = pickle.loads(data[timer]["route"])
        arr_point = df.to_json(orient="values")
        arr = json.loads(arr_point)
        body = {
            'ak': ak,
            'point_list': matcher.create_point_json(arr),
            'rectify_option': "need_mapmatch:1|transport_mode:driving|denoise_grade:1|vacuate_grade:1",
            'supplement_mode': "driving",
            'coord_type_output': "gcj02"
        }

        url = "https://api.map.baidu.com/rectify/v1/track?"
        res_json = matcher.request_post(url, body)
        try:
            time_points = matcher.get_matching_time_points(res_json)
            detail_points = matcher.get_car_msg(res_json)
            with open('./detail.txt','a', encoding='utf-8') as dp:
                for point in detail_points:
                    line = data[timer]["name"] + " " + str(point[0]) + " " + str(point[1]) + " " + str(point[2]) + " " + str(point[3]) + " " + str(point[4]) + '\n'
                    dp.write(line)
            with open('./output.txt', 'a', encoding='utf-8') as fp:
                for point in time_points:
                    line = data[timer]["name"]+" "+str(point[0])+" "+str(point[1])+" "+str(point[2])+'\n'
                    fp.write(line)
            time.sleep(1)
            fp.close()
            dp.close()
            timer = timer+1
        except TypeError:
            time.sleep(1)
            continue
        except KeyError:
            time.sleep(1)
            continue


encapsulate_daidu()
# pd = pandas.read_csv("./output.txt", delimiter=" ")
# group = pd.groupby('id')
# for key, value in group:
#
#     data = value.loc[:, ['lon', 'lat']].to_json(orient="values")
#     arr = json.loads(data)
#     print(arr)
#     for point in arr:
#         point[0] = matcher.gcj02_to_wgs84(point[0], point[1])[0]
#         point[1] = matcher.gcj02_to_wgs84(point[0], point[1])[1]
#     route = json.dumps(arr)
#     print(route)
#     break