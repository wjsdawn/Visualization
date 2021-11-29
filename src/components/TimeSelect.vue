<template>
    <el-time-picker
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
                value:[new Date(2018, 5, 1, 0, 0), new Date(2018, 5, 1, 8, 0)]
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