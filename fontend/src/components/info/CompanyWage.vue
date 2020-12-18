<template>
    <div id="totalBox">
        
        <div id="chartBox"></div>
    </div>
</template>

<script>
import { getWageInfo,drawChart } from '../../util'
export default {
    name:'Manage',
    mounted(){
        getWageInfo().then( res => {
            if(res.status){
                let source = [];
                for(let d of res.data){
                    source.push({position:d.name,salary:d.salary})
                }
                console.log(source)
                let option = {
                    title:{
                        text:'各职位薪资情况对比',
                    },
                    dataset: {
                        dimensions: ['position', 'salary'],
                        source,
                    },
                    xAxis: {type: 'category'},
                    yAxis: {},
                    series: [
                        {type: 'bar',color:'#CD853F'},
                    ]
                };
                drawChart(this,document.getElementById('chartBox'),option)
            }
        })
    },
}
</script>

<style lang="stylus" scoped>
    #totalBox
        height 75vh
        #chartBox
            height 75vh
            width 60vw
            padding-left 10vw
</style>