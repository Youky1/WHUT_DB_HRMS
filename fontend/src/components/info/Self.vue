<template>
    <div id="outsideBox">
        <div id="name" v-html="name"></div>
        <div id="container">
            <div class="infoItem" v-for="item in infoToShow" v-bind:key="item[1].手机号">
                <strong>{{item[0]}}</strong>
                <p>{{item[1]}}</p>
            </div>
        </div>
        
    </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
    data(){
        return{
        }
    },
    computed:{
        ...mapState(['userInfo','hrIdentity']),
        name(){
            return `<span class="iconfont ${this.hrIdentity ? 'iconadmin': 'iconyuangong'}"></span>${this.userInfo.name}`
        },
        infoToShow(){
            let arr = ['sex','phone','email','department','position','hireDate','workExperience','achievement']
            let obj = ['性别','手机号','邮箱','部门','职位','招聘日期','工作经验','评分'];
            let result = []
            for(let index in arr){
                result.push([ obj[index],this.userInfo[ arr[index] ] ])
            }
            return result
        }
    },
}
</script>

<style lang="stylus" scoped>
    #outsideBox
        height 75vh
        width 40vw
        margin-left 15vw
        display flex
        flex-direction column
        align-items center
        font-size 16px
        #name
            height 10%
            width 40%
            display flex
            justify-content center
            align-items center
            font-size 20px
        #container
            height 80%
            width 50vw
            display flex
            flex-direction column
            justify-content space-around
            align-items center
            flex-wrap: wrap;
        .infoItem
            cursor pointer
            width 40%
            height 40px
            background-color #87CEFA
            margin-top 20px
            display flex
            justify-content space-between
            align-items center
            padding-left 15px
            padding-right 15px
            border-radius 10px
            box-shadow 5px 5px 5px 5px #aaa
        .infoItem:hover
            border 2px solid #ccc
</style>>