<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <button @click="getData">get data</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import {AxiosInstance as axios} from "axios";

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
  methods:{
    getData(){
      this.axios.post('http://127.0.0.1:5000/msg').then(res=>{
        let message = res.data.msg
        this.serverResponse = message
        alert('success'+res.status + ',' + res.data + ',' + message)
      });
    }
  }
}
</script>
