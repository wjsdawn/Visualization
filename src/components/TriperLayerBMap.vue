<template>
    <div id="BMapTrips">

    </div>
    <button @click="drwaTrips">123123</button>
</template>
<script>
    import echarts from 'echarts';
    import "echarts-gl"
    export default {
        data(){
            return{
                Tripsdata:[]
            }
        },
        mounted() {
            this.getSource().then(res=>{
                this.drwaTrips(res)
                this.$store.commit("ChangeMapStatue",0)
            })
        },
        watch:{
            // "$store.state.timeFlag"(){
            //     this.$store.commit("ChangeMapStatue",1)
            //     this.getSource().then(res=>{
            //         this.map.removeLayer("carPoint-heat")
            //         this.map.removeSource('carPoint')
            //         this.drawHeat(this.map,res)
            //         this.$store.commit("ChangeMapStatue",0)
            //     })
            // },
        },
        methods:{
            async getSource(){
                return new Promise((resolve,reject) =>{
                    this.axios.post('http://127.0.0.1:5000/sendCarsLine', this.$store.state.time).then(res=>{
                        this.Tripsdata = res.data
                        console.log("数据读取成功")
                        resolve(this.Tripsdata)
                    });
                })

            },
            drwaTrips(res){
                var chart = echarts.init(document.getElementById('Trips'));
                var carLines = []
                var option;
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
                    let hStep = 150 / (data.length - 1);
                    return {
                        coords: data,
                        lineStyle: {
                            color: echarts.color.modifyHSL('#5A94DF', Math.round(hStep * idx))
                        }
                    };
                });
                console.log(dataLines)
                chart.setOption(
                    (option = {
                        bmap: {
                            center: [116.46, 39.92],
                            zoom: 10,
                            roam: true,
                            mapStyle: {
                                styleJson: [
                                    {
                                        featureType: 'water',
                                        elementType: 'all',
                                        stylers: {
                                            color: '#031628'
                                        }
                                    },
                                    {
                                        featureType: 'land',
                                        elementType: 'geometry',
                                        stylers: {
                                            color: '#000102'
                                        }
                                    },
                                    {
                                        featureType: 'highway',
                                        elementType: 'all',
                                        stylers: {
                                            visibility: 'off'
                                        }
                                    },
                                    {
                                        featureType: 'arterial',
                                        elementType: 'geometry.fill',
                                        stylers: {
                                            color: '#000000'
                                        }
                                    },
                                    {
                                        featureType: 'arterial',
                                        elementType: 'geometry.stroke',
                                        stylers: {
                                            color: '#0b3d51'
                                        }
                                    },
                                    {
                                        featureType: 'local',
                                        elementType: 'geometry',
                                        stylers: {
                                            color: '#000000'
                                        }
                                    },
                                    {
                                        featureType: 'railway',
                                        elementType: 'geometry.fill',
                                        stylers: {
                                            color: '#000000'
                                        }
                                    },
                                    {
                                        featureType: 'railway',
                                        elementType: 'geometry.stroke',
                                        stylers: {
                                            color: '#08304b'
                                        }
                                    },
                                    {
                                        featureType: 'subway',
                                        elementType: 'geometry',
                                        stylers: {
                                            lightness: -70
                                        }
                                    },
                                    {
                                        featureType: 'building',
                                        elementType: 'geometry.fill',
                                        stylers: {
                                            color: '#000000'
                                        }
                                    },
                                    {
                                        featureType: 'all',
                                        elementType: 'labels.text.fill',
                                        stylers: {
                                            color: '#857f7f'
                                        }
                                    },
                                    {
                                        featureType: 'all',
                                        elementType: 'labels.text.stroke',
                                        stylers: {
                                            color: '#000000'
                                        }
                                    },
                                    {
                                        featureType: 'building',
                                        elementType: 'geometry',
                                        stylers: {
                                            color: '#022338'
                                        }
                                    },
                                    {
                                        featureType: 'green',
                                        elementType: 'geometry',
                                        stylers: {
                                            color: '#062032'
                                        }
                                    },
                                    {
                                        featureType: 'boundary',
                                        elementType: 'all',
                                        stylers: {
                                            color: '#465b6c'
                                        }
                                    },
                                    {
                                        featureType: 'manmade',
                                        elementType: 'all',
                                        stylers: {
                                            color: '#022338'
                                        }
                                    },
                                    {
                                        featureType: 'label',
                                        elementType: 'all',
                                        stylers: {
                                            visibility: 'off'
                                        }
                                    }
                                ]
                            }
                        },

                        series: [
                            {
                                type: 'lines',
                                coordinateSystem: 'bmap',
                                polyline: true,
                                data: dataLines,
                                silent: true,
                                lineStyle: {
                                    // color: '#c23531',
                                    // color: 'rgb(200, 35, 45)',
                                    opacity: 0.2,
                                    width: 10
                                },
                                progressiveThreshold: 500,
                                progressive: 200
                            },
                            {
                                type: 'lines',
                                coordinateSystem: 'bmap',
                                polyline: true,
                                data: dataLines,
                                lineStyle: {
                                    width: 0
                                },
                                effect: {
                                    constantSpeed: 20,
                                    show: true,
                                    trailLength: 0.1,
                                    symbolSize: 1.5
                                },
                                zlevel: 1
                            }
                        ]
                    })
                );

                window.onresize = chart.resize;

                window.addEventListener('keydown', function () {
                    chart.dispatchAction({
                        type: 'lines3DToggleEffect',
                        seriesIndex: 0
                    });
                });
            },
        }
    }
</script>
<style>
    #BMapTrips{
        width: 100%;
        height: 100%;
        position: absolute;
        z-index: 1;
    }
</style>