<template>
    <div class="view_3">
        提取交通拥堵特征，挖掘交通拥堵成因，并结合可视分析技术给出疏导方案
    </div>
</template>

<script>
    export default {
        data(){

        },

    }
</script>
<style lang="scss">
    .view_3{
        flex: 1;
    }
</style>
import * as echarts from 'echarts';

var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

option = {
  xAxis: {
    type: 'category',
    boundaryGap: false,
//行数据
    data: 
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
//列数据        
      data: 
      type: 'line',
      areaStyle: {}
    }
  ]
};

option && myChart.setOption(option);
