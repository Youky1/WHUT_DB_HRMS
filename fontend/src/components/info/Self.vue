<template>
    <div id="outsideBox">
        <div id="name" v-html="name"></div>
        <div id="container">
            <div class="infoItem" v-for="item in infoToShow" v-bind:key="item[1]">
                <strong>{{item[0]}}</strong>
                <p>{{item[1]}}</p>
            </div>
        </div>
        
    </div>
</template>

<script>
import { mapState } from 'vuex'
import { getUserInfo } from '../../util'
export default {
    data(){
        return{
            userInfo:{},
        }
    },
    computed:{
        ...mapState(['userId']),
        name(){
            return `<span class="iconfont iconadmin"></span>${this.userInfo.name}`
        },
        infoToShow(){
            let arr = ['sex','phone','email','department','position','hireDate']
            let obj = ['性别','手机号','邮箱','部门','职位','招聘日期'];
            let result = []
            for(let index in arr){
                result.push([ obj[index],this.userInfo[ arr[index] ] ])
            }
            console.log(result)
            return result
        }
    },
    mounted(){
        getUserInfo(this.userId)
        .then(res => {
            if(res.status){
                this.userInfo = res.data;
            }else{
                console.log('查找个人信息失败')
            }
        })
    }
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