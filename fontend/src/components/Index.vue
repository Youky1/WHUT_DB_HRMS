<template>
    <div id="totalBox">
        <div id="functionBar">
            <div class="functionTitle">信息查询</div>
            <div class="functionItem" @click="changeShowingComponent('Self')">个人信息</div>
            <div class="functionItem" @click="changeShowingComponent('CompanyWage')">公司薪资待遇</div>

            <div class="functionTitle">公司业务管理</div>
            <div class="functionItem" @click="changeShowingComponent('ChangeDepartmentInfo')">部门信息管理</div>
            <div class="functionItem" @click="changeShowingComponent('DepartmentInfo')">员工职位统计</div>

            <div class="functionTitle">人事管理</div>
            <div class="functionItem" @click="changeShowingComponent('Distribution')">员工录用</div>
            <div class="functionItem" @click="changeShowingComponent('Hire')">岗位分配</div>
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
            width 20vw
            display flex
            flex-direction column
            .functionTitle
                width 100%
                height 40px
                font-size 16px
            .functionItem
                width 100%
                height 30px
                font-size 12px
</style>>