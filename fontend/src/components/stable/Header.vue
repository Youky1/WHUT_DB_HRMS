<template>
    <Header>
        <img id="logo" src="../../assets/logo.png">
        <div id="title">人力资源管理系统</div>
        <div style="margin-left:60vw">
            <a href="https://github.com/Youky1/WHUT_DB_HRMS" target="_blank">
                Github
                <span class="iconfont icongithub"></span>
            </a>
        </div>
    </Header>
</template>

<script>
export default {

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
</style>