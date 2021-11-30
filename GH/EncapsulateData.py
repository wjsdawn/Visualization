import json
import pickle

import Database
import GH.MapMatching as matcher


def encapsulate():
    coll = Database.get_coll()
    data = coll.find()
    # for car in data:
    #     df = pickle.loads(car["route"])
    #     arr_point = df.to_json(orient="values")
    #     arr = json.loads(arr_point)
    #
    #     body = {
    #         'ak': matcher.read_key("../public/user_key"),
    #         'point_list': matcher.create_point_json(arr),
    #         'rectify_option': "need_mapmatch:1|transport_mode:driving|denoise_grade:1|vacuate_grade:1",
    #         'supplement_mode': "driving",
    #         'coord_type_output': "bd09ll"
    #     }
    #
    #     url = "https://api.map.baidu.com/rectify/v1/track?"
    #     res_json = matcher.request_post(url, body)
    #     time_points = matcher.get_matching_time_points(res_json)
    #     with open('./output.txt', 'w', encoding='utf-8') as fp:
    #         for point in time_points:
    #             fp.write(str(point)+'\n')
    #     fp.close()



encapsulate()