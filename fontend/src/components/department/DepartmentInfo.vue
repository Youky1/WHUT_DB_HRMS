<template>
    <div id="outsideBox">
        <div class="departmentInfo" v-for="part in departmentInfo" v-bind:key="part.departmentId" @click="goManage(part)">
            <div id="line">
                <p id="name">{{part.name}}</p>
                <p id="host">主管：<span>{{part.host}}</span></p>
            </div>
            <div id="description">{{part.description}}</div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            departmentInfo:[{departmentId:'1', name:'管理部门',host:'阿萨德',description:'管理公司日常事务'},
                            {departmentId:'2', name:'管理部门',host:'请问',description:'管理公司日常事务'},
                            {departmentId:'3', name:'管理部门',host:'自行车',description:'管理公司日常事务'},
                            {departmentId:'4', name:'管理部门',host:'艾弗森',description:'管理公司日常事务'},
                        ],
        }
    },
    methods:{
        goManage(part){
            this.$emit('changeInfo')
        }
    }
}
</script>

<style lang="stylus" scoped>
    #outsideBox
        height 75vh
        width 60vw
        margin-left 15vw
        display flex
        justify-content space-around
        align-items center
        flex-wrap wrap
        .departmentInfo
            background-color #fff
            display flex
            flex-direction column
            justify-content center
            align-items center
            width 45%
            border-radius 30px
            cursor pointer
            border 1px solid #777
            #line
                width 100%
                display flex
                align-items center
                margin 20px 0
                #name
                    font-size 20px
                    margin 0 0 0 10px
                    color #45C8DC
                #host
                    margin 0 0 0 40px
                    font-size 16px
            #description
                font-size 12px
                color #777
                padding-bottom 10px
</style>