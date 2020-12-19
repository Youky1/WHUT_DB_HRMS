<template>
    <div id="totalBox">
        <div id="countChart"></div>
    </div>
</template>

<script>
import { drawChart,getWageInfo } from '../../util'
export default {
    mounted(){
        getWageInfo().then(res => {
            if(res.status){
                let source = [];
                for(let d of res.data){
                    source.push({name:d.name,'共需要':d.max,'已安排':d.already})
                }
                console.log(source)
                let option = {
                    legend: {},
                    tooltip: {},
                    dataset: {
                        dimensions: ['name', '共需要', '已安排'],
                        source
                    },
                    xAxis: {type: 'category'},
                    yAxis: {},
                    series: [
                        {type: 'bar'},
                        {type: 'bar'},
                    ]
                };
                drawChart(this,document.getElementById('countChart'),option)
            }
        })
    },
    data(){
        return {}
    }
}
</script>

<style lang="stylus" scoped>
    #totalBox
        height 75vh
        width 80vw
        #countChart
            height 75vh
            width 60vw
            margin-left 10vw
</style>