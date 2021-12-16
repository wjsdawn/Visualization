<template>
    <div id="main"></div>
    <el-slider class="jam-slider" 
    v-model="page"
    :step="1"
    show-input
    max="48"
    input-size="mini"
    format-tooltip="show_time(page)"></el-slider>
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
            show: false,
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
        },5000)
      });
  },
  methods:{
    run() {
      this.axios
        .post("http://127.0.0.1:5000/routespeed", {'page':this.page})
        .then((res) => {
          var na = res.data.route_name;
          var sp = res.data.route_speed;
          this.name = JSON.parse(na);
          this.speed = JSON.parse(sp);
          this.option.yAxis.data = this.name
          this.option.series[0].data = this.speed
          this.option&&this.myChart.setOption(this.option)
        })
        .then(()=>{
          if(this.page > 47)
          {
            this.page = 1
          }
          else{
            this.page = this.page+1
          }
        });
    },
    show_time(page){
        var time = new Date(2018,5,1,0,0);
        
    }
  },
};
</script>

<style scoped>

#main {
  position: relative;
  display: block;
  top: 1rem;
  height: 90%;
  text-align: center;
  line-height: 100%;
}
.jam-slider{
  position: relative;
  width: 90%;
  top:-2rem;
  left: 2rem;
}
canvas{
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>