<template>
  <div id="index">
      <dv-full-screen-container class="bg">
          <div class="top">
              <view_1/>
              <view_2/>
              <view_3/>
          </div>
          <div class="middle">
              <view_4/>
              <mapVisualization/>
              <view_5/>
          </div>
          <div class="bottom">
            <div></div>
          </div>
      </dv-full-screen-container>

  </div>
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
      serverResponse:String
    }
  },
  mounted() {
      this.getData()
  },
  methods:{
    getData(){
      this.axios.post('http://127.0.0.1:5000/send_test').then(res=>{
        let message = res.data.msg
        this.serverResponse = message
        console.log(res.data)
      });
    }
  }
}
</script>
<style lang="scss">
  @import '../assets/scss/index.scss';
</style>