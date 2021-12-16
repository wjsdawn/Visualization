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

option = {
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
    color:"rgb(255,0,0)"
  },
  series: [
    {
      data: [0,1736, 1340, 7664, 9337, 11701, 8238],
      type: 'line',
      areaStyle: {}
    }
  ]
};

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
