<template>
    <div id="totalBox">
        <div id="functionBar">
            <div class="choiceBox" @click="changeShowingComponent('Self')">个人信息</div>
            <div class="choiceBox" @click="changeShowingComponent('Company')">{{departmentOperation}}</div>
            <div class="choiceBox" @click="changeShowingComponent('Manage')" v-if="this.hrIdentity">人事管理</div>
        </div>
        <component  :is="currentComponent" @changeInfo="changeShowingComponent('changeDepartmentInfo')"></component>
    </div>
</template>

<script>
import Default from './content/Default'
import Self from './content/Self'
import Company from './content/Company'
import Manage from './content/Manage'
import changeDepartmentInfo from './content/changeDepartmentInfo'
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
        Company,
        Manage,
        changeDepartmentInfo
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
        #functionBar
            width 30vw
            height 100%
            display flex
            flex-direction column
            justify-content space-around
            align-items left
        .choiceBox
            width 80%
            height 20%
            display flex
            justify-content center
            align-items center
            background-color #fff
            box-shadow 5px 5px 5px 5px #aaa
            color #F4A460
            font-size 16px
        .choiceBox:hover
            width 82%
            height 22%
            cursor pointer
            background-color #ccc
            font-size 22px
</style>>