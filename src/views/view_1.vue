<template>
  <div class="view_1">
    <span></span>
    <div id="map"></div>
  </div>
</template>

<script>
import mapboxgl from "mapbox-gl";
import MapboxLanguage from "@mapbox/mapbox-gl-language";
import axios from "axios";
export default {
  data: function () {
    return {
      serverResponse: "resp",
      text: "dsdsd",
    };
  },
  mounted() {
    this.axios.get("http://127.0.0.1:5000/send_data").then((response) => {
      var id = response.data.id;
      var beginPos = response.data.begin_pos;
      var end = response.data.end_pos;
      var route = response.data.route;
      route = eval(route);

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
            "line-width": 8,
          },
        });
      });
    });
  },
  methods: {},
};
</script>
<style lang="scss">
.view_1 {
  border-width: 1px;
  border-style: solid;
  flex: 1;
}
#map {
  width: 95%;
  height: 95%;
  margin-left: 2%;
  margin-right: 2%;
  padding-top: 2%;
}
</style>