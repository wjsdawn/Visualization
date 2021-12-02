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
                        <timeSelect class="title"/>
                        <pie/>
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-60">
                    <div class="xpanel xpanel-l-b">
                        <div class="title"></div>
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
                        <div class="title"></div>
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-30">
                    <div class="xpanel xpanel-r-m">
                        <div class="title"></div>
                    </div>
                </div>
                <div class="xpanel-wrapper xpanel-wrapper-45">
                    <div class="xpanel xpanel-r-b">
                        <div class="title"></div>
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
    export default {
        components:{
            mapVisualization,
            slider,
            pie,
            timeSelect,
            trips,
            TripsLayerBMap
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