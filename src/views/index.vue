<!--
 * @Author: your name
 * @Date: 2021-12-16 22:32:20
<<<<<<< HEAD
 * @LastEditTime: 2021-12-19 22:05:52
=======
 * @LastEditTime: 2021-12-19 20:56:43
>>>>>>> ff012e2678abfdd3c2f34145e1d2c88c848f2f34
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \Visualization\src\views\index.vue
-->
<template>
<!--    <mapVisualization/>-->
    <trips/>
<!--    <TripsLayerBMap/>-->
    <div class="header">
        <h1 class="header-title">交通</h1>
    </div>
    <div style="text-align: center">
        <timeSelect class="title" style="z-index: 1;marigin-left:50%" />
    </div>

    <div class="wrapper">
        <div class="content">
            <div class="col col-l">
                <!-- <div class="xpanel-wrapper xpanel-wrapper-40">
                    <div class="xpanel xpanel-l-t">  
                        <traffic></traffic>
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-60">
                    <div class="xpanel xpanel-l-b"> 
                        <pie/>
                    </div>
                </div> -->
                <pie/>
            </div>
            <div class="col col-c">
                <div class="xpanel-wrapper xpanel-wrapper-75" style="opacity: 100%">
                    <div class="xpanel no-bg" style="z-index: 5">
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-25" style="z-index: 2">
                    <div class="xpanel xpanel-c-b" style="">
<!--                        <timeSelect class="title" style="margin-top:20%;z-index: 1;" />-->
                    </div>
                </div>
            </div>
            <div class="col col-r">
                <div class="xpanel-wrapper xpanel-wrapper-25">
                    <div class="xpanel xpanel-r-t">
                       <wordcloud/>
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-30">
                    <div class="xpanel xpanel-r-m">  
                        <demo/>      
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-45">
                    <div class="xpanel xpanel-r-b">
                       <traffic></traffic>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</template>
<script>
    import mapVisualization from "./mapVisualization";
    import TripsLayerBMap from "../components/TriperLayerBMap";
    import slider from "./slider";
    import pie from "../components/Pie"
    import timeSelect from "../components/TimeSelect"
    import trips from "../components/TripsLayer"
    import traffic from "../components/traffic.vue"
    import demo from "../components/demo.vue"
    import wordcloud from "../components/wordcloud.vue"
    export default {
        components:{
            mapVisualization,
            slider,
            pie,
            timeSelect,
            trips,
            TripsLayerBMap,
            traffic,
            demo,
            wordcloud
        },
        data(){
          return{

          }
        },
    }
</script>
<style>
    @import '../assets/css/app.css';
</style>