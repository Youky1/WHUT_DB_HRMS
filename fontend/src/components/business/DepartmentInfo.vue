<template>
    <div id="outsideBox">
        <div id="infoBox">
            <div class="departmentInfo" v-for="part in departmentInfo" v-bind:key="part.Department_id" @dblclick="changeInfo(part)">
                <div id="line">
                    <p id="name">{{part.Department_name}}</p>
                    <p id="host">主管：<span>{{part.Manager}}</span></p>
                </div>
                <div id="description">{{part.Affairs}}</div>
            </div>
        </div>
        
        <div id="infoChart" v-if="changeNow">
            <div class="part">
                <p>部门名称</p>
                <input type="text" v-model="currentDepartment.Department_name">
            </div>
            <div class="part">
                <p>部门主管</p>
                <select id="managerContainer" v-model="currentDepartment.Manager">
                    <option v-for="staff in staffOfCurrentDepartment" :key="staff.id" :value="staff.Employee_id">{{staff.Employee_id}}</option>
                </select>
            </div>
            <div class="part">
                <p>部门事务</p>
                <input type="text" v-model="currentDepartment.Affairs">
            </div>
            <div class="part">
                <button class="hideBtn" @click="submit">修改</button>
                <button class="hideBtn" @click="cancel">取消</button>
            </div>
            
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import { getDepartmentInfo, getAllStaffInfo, getStaffByDepartment, changeDepartmentInfo } from '../../util'
export default {
    data(){
        return{
            departmentInfo:[],
            currentDepartment:{},
            changeNow:false,
            staffOfCurrentDepartment:[],
        }
    },
    methods:{
        changeInfo(part){
            console.log(part)
            this.currentDepartment = JSON.parse(JSON.stringify(part));
            this.changeNow = true;
            getStaffByDepartment({department_id:part.Department_id}).then( res => {
                if(res.status){
                    this.staffOfCurrentDepartment = res.data;
                }
            })
        },
        submit(){
            console.log(this.currentDepartment.Manager);
            changeDepartmentInfo({
                Department_id:this.currentDepartment.Department_id,
                New_Department_name:this.currentDepartment.Department_name,
                New_Manager_id:this.currentDepartment.Manager,
                New_Affairs:this.currentDepartment.Affairs,
            }).then(res => {
                if(res.status){
                    this.successfulTip('部门信息修改成功')
                    this.cancel();
                }else{
                    this.failTip('部门信息修改失败')
                }
            })
        },
        cancel(){
            this.currentDepartment = {};
            this.changeNow = false;
            this.staffOfCurrentDepartment = [];
        }
    },
    mounted(){
        getDepartmentInfo().then(res => {
            if(res.status){
                this.departmentInfo = res.data;
            }
        })
    },
    computed:{
        ...mapState(['successfulTip', 'failTip'])
    }
}
</script>

<style lang="stylus" scoped>
    #outsideBox
        height 75vh
        width 80vw
        display flex
        align-items center
        #infoBox
            width 65vw
            height 100%
            margin-left 10vw
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
                width 25vw
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
        #infoChart
            height 70vh
            width 40vw
            background-color #FFFAFA
            position fixed
            left 40vw
            display flex
            flex-direction column
            justify-content space-around
            align-items center
            .hideBtn
                background-color #FFE4C4
                border none
                height 40px
                width 100px
                border-radius 20px
                outline none
                cursor pointer
            #managerContainer
                width 15vw
            .part
                display flex
                width 100%
                justify-content space-around
                p,input,select,option
                    font-size 14px
                    height 20px
                    margin 0
</style>