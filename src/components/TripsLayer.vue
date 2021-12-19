<template>
    <div id="Trips">
        <el-icon class="is-loading" color="white" size="100px" v-show="this.$store.state.map_status==1">
            <loading />
        </el-icon>
    </div>
</template>
<script>
    import echarts from 'echarts';
    import "echarts-gl"
    import *as d3 from 'd3'
    import {Loading} from "@element-plus/icons";
    export default {
        data(){
            return{
                Tripsdata:[]
            }
        },
        mounted() {
            this.$store.commit("ChangeMapStatue",1)
            this.getSource().then(res=>{
                this.drwaTrips(res)
                this.$store.commit("ChangeMapStatue",0)
            })
        },
        components:{
            [Loading.name]:Loading,
        },
        watch:{
            "$store.state.timeFlag"(){
                this.$store.commit("ChangeMapStatue",1)
                this.getSource().then(res=>{
                    $("#Trips").removeAttr("_echarts_instance_").empty()
                    // d3.selectAll("#Trips>*").remove()
                    this.drwaTrips(res)
                    this.$store.commit("ChangeMapStatue",0)
                })
            },
        },
        methods:{
            async getSource(){
                return new Promise((resolve,reject) =>{
                    this.axios.post('http://127.0.0.1:5000/sendCarsLine', this.$store.state.time).then(res=>{
                        this.Tripsdata = res.data
                        console.log("数据读取成功")
                        resolve(this.Tripsdata)
                        this.axios.post('http://127.0.0.1:5000/Pie').then(r=>{
                            this.$store.commit('ChangeTimeJson',r)
                            this.$store.commit('ChangePieFlag')
                        })
                    });
                })
            },
            drwaTrips(res){
                var chart = echarts.init(document.getElementById('Trips'));
                var carLines = []
                for(let i in res){
                    let temp = []
                    for(let j in res[i]){
                        let temp2 = []
                        for(let k in res[i][j]){
                            temp2.push(res[i][j][k])
                        }
                        temp.push(temp2)
                    }
                    carLines.push(temp)
                }
                var dataLines = carLines.map(function (data,idx) {
                    let hStep = 20 / (data.length - 1);
                    return {
                        coords: data,
                        lineStyle: {
                            color: echarts.color.modifyHSL('#5A94DF', Math.round(hStep * idx))
                        }
                    };
                });
                console.log(dataLines)
                chart.setOption({
                    mapbox3D: {
                        center: [104.040847,30.466655],
                        zoom: 13,
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
                            trailWidth: 2,
                            trailLength: 0.3,
                            // trailColor: [1, 1, 5],
                            trailOpacity: 1,

                            spotIntensity: 3
                        },

                        blendMode: 'lighter',

                        polyline: true,

                        lineStyle: {
                            width: 2,
                            color: 'rgb(60, 150, 80)',
                            opacity:  0.
                        },

                        data: dataLines
                    }]
                });

                window.onresize = chart.resize;

                window.addEventListener('keydown', function () {
                    chart.dispatchAction({
                        type: 'lines3DToggleEffect',
                        seriesIndex: 0
                    });
                });
            },
            drwaTripsTest(){

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
    z-index: 0;
}
.is-loading{
    position: absolute;
}
</style>