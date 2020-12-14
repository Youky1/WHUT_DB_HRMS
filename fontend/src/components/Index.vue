<template>
    <div id="totalBox">
        <div id="functionBar">
            <div class="choiceBox" @click="changeShowingComponent('Self')">个人信息</div>
            <div class="choiceBox" @click="changeShowingComponent('Company')">公司部门介绍</div>
            <div class="choiceBox" v-if="hrIdentity">公司管理</div>
        </div>
        <component  :is="currentComponent"></component>
    </div>
</template>

<script>
import Default from './content/Default'
import Self from './content/Self'
import Company from './content/Company'
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
        Company
    },
    computed:{
        ...mapState(['hrIdentity'])
    },
    methods:{
        changeShowingComponent(com){
            this.currentComponent = com;
        }
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
            align-items center
        .choiceBox
            width 80%
            height 20%
            display flex
            justify-content center
            align-items center
            background-color #fff
            box-shadow 15px 15px 10px 5px #777
            color #F4A460
            font-size 16px
        .choiceBox:hover
            width 82%
            height 22%
            cursor pointer
            background-color #ccc
            font-size 22px
</style>>