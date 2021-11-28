<template>
    <div class="container">
        <svg id="svg">

        </svg>
    </div>
</template>
<script>
    import *as d3 from 'd3'
    import {AxiosInstance as axios} from "axios";
    export default {
        data(){
            return{

            }
        },
        watch:{
            "$store.state.pieFlag"(){
                this.drawPie()
            }
        },
        mounted() {
            this.axios.post('http://127.0.0.1:5000/pie').then((res=>{}))
        },
        methods:{
            drawPie(){
                let oriData = []
                let i = 0
                for(let key in this.$store.state.timeJson.data){
                    oriData[i] = {'x':key, 'y':this.$store.state.timeJson.data[key]}
                    i++
                }
                console.log(this.$store.state.timeJson.data)
                // const oriData = [
                //     { 'x': '时代', 'y': 1 },
                //     { 'x': '地点', 'y': 2 },
                //     { 'x': '诗词', 'y': 3 },
                //     { 'x': '诗人', 'y': 4 },
                //     { 'x': '图片', 'y': 5 },
                // ];
                const [width, height] = [400, 300];

                let svg = d3.select('#svg')
                    .attr('width', width)
                    .attr('height', height)

                let g = svg.append('g')
                    .attr('transform', 'translate( 20, 20 )')

                //设置饼图的半径
                let radius = Math.min(width, height) * 0.8 / 2

                let arc = d3.arc()
                    .innerRadius(70)
                    // .outerRadius(radius)
                    .cornerRadius(10)

                //饼图与文字相连的曲线起点
                let pointStart = d3.arc()
                    .innerRadius(radius)
                    .outerRadius(radius)
                //饼图与文字相连的曲线终点
                let pointEnd = d3.arc()
                    .innerRadius(radius + 20)
                    .outerRadius(radius + 20)

                let drawData = d3
                    .pie()
                    .value(function(d) {
                        return d.y
                    })
                    .sort(null)
                    .sortValues(null)
                    .startAngle(0)
                    .endAngle(Math.PI * 2)
                    .padAngle(0.05)(oriData)
                // console.log(drawData)

                let colorScale = d3
                    .scaleOrdinal()
                    .domain(d3.range(0, oriData.length))
                    .range(d3.schemeSet1);
                g.append('g')
                    .attr('transform', 'translate( ' + radius + ', ' + radius + ' )')
                    .attr('stroke', 'steelblue')
                    .attr('stroke-width', 1)
                    .selectAll('path')
                    .data(drawData)
                    .enter()
                    .append('path')
                    .attr('fill', function(d) {
                        return colorScale(d.index)
                    })
                    .attr('d', function(d) {
                        d.outerRadius = radius;
                        return arc(d)
                    })
                    .attr('cursor','pointer')
                    .on('mouseover', arcTween(radius + 20, 0))
                    .on('mouseout', arcTween(radius, 150))
                    .transition()
                    .duration(2000)
                    .attrTween('d', function (d) {
                        //初始加载时的过渡效果
                        let fn = d3.interpolate({
                            endAngle: d.startAngle
                        }, d)
                        return function(t) {
                            return arc(fn(t))
                        }
                    })

                function arcTween(outerRadius, delay) {
                    // 设置缓动函数,为鼠标事件使用
                    return function() {
                        d3.select(this)
                            .transition()
                            .delay(delay)
                            .attrTween('d', function(d) {
                                let i = d3.interpolate(d.outerRadius, outerRadius)
                                return function(t) {
                                    d.outerRadius = i(t)
                                    return arc(d)
                                }
                            })
                    }
                }

                //文字层
                let sum = d3.sum(oriData, d => d.y);

                //图例legend
                let legend = g.append('g')
                    .attr('transform', 'translate( ' + radius * 2.5 + ', 0 )')
                    .selectAll('g')
                    .data(drawData)
                    .enter()
                    .append('g')
                    .attr('transform', function(d, i) {
                        return 'translate(0,' + i * 20 + ')'
                    });

                legend
                    .append('rect')
                    .attr('width', 27)
                    .attr('height', 18)
                    .attr('fill', function(d) {
                        return colorScale(d.index)
                    });
                legend
                    .append('text')
                    .text(function(d) {
                        return d.data.x+"-----"+(d.data.y / sum * 100).toFixed(2) + '%'
                    })
                    .style('font-size', 10)
                    .attr('fill', 'white')
                    .attr('y', '1em')
                    .attr('x', '3em')
                    .attr('dy', 3)


                //曲线层
                g.append('g')
                    .attr('transform', 'translate( ' + radius + ', ' + radius + ' )')
                    .selectAll('path')
                    .data(drawData)
                    .enter()
                    .append('path')
                    .attr('d',
                        d3
                            .linkHorizontal()
                            .source(function(d) {
                                return pointStart.centroid(d)
                            })
                            .target(function(d) {
                                return pointEnd.centroid(d)
                            })
                    )
                    .style('stroke', '#999')
                    .style('stroke-width', 1)
                    .attr('fill', 'none')

                //饼图外面的文字
                g.append('g')
                    .attr('transform', 'translate( ' + radius + ', ' + radius + ' )')
                    .selectAll('path')
                    .data(drawData)
                    .enter()
                    .append('text')
                    .text(function(d) {
                        return d.data.x
                    })
                    .attr('x', function(d) {
                        return pointEnd.centroid(d)[0]
                    })
                    .attr('y', function(d) {
                        return pointEnd.centroid(d)[1]
                    })
                    .style('font-size', 10)
                    .attr('fill', 'white')
                    .attr('text-anchor', function(d) {
                        if (d.startAngle > Math.PI) {
                            return 'end'
                        }
                    })
                    .attr('dominant-baseline', function(d) {
                        if (d.index === 4) {
                            return 'hanging'
                        }
                    })


            }
        }
    }
</script>
<style>
    .container{
        padding: 0;
    }
</style>