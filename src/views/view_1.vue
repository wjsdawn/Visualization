<template>
  <div class="view_1">
    <el-button @click="download">下载</el-button>
    <div id="map"></div>
  </div>
</template>

<script>
// import mapboxgl from "mapbox-gl";
// import MapboxLanguage from "@mapbox/mapbox-gl-language";
import axios from "axios";
const FileSaver = require("file-saver");
export default {
  data: function () {
    return {
      serverResponse: "resp",
      text: "dsdsd",
      way:[]
    };
  },
  mounted() {
    this.axios.get("http://127.0.0.1:5000/test_route").then((response) => {
      // var id = response.data.id;
      // var beginPos = response.data.begin_pos;
      // var end = response.data.end_pos;
      // var route = response.data.route;
      var route = response.data
      route = eval(route);
      this.way = route;
      console.log(route)
      //加载地图
      mapboxgl.accessToken =
        "pk.eyJ1Ijoid2pzMjIyIiwiYSI6ImNrdmdvOHQ2bDJiZmQydnQyZzJwajloam8ifQ.H0JOuWJGAgpplvEraMnhDQ"; //必须设置accessToken否则地图无法显示

      //创建地图对象，绑定容器
      const map = new mapboxgl.Map({
        container: "map",
        style: "mapbox://styles/mapbox/streets-v11",
        center: [104.05878, 30.50994],
        zoom: 15,
      });
      var language = new MapboxLanguage({ defaultLanguage: "zh-Hans" });
      map.addControl(language);

      //绘制路径
      map.on("load", () => {
        map.addSource("route", {
          type: "geojson",
          data: {
            type: "Feature",
            properties: {},
            geometry: {
              type: "LineString",
              coordinates: route,
            },
          },
        });

        //路径样式
        map.addLayer({
          id: "route",
          type: "line",
          source: "route",
          layout: {
            "line-join": "round",
            "line-cap": "round",
          },
          paint: {
            "line-color": "#888",
            "line-width": 1,
          },
        });
      });
    });
  },
  methods: {
    switchData(array) {
      // var jsondata = JSON.stringify(Object.assign([], array));
      var jsondata = JSON.stringify(array);
      // console.log(jsondata);
      alert(jsondata);
      return jsondata;
    },
    download() {
      var content = this.switchData(this.way);
      var blob = new Blob([content], { type: "textain;charset=utf-8" });
      FileSaver.saveAs(blob, "1.txt");
    },
  },
};
</script>
<style lang="scss">
.view_1 {
  flex: 1;
  width: 100%;
  height: 100%;
}
#map {
  width: 100%;
  height: 95%;
}
</style>