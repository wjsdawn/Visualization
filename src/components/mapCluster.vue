<template>
    <div class="Cluster">

    </div>
</template>

<script>
    export default {
        data(){
            return{
                mapCluster:{}
            }
        },
        mounted() {
            this.map = new mapboxgl.Map({
                container:'map',


            })
        },
        methods:{

        },
    }
</script>