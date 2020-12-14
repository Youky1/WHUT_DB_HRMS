<template>
    <div id="totalContainer">
        <div id="contentBox">
            <info-input v-bind:submit="submit"></info-input>
            <button id="commitBtn" @click="commitSignup">提交注册</button>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex';

import InfoInput from'./InfoInput'

export default {
    name:'Signup',
    components:{
        'info-input':InfoInput
    },
    data(){
        return {
            submit:false
        }
    },
    methods:{
        // 提交注册请求
        commitSignup(){
            this.submit = true;
            setTimeout(() => {
                let {naem,sex,phone,email} = this.$store.state.infoInput;
                let id = this.$store.userId;
                let info = { id, name, sex, phone, email }
                this.postData('signup/submit',info)
                .then(res => {
                    if(res.status){ // 注册成功，跳转至主页
                        this.successfulTip('注册成功');
                        this.$router.back();
                    }else{
                        this.failTip('注册失败')
                    }
                })
            }, 0);
        },
    },
    computed:{
        ...mapState(['postData','successfulTip','failTip'])
    }
}
</script>

<style lang="stylus" scoped>
    #totalContainer
        height 75vh
        display flex
        justify-content center
        align-items center
        background-color #E8EAF2
        #contentBox
            height 75vh
            width 35vw
            background-color #fff
            border-left 1px solid #777
            border-right 1px solid #777
            
            #commitBtn
                width 50%
                height 30px
                border-radius 15px
                display block
                margin 50px auto
                background-color #45C8DC
                border none
                color #777
                cursor pointer
                font-size 14px
                outline none
                transition all 0.5s
            #commitBtn:hover
                font-size 18px
                color #fff
</style>>