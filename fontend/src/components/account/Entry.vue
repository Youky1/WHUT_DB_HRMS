<template>
    <div id="totalContainer">
        <div id="contentBox">
            <div id="functionBar">
                <button class="functionBtn" 
                        @click="handleStatusChange(1)" 
                        id="loginBtn"
                >登录</button>
                <button class="functionBtn" 
                        @click="handleStatusChange(0)" 
                        id="signupBtn"
                >注册</button>
            </div>
            <hr>
            <div id="infoInputContainer">
                <input class="infoInputBox" 
                       type="text" 
                       placeholder="请输入用户ID"
                       v-model="user_id"
                >
                <input class="infoInputBox" 
                       type="password" 
                       placeholder="请输入密码"
                       v-model="user_password"
                >
            </div>
            <button id="operationBtn" @click="handleOperation">{{operationNow}}</button>
            <div id="findBackPassword">
                <a href="#">忘记密码？点击找回</a>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex';
export default {
    name:'Entry',
    methods:{
        handleStatusChange(isLogin){
            this.isLogin = isLogin;
            this.user_id = '';
            this.user_password = '';
        },
        handleOperation(){
            if(this.isLogin){// 登录
                let user_info = {
                    id:this.user_id,
                    password:this.user_password
                }
                this.postData('login',JSON.stringify(user_info))
                .then(res => {
                    if(res.status){
                        // 存储登录信息
                        this.$store.commit('login',user_info)

                        // 跳转页面
                        this.successfulTip('登录成功！')
                        this.$router.replace('index')
                    }else{
                        // ID/密码错误，登录出错
                        this.failTip('ID或密码错误，登录失败！')
                        this.user_id = '';
                        this.user_password = '';
                    }
                })
            }else{// 注册
                this.postData('signup/test',JSON.stringify({id:this.user_id}))
                .then(res => {
                    if(res.status){
                        // 存储当前要进行注册的ID
                        this.$store.commit('goSignup',{id:this.user_id})
                        // 跳转至信息填写页面
                        this.$router.replace('signup')
                    }else{
                        this.failTip('该ID未经HR授权，无法注册！')
                        this.user_id = '';
                        this.user_password = '';
                    }
                })
            }
        },
        
        ...mapMutations(['goSignup'])
    },
    data(){
        return{
            isLogin:true,
            user_id:'',
            user_password:'',
            
        }
    },
    computed:{
        operationNow(){
            return this.isLogin ? '登录' : '注册'
        },
        ...mapState(['postData','successfulTip','failTip'])
    },
}
</script>

<style lang="stylus" scoped>
    #totalContainer
        height 75vh
        display flex
        justify-content center
        align-items center
        background-color #E8EAF2
        button
            background-color #45C8DC
            border none
            color #fff
            cursor pointer
            font-size 14px
            transition all 0.1s
            outline none
        #contentBox
            height 50vh
            width 35vw
            background-color #fff
            border 1px solid #777 
            #functionBar
                height 20%
                display flex
                justify-content space-around
                align-items center
                .functionBtn
                    height 60%
                    width 40%
                    border-radius 5px
                .functionBtn:hover
                    font-size 16px
                    background-color #45C8aa
            #infoInputContainer
                height 45%
                display flex
                flex-direction column
                align-items center
                .infoInputBox
                    width 50%
                    margin-top 5%
                    padding-left 10px
                    border-radius 10px
                    border 1px solid #777
                    outline none
            #operationBtn
                width 50%
                height 30px
                border-radius 15px
                display block
                margin 0 auto
            #findBackPassword
                width 60%
                font-size 10px
                margin 20px auto
                display flex
                justify-content center

</style>>