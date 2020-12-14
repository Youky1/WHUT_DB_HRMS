<template>
    <Header>
        <img id="logo" src="../../assets/logo.png">
        <div id="title">人力资源管理系统</div>
        <a href="#" style="margin-left:350px" @click="logout">注销登录</a>
        <a href="#" style="margin-left:25px" @click="toChangePassword">修改密码</a>
        <a href="#" style="margin-left:25px" @click="toChangeInfo">修改个人信息</a>
        <div style="position:absolute;right:10vw;">
            <a href="https://github.com/Youky1/WHUT_DB_HRMS" target="_blank">
                Github
                <span class="iconfont icongithub"></span>
            </a>
        </div>
    </Header>
</template>

<script>
import { mapState } from 'vuex';
export default {
    methods:{
        logout(){
            if(this.hasLogin){
                this.$store.commit('logout');
                this.$router.replace('/')
            }else{
                this.failTip('还未登录哦')
            }
        },
        toChangePassword(){
            if(this.hasLogin){
                this.$router.replace('/change/password')
            }else{
                this.failTip('还未登录哦')
            }
        },
        toChangeInfo(){
            if(this.hasLogin){
                this.$router.replace('/change/userinfo')
            }else{
                this.failTip('还未登录哦')
            }
        },
    },
    computed:{
        ...mapState(['hasLogin','failTip'])
    }
}
</script>

<style lang="stylus" scoped>
    Header
        height 15vh
        background-color #45C8DC
        display flex
        align-items center
        #logo
            height 80%
        #title
            font-size 20px
            color #fff
            margin-left 20px
        a
            text-decoration none
            color #fff
            font-size 14px
        a:hover
            color #000
</style>