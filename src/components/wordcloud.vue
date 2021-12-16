<template>
    <div id="app1">
    词云图
    </div>
</template>

<script>    
import * as echarts from 'echarts';

export default {
    mounted(){
var myChart = echarts3.init(document.getElementById('app1'));
var keywords = [{"name":"成都市双流区","value":2.64},
                {"name":"成都市双流区公黄路","value":4.03},
                {"name":"成都市双流区剑南大道南段辅路","value":24.95},
                {"name":"成都市双流区武汉路西段辅路","value":4.04},]
var option = {
            series: [{
                type: 'wordCloud',
                sizeRange: [15, 80],
                rotationRange: [0, 0],
                rotationStep: 45,
                gridSize: 8,
                shape: 'pentagon',
                width: '100%',
                height: '100%',
                textStyle: {
                    normal: {
                        color: function () {
                            return 'rgb(' + [
                                Math.round(Math.random() * 160),
                                Math.round(Math.random() * 160),
                                Math.round(Math.random() * 160)
                            ].join(',') + ')';
                        }
                    }
                },
                data: keywords
            }]
        };
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function() {
        myChart.resize();
    });
 
}
}
</script>
