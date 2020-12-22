<template>
    <div id="totalBox">
        <div id="chartBox"></div>
    </div>
</template>

<script>
import { getWageInfo, getUserInfo, drawChart } from '../../util'
export default {
    name:'Manage',
    data(){
        return{
            minePosition:null,
            option:null,
        }
    },
    mounted(){
        let self = this;
        (async function(){
            console.log('ID is ',self.$store.state.userId)
            await getUserInfo(self.$store.state.userId).then(res => {
                if(res.status){
                    console.log(res.data)
                    self.minePosition = res.data.Position_name;
                    console.log(self.minePosition)
                }else{
                    console.log('fuck')
                }
            })
            .catch(err => console.log(err))
            await getWageInfo().then( res => {
                if(res.status){
                    let source = [];
                    for(let d of res.data){
                        source.push({position:d.Position_name,salary:d.Salary})
                    }
                    self.option = {
                        title:{
                            text:'各职位薪资情况对比',
                        },
                        dataset: {
                            dimensions: ['position', 'salary'],
                            source,
                        },
                        xAxis: {type: 'category'},
                        yAxis: {},
                        tooltip: {},
                        series: [
                            {
                                type: 'bar',
                                itemStyle:{
                                    normal:{
                                        color:function(param){
                                            console.log(self.minePosition)
                                            console.log(param.data.position)
                                            if(param.data.position == self.minePosition)
                                                return '#FFA500';
                                            else
                                                return '#FF6347'
                                        }
                                    }
                                }
                            },
                        ]
                    };
                }
            })
            await drawChart(self,document.getElementById('chartBox'),self.option)
        })()
        
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