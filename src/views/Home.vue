<template>
<!--  <div class="home">-->
<!--    <button @click="getData">get data</button>-->
<!--  </div>-->
  <div id="container" style="width: 800px;height: 800px"></div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import {AxiosInstance as axios} from "axios";
import mapboxgl from 'mapbox-gl'
import MapboxLanguage  from '@mapbox/mapbox-gl-language'
// const mapboxgl = require('mapbox-gl');  //引入组件

export default {
  name: 'Home',
  data: function(){
    return{
      serverResponse:String
    }
  },
  components: {
    HelloWorld
  },
  mounted() {
    // var map = new BMap.Map('container')
    // var point = new BMap.Point(104.05878, 30.50994)
    // map.centerAndZoom(point, 15)
    // map.setMapStyleV2({
    //   styleId: '2c1ce2cf7123b0ab6e4694a24c20038a'
    // });
    // map.enableScrollWheelZoom(true)
    mapboxgl.accessToken = 'pk.eyJ1Ijoid2pzMjIyIiwiYSI6ImNrdmdvOHQ2bDJiZmQydnQyZzJwajloam8ifQ.H0JOuWJGAgpplvEraMnhDQ'; //这里请换成自己的token
    var map = new mapboxgl.Map({
      container: 'container', // container id 绑定的组件的id
      style: 'mapbox://styles/mapbox/streets-v11', //地图样式，可以使用官网预定义的样式,也可以自定义
      center: [104.05878,30.50994], // 初始坐标系，这个是南京建邺附近
      zoom: 15,     // starting zoom 地图初始的拉伸比例
      pitch: 0,  //地图的角度，不写默认是0，取值是0-60度，一般在3D中使用
      bearing: -17.6, //地图的初始方向，值是北的逆时针度数，默认是0，即是正北
      antialias: false, //抗锯齿，通过false关闭提升性能
    });
    var language = new MapboxLanguage({ defaultLanguage: "zh-Hans" });
    map.addControl(language);
  },
  methods:{
    getData(){

      // this.axios.post('http://127.0.0.1:5000/msg').then(res=>{
      //   let message = res.data.msg
      //   this.serverResponse = message
      //   // alert('success'+res.status + ',' + res.data + ',' + message)
      // });
    }
  }
}
</script>
