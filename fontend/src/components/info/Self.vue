<template>
    <div id="outsideBox">
        <div id="name"><span class="iconfont iconadmin">{{userInfo.name}}</span></div>
        <div id="container">
            <div class="infoItem" v-for="item in infoToShow" v-bind:key="item[0]">
                <strong>{{item[0]}}</strong>
                <p>{{item[1]}}</p>
            </div>
        </div>
        <div id="listTitle">
            <div class="listItem" style="border:none">工作经历</div>
            <div class="listItem" style="border:none">成绩</div>
        </div>
        <div id="experienceList">
            <div class="experienceItem" v-for="item in userInfo.experience" :key="item.description">
                <p class="listItem">{{item.description}}</p>
                <p class="listItem">{{item.grade}}</p>
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
            userInfo:{name:'youky'},
        }
    },
    computed:{
        ...mapState(['userId']),
        name(){
            return ``
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
        margin-left 10vw
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
            height 55%
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
        #experienceList
            height 100px
            width 45vw
            overflow scroll
            .experienceItem
                display flex
        .listItem
            width 50%
            height 20px
            font-size 12px
            margin  0
            border-top 1px solid #000
            overflow hidden
        #listTitle
            display flex
            width 45vw
            margin-top 20px
</style>