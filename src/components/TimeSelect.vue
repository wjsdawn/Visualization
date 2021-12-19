<!--
 * @Author: your name
 * @Date: 2021-12-16 14:38:56
 * @LastEditTime: 2021-12-19 20:48:05
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \Visualization\src\components\TimeSelect.vue
-->
<template>
    <el-time-picker
            id = "timeselect"
            v-model="value"
            range-separator="To"
            start-placeholder="Start time"
            end-placeholder="End time"
            :clearable = "false"
            arrow-control
            is-range
            :disabled="this.$store.state.map_status==0?false:true"
            :disabled-minutes="disabledMinutes"
            :disabled-seconds="disabledSeconds"
            @change="timeSelect"
    >
    </el-time-picker>
</template>
<script>
    export default {
        data(){
            return {
                value:[new Date(2018, 5, 1, 7, 0), new Date(2018, 5, 1, 8, 0)]
            }
        },
        methods:{
            disabledMinutes(){
                let result = []
                for(let i = 0;i < 60;i++){
                    result.push(i)
                }
                return result
            },
            disabledSeconds(){
                let result = []
                for(let i = 0;i < 60;i++){
                    result.push(i)
                }
                return result
            },
            timeSelect(val){
                this.$store.commit('ChangeTime', {start:val[0].getHours(),end:val[1].getHours()})
            }
        }
    }
</script>
<style scoped>
#timeselect{
    position: absolute;
    top: 5rem;
}
</style>