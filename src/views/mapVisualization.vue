<template>

    <div id="container">
        <el-icon class="is-loading" color="white" size="100px" v-show="this.$store.state.map_status==1">
            <loading />
        </el-icon>
    </div>
</template>

<script>
    import { saveAs } from 'file-saver';
    import {Loading} from "@element-plus/icons";
    export default {
        data(){
            return{
                heatSource: {},
                time: {},
                map:{}
            }
        },
        watch:{
            "$store.state.timeFlag"(){
                this.$store.commit("ChangeMapStatue",1)
                this.getHeatSource().then(res=>{
                    this.map.removeLayer("carPoint-heat")
                    this.map.removeSource('carPoint')
                    this.drawHeat(this.map,res)
                    this.$store.commit("ChangeMapStatue",0)
                })
            },
            // "$store.state.time.end"(){
            //     this.$store.commit("ChangeMapStatue",1)
            //     this.getHeatSource().then(res=>{
            //         this.map.removeLayer("carPoint-heat")
            //         this.map.removeSource('carPoint')
            //         this.drawHeat(this.map,res)
            //         this.$store.commit
            
            //     })
            // }
        },
        components:{
            [Loading.name]:Loading,
        },
        mounted() {
            // mapboxgl.accessToken = 'pk.eyJ1Ijoid2pzMjIyIiwiYSI6ImNrdmdvOHQ2bDJiZmQydnQyZzJwajloam8ifQ.H0JOuWJGAgpplvEraMnhDQ'; //这里请换成自己的token
            this.map = new mapboxgl.Map({
                container: 'container', // container id 绑定的组件的id
                style: 'mapbox://styles/mapbox/dark-v10', //地图样式，可以使用官网预定义的样式,也可以自定义
                // style:'mapbox://styles/wjs222/ckxebui5g5qj115oi9zfyhmng',
                center: [104.040847,30.466655],
                zoom: 12,     // starting zoom 地图初始的拉伸比例
                pitch: 0,  //地图的角度，不写默认是0，取值是0-60度，一般在3D中使用
                bearing: 0, //地图的初始方向，值是北的逆时针度数，默认是0，即是正北
                antialias: false, //抗锯齿，通过false关闭提升性能
            });
            // var language = new MapboxLanguage({ defaultLanguage: "zh-Hans" });
            // this.map.addControl(language);
            this.$store.commit("ChangeMapStatue",1)
            this.getHeatSource().then(res=>{
                this.drawHeat(this.map,res)
                this.$store.commit("ChangeMapStatue",0)
            })
        },
        methods:{
            async getHeatSource(){
                return new Promise((resolve,reject) =>{
                    this.axios.post('http://127.0.0.1:5000/send_point', this.$store.state.time).then(res=>{
                        this.heatSource = res.data
                        // this.$store.commit('change', {start:7,end:10})
                        // console.log(this.$store.state.time)
                        console.log("数据读取成功")
                        resolve(this.heatSource)
                        // this.axios.post('http://127.0.0.1:5000/pie').then(r=>{
                        //     this.$store.commit('ChangeTimeJson',r)
                        //     this.$store.commit('ChangePieFlag')
                        // })
                    });
                })

            },
            drawHeat(map,res){
                console.log("开始绘制热力图")
                map.addSource('carPoint',{
                    "type":"geojson",
                    "data":res
                });
                map.addLayer({
                    "id":"carPoint-heat",
                    "type":"heatmap",
                    "source":"carPoint",
                    "maxzoom":20,
                    "paint":{
                        "heatmap-intensity":[
                            "interpolate",
                            ['linear'] ,
                            ["zoom"],
                            14,1,
                            15,3
                        ],
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
                            12, 1,
                            14, 3
                        ],
                        "heatmap-opacity": [
                            "interpolate",
                            ["linear"],
                            ["zoom"],
                            14, 1,
                            15, 0
                        ],
                    }
                }, 'waterway-label')
                console.log("热力图绘制完成")
            },
            getGeoJson(){
            }
        }

    }
</script>

<style lang="scss">
    #container{
        width: 100%;
        height: 100%;
        position: absolute;
        z-index: 1;
        .is-loading{
            position: absolute;
        }
    }
</style>