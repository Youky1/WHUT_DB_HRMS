<template>
    <div id="totalBox">
        <div id="functionBar">
            <div class="functionTitle">信息查询</div>
            <div class="functionItem" @click="changeShowingComponent('Self')">个人信息</div>
            <div class="functionItem" @click="changeShowingComponent('CompanyWage')">薪资待遇</div>

            <div class="functionTitle">公司业务管理</div>
            <div class="functionItem" @click="changeShowingComponent('ChangeDepartmentInfo')">部门管理</div>
            <div class="functionItem" @click="changeShowingComponent('DepartmentInfo')">职位统计</div>

            <div class="functionTitle">人事管理</div>
            <div class="functionItem" @click="changeShowingComponent('Hire')">员工录用</div>
            <div class="functionItem" @click="changeShowingComponent('Distribution')">岗位分配</div>
            <div class="functionItem" @click="changeShowingComponent('Manage')">岗位调整</div>
        </div>
        <component  :is="currentComponent"></component>
    </div>
</template>

<script>
import Default from './stable/Default'
import Self from './info/Self'
import CompanyWage from './info/CompanyWage'
import ChangeDepartmentInfo from './department/ChangeDepartmentInfo'
import DepartmentInfo from './department/DepartmentInfo'
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
        ChangeDepartmentInfo,
        DepartmentInfo,
        Distribution,
        Hire,
        Manage,
    },
    methods:{
        changeShowingComponent(com){
            this.currentComponent = com;
        }
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
            .functionItem:hover
                background-color #ddd
</style>>