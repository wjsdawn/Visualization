<template>
    <el-container id="index">
        <el-header>Header</el-header>
        <el-container>
            <el-aside width="200px">Aside</el-aside>
            <el-container>
                <el-main>
                    <mapVisualization/>
<!--                    <view_2/>-->
                </el-main>
                <el-footer>Footer</el-footer>
            </el-container>
        </el-container>
    </el-container>
</template>

<script>
import {AxiosInstance as axios} from "axios";
import mapboxgl from 'mapbox-gl'
import MapboxLanguage  from '@mapbox/mapbox-gl-language'
import mapVisualization from './mapVisualization.vue'
import view_1 from "./view_1";
import view_2 from "./view_2";
import view_3 from "./view_3";
import view_4 from "./view_4";
import view_5 from "./view_5";
export default {
  components:{
      mapVisualization,
      view_1,
      view_2,
      view_3,
      view_4,
      view_5
  },
  data(){
    return{
      heatSource:{},
      serverResponse:String
    }
  },
  mounted() {
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