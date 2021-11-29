<template>
    <div id="Trips">

    </div>
    <button @click="drwaTrips">123123</button>
</template>
<script>
    import echarts from 'echarts';
    import "echarts-gl"
    export default {
        data(){
            return{

            }
        },
        mounted() {
            this.drwaTrips()
        },
        methods:{
            drwaTrips(){

                var chart = echarts.init(document.getElementById('Trips'));
                $.getJSON('lines-bus.json', function (data) {
                    var hStep = 300 / (data.length - 1);
                    var busLines = data.map(function (busLine, idx) {
                        var prevPt;
                        var points = [];
                        for (var i = 0; i < busLine.length; i += 2) {
                            var pt = [busLine[i], busLine[i + 1]];
                            if (i > 0) {
                                pt = [
                                    prevPt[0] + pt[0],
                                    prevPt[1] + pt[1]
                                ];
                            }
                            prevPt = pt;

                            points.push([pt[0] / 1e4, pt[1] / 1e4]);
                        }
                        return {
                            coords: points,
                            lineStyle: {
                                color: echarts.color.modifyHSL('#5A94DF', Math.round(hStep * idx))
                            }
                        };
                    });

                    chart.setOption({
                        mapbox3D: {
                            center: [116.46, 39.92],
                            zoom: 11,
                            pitch: 50,
                            bearing: -10,
                            style: 'mapbox://styles/mapbox/dark-v9',
                            postEffect: {
                                enable: true
                            }
                        },
                        series: [{
                            type: 'lines3D',

                            coordinateSystem: 'mapbox3D',

                            effect: {
                                show: true,
                                constantSpeed: 10,
                                trailWidth: 1,
                                trailLength: 0.3,
                                // trailColor: [1, 1, 5],
                                trailOpacity: 1,

                                spotIntensity: 3
                            },

                            blendMode: 'lighter',

                            polyline: true,

                            lineStyle: {
                                width: 1,
                                color: 'rgb(60, 150, 80)',
                                opacity: 0.
                            },

                            data: busLines
                        }]
                    });

                    window.onresize = chart.resize;

                    window.addEventListener('keydown', function () {
                        chart.dispatchAction({
                            type: 'lines3DToggleEffect',
                            seriesIndex: 0
                        });
                    });
                });
            },
        }
    }
</script>
<style>
#Trips{
    width: 100%;
    height: 100%;
    position: absolute;
    z-index: 1;
}
</style>