<template>
    <div class="mapVisualiazation">
        <div id="container"></div>
    </div>

</template>

<script>
    import mapboxgl from 'mapbox-gl'
    import MapboxLanguage  from '@mapbox/mapbox-gl-language'
    export default {
        data(){
            return{
            }
        },
        mounted() {
            mapboxgl.accessToken = 'pk.eyJ1Ijoid2pzMjIyIiwiYSI6ImNrdmdvOHQ2bDJiZmQydnQyZzJwajloam8ifQ.H0JOuWJGAgpplvEraMnhDQ'; //这里请换成自己的token
            var map = new mapboxgl.Map({
                container: 'container', // container id 绑定的组件的id
                style: 'mapbox://styles/mapbox/streets-v11', //地图样式，可以使用官网预定义的样式,也可以自定义
                center: [104.05878,30.50994],
                zoom: 15,     // starting zoom 地图初始的拉伸比例
                pitch: 0,  //地图的角度，不写默认是0，取值是0-60度，一般在3D中使用
                bearing: -17.6, //地图的初始方向，值是北的逆时针度数，默认是0，即是正北
                antialias: false, //抗锯齿，通过false关闭提升性能
            });
            var language = new MapboxLanguage({ defaultLanguage: "zh-Hans" });
            map.addControl(language);
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