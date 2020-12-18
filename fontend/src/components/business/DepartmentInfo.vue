<template>
    <div id="outsideBox">
        <div id="infoBox">
            <div class="departmentInfo" v-for="part in departmentInfo" v-bind:key="part.departmentId" @dblclick="changeInfo(part)">
                <div id="line">
                    <p id="name">{{part.name}}</p>
                    <p id="host">主管：<span>{{part.host}}</span></p>
                </div>
                <div id="description">{{part.description}}</div>
            </div>
        </div>
        
        <div id="infoChart" v-if="changeNow">
            <input type="text" v-model="currentDepartment.name">
            <input type="text" v-model="currentDepartment.description">
            <button id="changeBtn">提交修改</button>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            departmentInfo:[{departmentId:'1', name:'管理部门',host:'阿萨德',description:'管理公司日常事务'},
                            {departmentId:'2', name:'管理部门',host:'请问',description:'管理公司日常事务'},
                            {departmentId:'3', name:'管理部门',host:'自行车',description:'管理公司日常事务'},
                            {departmentId:'4', name:'管理部门',host:'艾弗森',description:'管理公司日常事务'},
                        ],
            currentDepartment:{},
            changeNow:false
        }
    },
    methods:{
        changeInfo(part){
            this.currentDepartment = part
            this.changeNow = true
        }
    },
}
</script>

<style lang="stylus" scoped>
    #outsideBox
        height 75vh
        width 80vw
        display flex
        align-items center
        #infoBox
            width 55vw
            height 100%
            display flex
            justify-content space-around
            align-items center
            flex-wrap wrap
            .departmentInfo
                background-color #fff
                display flex
                flex-direction column
                justify-content center
                align-items center
                width 25vw
                border-radius 30px
                cursor pointer
                border 1px solid #777
                #line
                    width 100%
                    display flex
                    align-items center
                    margin 20px 0
                    #name
                        font-size 20px
                        margin 0 0 0 10px
                        color #45C8DC
                    #host
                        margin 0 0 0 40px
                        font-size 16px
                #description
                    font-size 12px
                    color #777
                    padding-bottom 10px
        #infoChart
            height 100%
            width 22vw
            margin-left 2vw
            margin-right 1vw
            background-color #FFFAFA
            display flex
            flex-direction column
            justify-content space-around
            align-items center
            #changeBtn
                background-color #FFE4C4
                border none
                height 40px
                width 100px
                border-radius 20px
                outline none
                cursor pointer
</style>