<template>
    <div id="main" @click="()=>{this.$store.state.pauseFlag=this.$store.state.pauseFlag? false:true}"></div>
    <timeslider></timeslider>
</template>

<script>
import * as echarts from "echarts";
import { Right } from "@element-plus/icons";
import timeslider from "./TimeSlider.vue"
export default {
  data() {
    return {
      name: [],
      speed: [],
      myChart: Object,
      option: {},
      interval_id:""
    };
  },
  components: {
      timeslider,
  },
  computed:{
      pauseStateLin(){
        return this.$store.state.pauseFlag
      },
      reflashData(){
        return this.$store.state.reqdata
      }
  },
  watch:{
      pauseStateLin(){
        this.pause()
      },
      reflashData(){
          alert("状态改变")
          this.run()
      }
  },
  mounted() {
    this.axios
      .post("http://127.0.0.1:5000/routespeed", { 'page': this.$store.state.page })
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
            max: 15,
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
        this.interval_id = setInterval(function(){
          _this.run().then(()=>{
          if(_this.$store.state.page > 23)
          {
            _this.$store.state.page = 1
          }
          else{
            _this.$store.state.page = _this.$store.state.page + 1
          }
        });
        },5000)
      });
  },
  methods:{
    async run() {
      this.axios
        .post("http://127.0.0.1:5000/routespeed", {'page':this.$store.state.page})
        .then((res) => {
          var na = res.data.route_name;
          var sp = res.data.route_speed;
          this.name = JSON.parse(na);
          this.speed = JSON.parse(sp);
          this.option.yAxis.data = this.name
          this.option.series[0].data = this.speed
          this.option&&this.myChart.setOption(this.option)
        })
    },
    pause(){
      alert("调用pause")
      if(this.$store.state.pauseFlag)
      {   
        clearInterval(this.interval_id)
      }
      else
      {
        let _this = this
        this.$store.state.reqdata = false
        this.interval_id = setInterval(function(){
            _this.run().then(()=>{
          if(_this.$store.state.page > 23)
          {
            _this.$store.state.page = 1
          }
          else{
            _this.$store.state.page = _this.$store.state.page + 1
          }
        });
        },5000)
      }
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
canvas{
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>