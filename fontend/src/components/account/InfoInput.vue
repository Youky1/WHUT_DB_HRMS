<template>
    <div id="infoInputContainer">
        <div class="infoLine">
            <p>姓名</p>
            <input type="text" class="infoInput" v-model="name">
        </div>
        <div class="infoLine">
            <p>性别</p>
            <select name="sex" class="infoInput" v-model="sex">
                <option value="男">男</option>
                <option value="女">女</option>
            </select>
        </div>
        <div class="infoLine">
            <p>电话</p>
            <input type="text" class="infoInput" v-model="phone">
        </div>
        <div class="infoLine">
            <p>邮箱</p>
            <input type="text" class="infoInput" v-model="email">
        </div>
    </div>
</template>

<script>
export default {
    name:'InfoInput',
    props:['submit'],
    watch:{
        submit(){
            console.log(this.name)
            this.$store.commit('setUserInfo',{
                name:this.name,
                sex:this.sex,
                phone:this.phone,
                email:this.email
            })
        }
    },
    data(){
        return {
            name:'',
            sex:'',
            phone:'',
            email:'',
        }
    }
}
</script>

<style lang="stylus" scoped>
    #infoInputContainer
        margin-top 20px
        display flex
        flex-direction column
        justify-content space-between
        .infoLine
            display flex
            justify-content space-around
            align-items center
            .infoInput
                width 140px
                height 20px

</style>