<template>
    <div id="dBox">
        <div id="container">
            <div class="tr">
                <div class="td" >姓名</div>
                <div class="td" >性别</div>
                <div class="td" >电话</div>
                <div class="td" >邮箱</div>
                <div class="td" >聘用日期</div>
            </div>
            <div class="tr" v-for="staff in staffInfo" :key="staff.id" @click="manage(staff)">
                <div class="td">{{staff.name}}</div>
                <div class="td">{{staff.sex}}</div>
                <div class="td">{{staff.phone}}</div>
                <div class="td">{{staff.email}}</div>
                <div class="td">{{staff.hireDate}}</div>
            </div>
        </div>

        <!-- 分配选择框 -->
        <div id="disContainer" v-if="manageNow">
            <div class="line">
                <p>部门</p>
                <select v-model="department">
                    <option v-for="part in departmentInfo" :key="part.id" :value="part.id">{{part.name}}</option>
                </select>
            </div>
            <div class="line">
                <p>职位</p>
                <select v-model="position">
                    <option v-for="position in positionInfo" :key="position.id" :value="position.id">{{position.name}}</option>
                </select>
            </div>
            <div class="line">
                <button @click="submitManage">调度</button>
                <button @click="cancle">取消</button>
            </div>
        </div>
    </div>
</template>

<script>
import { getAllStaffInfo, getDepartmentInfo, getWageInfo, manage } from '../../util'
export default {
    data(){
        return{
            staffInfo:[],
            departmentInfo:[],
            positionInfo:[],
            manageNow:false,
            currentStaffId:'',
            department:'',
            position:'',
        }
    },
    mounted(){
        getAllStaffInfo().then(res => {
            if(res.status){
                this.staffInfo = res.data
            }
        });
        getDepartmentInfo().then(res => {
            if(res.status){
                this.departmentInfo = res.data;
            }
        });
        getWageInfo().then(res => {
            if(res.status){
                this.positionInfo = res.data
            }
        })

    },
    methods:{
        manage(staff){
            this.currentStaffId = staff.id ;
            this.manageNow = true;
        },
        submitManage(){
            manage({
                user_id:this.currentStaffId,
                department_id:this.department,
                position_id:this.position
            }).then(res => {
                if(res.status){
                    this.$store.state.successfulTip('调度成功！')
                }else{
                    this.$store.state.failTip('调度失败')
                }
                this.cancle();
            }).catch(()=>{
                this.$store.state.failTip('调度失败');
                this.cancle();
            })
        },
        cancle(){
            this.manageNow = false;
            this.currentStaffId = '';
            this.department = '';
            this.position = '';
        },
    }
}
</script>

<style scoped>
    #dBox{
        height:75vh;
    }
    #container{
        height: 75vh;
        margin-left: 15vw;
        margin-top: 2vh;
        overflow-y: auto;
    }
    .tr{
        display: flex;
        border-top: 1px solid #777;
        border-bottom: 1px solid #777;
        height: 25px;
        background-color: #fff;
        cursor: pointer;
    }
    .td{
        width: 120px;
        border-left: 1px solid #777;
        border-right: 1px solid #777;
        font-size: 10px;
        height: 100%;
        display: flex;
        align-items: center;
        text-indent: 5px;
    }
    #disContainer{
        position: fixed;
        top: 50%;
        left: 50%;
        transform:translate(-50%,-50%);
        background-color: #3eb2c4;
        color: #fff;
        width: 300px;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
    }
    .line{
        display: flex;
        height: 20px;
        align-items: center;
    }
    .line p{
        width: 40px;
        margin: 0 30px 0 0;
    }
    .line select{
        width: 150px;
        outline: none;
    }
    .line button{
        width: 100px;
        height: 30px;
        margin: 0 30px;
    }
</style>