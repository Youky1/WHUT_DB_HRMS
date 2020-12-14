<template>
    <div id="outsideBox">
        <h3 id="welcome">欢迎使用本系统</h3>
        <p>您的身份是 <strong v-html="identity"></strong></p>
        <p id="date">{{date}}</p>
    </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
    computed:{
        ...mapState(['hrIdentity']),
        identity(){
            return this.hrIdentity ? `管理员<span class='iconfont iconadmin'></span>`
                                   : `员工<span class='iconfont iconyuangong'></span>`
            
        },
        date(){
            let now = new Date();
            let currentDate = `${now.getFullYear()}/${now.getMonth()}/${now.getDate()},周${now.getDay()}`;
            return `现在是${currentDate}`
        },
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
        justify-content center
        p
            font-size 12px
</style>