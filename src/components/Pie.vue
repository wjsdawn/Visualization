<template>
  <div id="hotmap">
  </div>
</template>
<script>
import * as echarts from "echarts";
import { AxiosInstance as axios } from "axios";
export default {
  data() {},
  mounted() {
    var chartDom = document.getElementById("hotmap");
    var myChart = echarts.init(chartDom);
    var option;

    function getVirtulData(year) {
      year = year || "2017";
      var date = +echarts.number.parseDate(year + "-01-01");
      var end = +echarts.number.parseDate(+year + 1 + "-01-01");
      var dayTime = 3600 * 24 * 1000;
      var data = [];
      for (var time = date; time < end; time += dayTime) {
        data.push([
          echarts.format.formatTime("yyyy-MM-dd", time),
          Math.floor(Math.random() * 10000),
        ]);
      }
      return data;
    }
    option = {
      title: {
        top: 30,
        left: "center",
        text: "Daily Step Count",
      },
      tooltip: {},
      visualMap: {
        min: 0,
        max: 10000,
        type: "piecewise",
        orient: "horizontal",
        left: "center",
        top: 65,
      },
      calendar: {
        top: 120,
        left: 30,
        right: 30,
        cellSize: ["auto", 13],
        range: "2016",
        itemStyle: {
          borderWidth: 0.5,
        },
        yearLabel: { show: false },
      },
      series: {
        type: "heatmap",
        coordinateSystem: "calendar",
        data: getVirtulData("2016"),
      },
    };

    option && myChart.setOption(option);
  },
  methods: {
    circleColor(d) {
      if (d.sex === "M") {
        return "blue";
      } else {
        return "pink";
      }
    },
    linkColor(d) {
      if (d.type === "A") {
        return "green";
      } else {
        return "red";
      }
    },
  },
};
</script>
<style scoped>
#hotmap{
  display: block;
  height: 100%;
}
</style>
