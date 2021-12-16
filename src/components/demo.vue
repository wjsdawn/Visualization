<template>
    <div id="contain">
    
    </div>
</template>

<script>     
import * as echarts from 'echarts';
export default {
    mounted(){
var chartDom = document.getElementById('contain');
var myChart = echarts.init(chartDom);
var option;
var myChart= echarts.init(document.getElementById("contain"));

option = {
  color:['#FFF000'],
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['4-30-16', '4-30-20', '4-30-24', '5-01-4', '5-01-8', '5-01-12', '5-01-16'],
    label:{
        show:true,
    }
  },
  yAxis: {
    type: 'value',
    label:{
        show:true,
    }
  },
  textStyle:{
    color:"#FF0000"
  },
  series: [
    {
      data: [0,1736, 1340, 7664, 9337, 11701, 8238],
      type: 'line',
      smooth:true,
      symbol:'none',
      areaStyle: {} 
    }
  ],
};
myChart.setOption(option);
//监听页面的尺寸变化，动态改变echarts的尺寸
 window.onresize = function () {
     myChart.resize();
 }
myChart.setOption(option);

}
}
</script>
<style lang="scss">
#contain{
    display:block;
    height:100%;    
}
</style>
