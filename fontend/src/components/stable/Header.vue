<template>
    <Header>
        <img id="logo" src="../../assets/logo.png">
        <div id="title">人力资源管理系统</div>
        <a href="#" style="margin-left:350px">注销登录</a>
        <a href="#" style="margin-left:25px">修改密码</a>
        <a href="#" style="margin-left:25px">修改个人信息</a>
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