<template>
    <div id="hireBox">
        <div id="basicInfo">
            <div class="line">
                <p class="key">姓名</p>
                <input class="value" type="text" v-model="info.name">
            </div>
            <div class="line">
                <p class="key">性别</p>
                <select class="value" v-model="info.sex">
                    <option value="男">男</option>
                    <option value="女">女</option>
                </select>
            </div>
            <div class="line">
                <p class="key">手机号</p>
                <input class="value" type="text" v-model="info.phone">
            </div>
            <div class="line">
                <p class="key">邮箱</p>
                <input class="value" type="text" v-model="info.email">
            </div>
            <div class="line">
                <p class="key">聘用日期</p>
                <input class="value" type="text" v-model="info.hireDate">
            </div>
        </div>
        <div id="experienceInfo">
            <h3>工作经验</h3>
            <div class="line">
                <p class="value" style="border:none">工作经历</p>
                <p class="value" style="border:none">成绩</p>
            </div>
            
            <div style="margin-bottom:20px"  v-for="e in info.experience" :key="e.description">
                <div class="line">
                    <input type="text" class="value">
                    <input type="text" class="value">
                </div>
            </div>
            

            <div id="btnContainer">
                <button @click="add">添加</button>
                <button @click="confirmHire">录用</button>
            </div>
            
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import { hire } from '../../util'
export default {
    name:'Manage',
    data(){
        return{
            info:{
                name:'',
                sex:'',
                phone:'',
                email:'',
                hireDate:'',
                experience:[],
            },
            ex_num:0,
        }
    },
    computed:{
        ...mapState(['failTip','successfulTip'])
    },
    methods:{
        add(){
            if(this.info.experience.length > 4){
                this.failTip('工作记录最多五条')
                return;
            }
            this.info.experience.push({
                description:'',
                grade:''
            })
        },
        confirmHire(){
            hire(this.info)
            .then( res => {
                if(res.status){
                    this.successfulTip('录用成功！')
                    for(let key of Object.keys(this.info)){
                        this.info[key] = '';
                    }
                    this.info.experience = [];
                }
            })
        },
    }
}
</script>

<style lang="stylus" scoped>
    #hireBox
        height 75vh
        width 70vw
        margin-left 5vw
        display flex
        #basicInfo
            height 75vh
            width 30vw
            display flex
            flex-direction column
            align-items center
            justify-content space-around
        .line
            width 30vw
            display flex
            justify-content space-between
            align-items center
            .key
                width 100px
            .value,option
                width 150px
                height 20px
                outline none 
                border 1px solid #ccc
                border-radius 10px
                padding-left 10px
        #experienceInfo
            height 75vh
            width 40vw
            display flex
            flex-direction column
            align-items center
            button 
                cursor pointer
                outline none
                border none
                width 100px
                height 30px
                border-radius 15px
                background-color #fff
                border 1px solid #ccc
                background-color #45C8DC
                color #fff
                border none
            #btnContainer
                position fixed
                bottom 60px
                width 40vw
                display flex
                align-items center
                justify-content space-around
</style>