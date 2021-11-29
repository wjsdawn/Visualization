#
# def main():
#   trajectory_data_rootdir = "轨迹数据根路径"
#   network_path = "BJRoadNet/Beijing_Polyline.shp" # 路网shp文件路径
#   bufferDis = 50 # 缓冲距离
#   taix_id = 1 # 出租车辆id
#   prex = "point_taxi_gps_20xx_by_id" # 保存文件的前缀
#
#   # 加载轨迹数据以及基础数据
#   datas = readTrajectory(trajectory_data_rootdir + "taxi_log_20xx_by_id/%s.txt" % (str(taix_id)))
#   network = Network.loadNetwork("Beijing_NetworkLink", "NetworkLink")
#   ArcPy_Util.bindFeatureLayer(network, network_path)
#
#   isStop(datas, network_path, bufferDis) # 判断为静止的时段，就不考虑该轨迹点
#
#   datas = datas[datas["Day"] == 2]
#   datas.reset_index(drop = True)
#
#   # 匹配部分代码
#   candinate_points = match(network, datas, bufferDis)
#
#   # 匹配结果整理，获取轨迹线、点信息
#   print("Start to get the matched info...")
#   route_polylines, route_points = getPolyline_Point_Info(candinate_points, network)
#
#   # 匹配前结果存为shp文件
#   points = [ArcPy_Util.lnglatToXY(coords["LNG"], coords["LAT"], ArcPy_Util.get_spatial_reference(network_path)) for index, coords in datas.iterrows() if not coords["Is_Stop"]]
#   ArcPy_Util.save_points(points, ArcPy_Util.get_spatial_reference(network_path), "Matched_Taxi_Data/%s_%s.shp" % (prex, str(taix_id)))
#
#   # 匹配后结果存为shp文件
#   ArcPy_Util.save_points(route_points, ArcPy_Util.get_spatial_reference(network_path), "Matched_Taxi_Data/Mathched_%s_%s.shp" % (prex, str(taix_id)))
#   ArcPy_Util.save_polylines(route_polylines, "Matched_Taxi_Data/%s_%s.shp" % ("polyline", str(taix_id)))

