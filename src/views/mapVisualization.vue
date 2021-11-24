<template>
    <div class="mapVisualiazation">
        <div id="container"></div>
    </div>

</template>

<script>
    import mapboxgl from 'mapbox-gl'
    import MapboxLanguage  from '@mapbox/mapbox-gl-language'
    import { saveAs } from 'file-saver';
    export default {
        data(){
            return{
                heatSource: {},
                time:5
            }
        },
        mounted() {
            // this.drawHeat(map)
            this.getHeatSource().then(res=>{
                // mapboxgl.accessToken = 'pk.eyJ1Ijoid2pzMjIyIiwiYSI6ImNrdmdvOHQ2bDJiZmQydnQyZzJwajloam8ifQ.H0JOuWJGAgpplvEraMnhDQ'; //这里请换成自己的token
                // var map = new mapboxgl.Map({
                //     container: 'container', // container id 绑定的组件的id
                //     style: 'mapbox://styles/mapbox/dark-v10', //地图样式，可以使用官网预定义的样式,也可以自定义
                //     center: [104.040847,30.466655],
                //     zoom: 5,     // starting zoom 地图初始的拉伸比例
                //     pitch: 0,  //地图的角度，不写默认是0，取值是0-60度，一般在3D中使用
                //     bearing: 0, //地图的初始方向，值是北的逆时针度数，默认是0，即是正北
                //     antialias: false, //抗锯齿，通过false关闭提升性能
                // });
                // var language = new MapboxLanguage({ defaultLanguage: "zh-Hans" });
                // map.addControl(language);
                // this.drawHeat(map,res)
                // console.log(res)
            })

        },
        methods:{
            async getHeatSource(){
                return new Promise((resolve,reject) =>{
                    this.axios.post('http://127.0.0.1:5000/send_point', {"time":this.time}).then(res=>{
                        this.heatSource = res.data
                        // this.$store.commit('change', {start:7,end:10})
                        console.log(this.$store.state.time)
                        console.log("数据读取成功")
                        resolve(this.heatSource)
                    });
                })

            },
            drawHeat(map,res){
                console.log("开始")
                map.on('load',function () {
                    console.log(res)
                    map.addSource('carPoint',{
                        "type":"geojson",
                        "data":res
                    });
                    map.addLayer({
                        "id":"carPoint-heat",
                        "type":"heatmap",
                        "source":"carPoint",
                        "maxzoom":9,
                        "paint":{
                            "heatmap-color": [
                                "interpolate",
                                ["linear"],
                                ["heatmap-density"],
                                0, "rgba(33,102,172,0)",
                                0.2, "rgb(103,169,207)",
                                0.4, "rgb(209,229,240)",
                                0.6, "rgb(253,219,199)",
                                0.8, "rgb(239,138,98)",
                                1, "rgb(178,24,43)"
                            ],
                            "heatmap-radius": [
                                "interpolate",
                                ["linear"],
                                ["zoom"],
                                0, 13,
                                9, 20
                            ],
                            "heatmap-opacity": [
                                "interpolate",
                                ["linear"],
                                ["zoom"],
                                7, 13,
                                9, 20
                            ],
                        }
                    }, 'waterway-label')
                    map.addLayer({
                        "id": "car-point",
                        "type": "circle",
                        "source": "carPoint",
                        "minzoom": 7,
                        "paint": {
                            "circle-stroke-color": "white",
                            "circle-stroke-width": 1,
                            "circle-opacity": [
                                "interpolate",
                                ["linear"],
                                ["zoom"],
                                7, 13,
                                8, 20
                            ]
                        }
                    }, 'waterway-label');
                });
                console.log("热力图绘制完成")
            },
            getGeoJson(t){
                console.log(t)
            }
        }

    }
</script>

<style lang="scss">
    .mapVisualiazation{
        flex: 1;
        width: 100%;
        height: 100%;
        /*margin: 10px;*/
        #container{
            width: 100%;
            height: 100%;
        }
    }
</style>