<!--
 * @Author: your name
 * @Date: 2021-12-16 14:38:56
 * @LastEditTime: 2021-12-16 19:46:29
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
    <div class="wrapper">
        <div class="content">
            <div class="col col-l">
                <div class="xpanel-wrapper xpanel-wrapper-40">
                    <div class="xpanel xpanel-l-t">
                        
                        <pie/>
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-60">
                    <div class="xpanel xpanel-l-b">
                        <traffic></traffic>
                    </div>
                </div>
            </div>
            <div class="col col-c">
                <div class="xpanel-wrapper xpanel-wrapper-75" style="opacity: 100%">
                    11
                    <div class="xpanel no-bg" style="z-index: -1">
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-25" style="z-index: 2">
                    <div class="xpanel xpanel-c-b">
                        <div class="title title-long"></div>
                    </div>
                </div>
            </div>
            <div class="col col-r">
                <div class="xpanel-wrapper xpanel-wrapper-25">
                    <div class="xpanel xpanel-r-t">
                        <timeSelect class="title"/>
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-30">
                    <div class="xpanel xpanel-r-m">
                        <wordcloud/>
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-45">
                    <div class="xpanel xpanel-r-b">
                       <demo/>
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