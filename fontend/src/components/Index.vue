<template>
    <div id="totalBox">
        <div id="functionBar">
            
        </div>
        <component  :is="currentComponent" @changeInfo="changeShowingComponent('changeDepartmentInfo')"></component>
    </div>
</template>

<script>
import Default from './stable/Default'
import Self from './info/Self'
import CompanyWage from './info/CompanyWage'
import ChangeDepartmentInfo from './business/ChangeDepartmentInfo'
import DepartmentInfo from './business/DepartmentInfo'
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
    computed:{
        ...mapState(['hrIdentity','postData',]),
        departmentOperation(){
            return this.hrIdentity ? '部门管理' : '部门信息查询';
        }
    },
    methods:{
        changeShowingComponent(com){
            if(com == 'changeDepartmentInfo' && !this.hrIdentity) 
                return;
            else
                this.currentComponent = com;
        }
    },
    mounted(){
        this.postData('index/get_user_info',{})
        .then(res => {
            if(res.status){
                console.log('get user info')
            }
        })
        this.postData('index/get_company_info',{})
        .then(res => {
            if(res.status){
                console.log('get company info')
            }
        })
    }
}
</script>

<style lang="stylus" scoped>
    #totalBox
        height 75vh
        display flex
        background-color #E8EAF2
       
</style>>