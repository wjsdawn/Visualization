<template>
    <div class="slider">
        <el-slider v-model="value" range :marks="marks" :max=24 @change="change($event)">

        </el-slider>
    </div>
</template>

<script>
    export default {
        data(){
            return{
                value:[0,8],
                marks:{
                    0:'0点',
                    6:'6点',
                    12:'12点',
                    18:'18点',
                    24:'24点'
                }
            }
        },
        methods:{
            change(event){
                this.$store.commit('ChangeTime', {start:event[0],end:event[1]})
                // console.log(this.$store.state.time)
            }
        },
        mounted() {
            this.$store.commit('ChangeTime', {start:0,end:8})
        }


    }
</script>
<style lang="scss">
    .slider{
    }
</style>