<template>
    <div class="slider">
        <el-slider v-model="value" range :marks="marks" :max=24 @change="change($event)" :disabled="this.$store.state.map_status==0?false:true">
        </el-slider>
    </div>

</template>

<script>
    import {Loading} from "@element-plus/icons";
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
        components:{
            [Loading.name]:Loading,
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