<template>
  <div id="index">
      <dv-full-screen-container class="bg">
             <mapVisualization/>
      </dv-full-screen-container>

  </div>
</template>

<script>
import {AxiosInstance as axios} from "axios";
import mapboxgl from 'mapbox-gl'
import MapboxLanguage  from '@mapbox/mapbox-gl-language'
import mapVisualization from './mapVisualization.vue'

export default {
  components:{
    mapVisualization,
  },
  data(){
    return{
      serverResponse:String
    }
  },
  mounted() {
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
<style lang="scss">
  @import '../assets/scss/index.scss';
</style>