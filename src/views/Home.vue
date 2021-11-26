<!--
 * @Author: your name
 * @Date: 2021-11-25 15:10:22
 * @LastEditTime: 2021-11-25 15:12:54
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \Visualization\src\views\Home.vue
-->
<template>
    <el-container id="index">
        <el-header class="top">Header</el-header>
        <el-container>
            <el-aside width="200px" class="aside">Aside</el-aside>
            <el-container>
                <!-- <el-main><view1/></el-main> -->
                <el-main class="main">
                    <mapVisualization/>
                </el-main>
                <el-footer class="bottom">
                    <slider/>
                </el-footer>
            </el-container>
        </el-container>
    </el-container>
</template>

<script>
import {AxiosInstance as axios} from "axios";
import mapboxgl from 'mapbox-gl'
import MapboxLanguage  from '@mapbox/mapbox-gl-language'
import mapVisualization from './mapVisualization.vue'
import view1 from "./view_1.vue";
import view_2 from "./view_2";
import view_3 from "./view_3";
import view_4 from "./view_4";
import slider from "./slider";
export default {
  components:{
      mapVisualization,
      view1,
      view_2,
      view_3,
      view_4,
      slider
  },
  data(){
    return{
      heatSource:{},
      serverResponse:String
    }
  },
  mounted() {
      //this.getData()
      // this.getData()
      // this.getData1()
  },
  methods:{
    getData(){
      this.axios.post('http://127.0.0.1:5000/send_test').then(res=>{
          this.heatSource['type'] = "FeatureCollection"
          this.heatSource['features'] = res.data
          console.log(res.data)
      });
    },
      getData1(){
          this.axios.post('http://127.0.0.1:5000/msg').then(res=>{
              this.heatSource['type'] = "FeatureCollection"
              this.heatSource['features'] = res.data
              // console.log(res.data)
              console.log(this.heatSource)
          });
      }
  }
}
</script>
<style lang="scss">
  @import '../assets/scss/index.scss';
</style>