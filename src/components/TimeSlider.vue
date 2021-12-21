<!--
 * @Author: your name
 * @Date: 2021-12-17 15:11:35
 * @LastEditTime: 2021-12-21 17:45:27
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \Visualization\src\components\TimeSlider.vue
-->
<template>
  <el-row>
    <el-col :span="24">
      <div class="grid-content bg-purple" @click="pause">
        <el-time-picker
          is-range
          v-model="value"
          size = "mini"
          range-separator="to"
          start-placeholder="开始时间"
          end-placeholder="结束时间"
          placeholder="选择时间范围"
          :disabled="false"
          :disabled-seconds="disable_time"
          :disabled-minutes="disable_time"
          @change="timeSelect"
          @focus="pauseSate"
        >
        </el-time-picker>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import timeselect from "./TimeSelect.vue";
export default {
  data() {
    return {
      value: [new Date(2018, 5, 1, 0, 0, 0), new Date(2018, 5, 1, 1,0 , 0)],
    };
  },
  components: {
    timeselect,
  },
  computed:{
      pageChange(){
          return this.$store.state.page
      }
  },
  watch:{
      pageChange(newValue,oldValue){
          var endTime = new Date(2018,5,1,newValue,0,0)
          var startTime = new Date(2018,5,1,newValue-1,0,0)
          this.value[0] = startTime
          this.value[1] = endTime
      }
  },
  mounted() {

  },
  methods: {
    disable_time(){
      let result = [];
      for (let i = 0; i < 60; i++) {
        result.push(i);
      }
      return result;
    },
    timeSelect(val){
        this.$store.state.page = val[1].getHours()
        this.$store.state.reqdata = val[1].getHours()
    },
    pauseSate(){
        this.$store.state.pauseFlag = true
    }
  },
};
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}
.el-col {
  margin-bottom: 20px;
  border-radius: 4px;
  padding-left: 5rem;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
}
</style>