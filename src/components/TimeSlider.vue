<template>
  <el-row>
    <el-col :span="24">
      <div class="grid-content bg-purple" @click="pause">
        <el-time-picker
          is-range
          v-model="value"
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
          console.log(this.$store.state.page)
          return this.$store.state.page
      }
  },
  watch:{
      pageChange(newValue,oldValue){
          var endTime = new Date(2018,5,1,newValue,0,0)
          var startTime = new Date(2018,5,1,newValue-1,0,0)
          this.value[0] = startTime
          this.value[1] = endTime
          console.log(this.value)
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
        console.log(val[1].getHours())
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