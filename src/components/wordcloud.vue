<template>
  <div >
    <el-image :src="srcdata"></el-image>
    <!-- <img :src="data:image/jpg;base64,这里是base64的编码"/> -->
  </div>
</template>
<script>
export default {
  data() {
    return {
      srcdata: "data:image/jpg;base64,",
    };
  },
  mounted() {
      this.axios.post("http://127.0.0.1:5000/worldcolud").then((res)=>{
          this.srcdata = this.srcdata+res.data
      })
  }
};
</script>



