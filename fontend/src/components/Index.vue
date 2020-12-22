<template>
    <div id="totalBox">
        <div id="functionBar">
            <div class="functionTitle">信息查询</div>
            <div class="functionItem" @click="changeShowingComponent('Self')">
                <strong class="icon iconfont icongerenxinxi-copy"></strong> 个人信息
            </div>
            <div class="functionItem" @click="changeShowingComponent('CompanyWage')">
                <span class="icon iconfont iconxinzidaiyu"></span> 薪资待遇
            </div>

            <div class="functionTitle">公司业务管理</div>
            <div class="functionItem" @click="changeShowingComponent('DepartmentInfo')">
                <span class="icon iconfont iconbumen"></span> 部门管理
            </div>
            <div class="functionItem" @click="changeShowingComponent('PositionCount')">
                <span class="icon iconfont iconzhiwei"></span> 职位统计
            </div>

            <div class="functionTitle">人事管理</div>
            <div class="functionItem" @click="changeShowingComponent('Hire')">
                <span class="icon iconfont iconluyong"></span> 员工录用
            </div>
            <div class="functionItem" @click="changeShowingComponent('Distribution')">
                <span class="icon iconfont iconfenpei"></span> 岗位分配
            </div>
            <div class="functionItem" @click="changeShowingComponent('Manage')">
                <span class="icon iconfont icontiaozheng"></span> 岗位调整
            </div>
        </div>
        <component  :is="currentComponent"></component>
    </div>
</template>

<script>
import Default from './stable/Default'

import Self from './info/Self'
import CompanyWage from './info/CompanyWage'

import DepartmentInfo from './business/DepartmentInfo'
import PositionCount from'./business/PositionCount'

import Distribution from './hr/Distribution'
import Hire from './hr/Hire'
import Manage from './hr/Manage'

import { mapState } from 'vuex'

export default {
    name:'Index',
    data(){
        return{
            currentComponent:'default'
        }
    },
    components:{
        Default,
        Self,
        CompanyWage,
        DepartmentInfo,
        PositionCount,
        Distribution,
        Hire,
        Manage,
    },
    methods:{
        changeShowingComponent(com){
            this.currentComponent = com;
        },
    },
    mounted(){
        
    }
}
</script>

<style lang="stylus" scoped>
    #totalBox
        height 75vh
        display flex
        background-color #E8EAF2
        #functionBar
            width 15vw
            margin-right 5vw
            display flex
            flex-direction column
            border-right 1px solid #777
            background-color #fff
            .functionTitle
                text-indent 5px
                width 100%
                font-size 14px
                background-color #eee
                margin-bottom 5px
            .functionItem
                cursor pointer
                width 100%
                font-size 12px
                text-indent 15px
                padding-bottom 10px
                display flex
                align-items center
                .icon
                    margin-right 10px
            .functionItem:hover
                background-color #ddd
                
</style>>