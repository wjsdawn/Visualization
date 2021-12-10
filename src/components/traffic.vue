<template>
  <div id="main"></div>
</template>

<script>
import * as echarts from 'echarts';
import { Right } from '@element-plus/icons';
export default { 
  mounted() {
    this.axios.post('http://127.0.0.1:5000/routespeed', this.$store.state.time).then(res=>{
    var name = res.data.route_name
    var speed = res.data.route_speed
    name = JSON.parse(name)
    speed = JSON.parse(speed)
    var chartDom = document.getElementById("main");
    var myChart = echarts.init(chartDom);
    var option;

    const data = [];
    for (let i = 0; i < 5; ++i) {
      data.push(Math.round(Math.random() * 200));
    }
    option = {
      xAxis: {
        max: "dataMax",
      },
      yAxis: {
        type: "category",
        data: name,
        inverse: true,
        animationDuration: 300,
        animationDurationUpdate: 300,
        max: 20, 
        label: {
            show: true,
          },// only the largest 3 bars will be displayed
      },
      series: [
        {
          realtimeSort: true,
          name: "X",
          type: "bar",
          data: speed,
          label: {
            show: true,
            position: "right",
            valueAnimation: true,
          },
        },
      ],
      textStyle:{
        color:"rgb(255,255,255)",
      },
      grid:{
        x:200
      },
      legend: {
        show: true,
      },
      animationDuration: 0,
      animationDurationUpdate: 3000,
      animationEasing: "linear",
      animationEasingUpdate: "linear",
    };
    function run() {
      for (var i = 0; i < data.length; ++i) {
        if (Math.random() > 0.9) {
          data[i] += Math.round(Math.random() * 2000);
        } else {
          data[i] += Math.round(Math.random() * 200);
        }
      }
      myChart.setOption({
        series: [
          {
            type: "bar",
            speed,
          },
        ],
      });
    }
    setTimeout(function () {
      run();
    }, 0);
    setInterval(function () {
      run();
    }, 3000);

    myChart.setOption(option);
    })
  },
};
</script>

<style scoped>
#main{
    position: relative;
    display: block;
    top: 0.1rem;
    height: 100%;
    left: 3rem;
}
</style>