<template>
  <div id="main"></div>
</template>

<script>
import * as echarts from "echarts";
import { Right } from "@element-plus/icons";
export default {
  data() {
    return {
      page: 1,
      name: [],
      speed: [],
      myChart: Object,
      option: {},
    };
  },
  mounted() {
    this.axios
      .post("http://127.0.0.1:5000/routespeed", { 'page': this.page })
      .then((res) => {
        var na = res.data.route_name;
        var sp = res.data.route_speed;
        this.name = JSON.parse(na);
        this.speed = JSON.parse(sp);
        var chartDom = document.getElementById("main");
        this.myChart = echarts.init(chartDom);
        this.option = {
          xAxis: {
            max: "dataMax",
          },
          yAxis: {
            type: "category",
            data: this.name,
            inverse: true,
            animationDuration: 300,
            animationDurationUpdate: 300,
            max: 20,
            label: {
              show: true,
            }, // only the largest 3 bars will be displayed
          },
          series: [
            {
              realtimeSort: true,
              name: "X",
              type: "bar",
              data: this.speed,
              label: {
                show: true,
                position: "right",
                valueAnimation: true,
              },
            },
          ],
          textStyle: {
            color: "rgb(255,255,255)",
          },
          grid: {
            x: 100,
          },
          legend: {
            show: true,
          },
          animationDuration: 0,
          animationDurationUpdate: 3000,
          animationEasing: "linear",
          animationEasingUpdate: "linear",
        };
        this.myChart.setOption(this.option);
      }).then(()=>{
        let _this = this
        setInterval(function(){
          _this.run()
        },3000)
      });
  },
  methods:{
    run() {
      alert('调用')
      this.axios
        .post("http://127.0.0.1:5000/routespeed", {'page':this.page})
        .then((res) => {
          var na = res.data.route_name;
          var sp = res.data.route_speed;
          this.name = JSON.parse(na);
          this.speed = JSON.parse(sp);
          this.myChart.setOption({
            series: [
              {
                type: "bar",
                data: this.speed,
              },
            ],
            yAxis: {
              data: this.name,
            },
          });
        })
        .then(()=>{
           this.page = this.page+1
        });
    }
  },
};
</script>

<style scoped>
#main {
  position: relative;
  display: block;
  top: 0.1rem;
  height: 100%;
  left: 3rem;
}
</style>