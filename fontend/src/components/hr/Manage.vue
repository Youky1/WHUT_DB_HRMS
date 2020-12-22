<template>
    <div id="dBox">
        <div id="container">
            <div class="tr">
                <div class="td" >姓名</div>
                <div class="td" >部门</div>
                <div class="td" >职位</div>
                <div class="td" >聘用日期</div>
            </div>
            <div class="tr" v-for="staff in staffInfo" :key="staff.ID" @click="goManage(staff)">
                <div class="td">{{staff.Name}}</div>
                <div class="td">{{staff.Department_name}}</div>
                <div class="td">{{staff.Position_name}}</div>
                <div class="td">{{staff.Hire_date}}</div>
            </div>
        </div>

        <!-- 分配选择框 -->
        <div id="disContainer" v-if="manageNow">
            <div class="line">
                <p>部门</p>
                <select v-model="department">
                    <option v-for="part in departmentInfo" 
                            :key="part.Department_id" 
                            :value="part.Department_name"
                    >{{part.Department_name}}</option>
                </select>
            </div>
            <div class="line">
                <p>职位</p>
                <select v-model="position">
                    <option v-for="position in positionInfo" 
                            :key="position.Position_id" 
                            :value="position.Position_name"
                    >{{position.Position_name}}</option>
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
import { getDistributedStaff, getDepartmentInfo, getWageInfo, manage } from '../../util'
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
        self = this;
        (async function fn(){
            await getDistributedStaff().then(res => {
                if(res.status){
                    self.staffInfo = res.data;
                }else{
                    console.log('getAllStaffInfo status false')
                }
            }).catch(err => console.log(err))
            await getDepartmentInfo().then(function(res){
                if(res.status){
                    self.departmentInfo = res.data;
                }else{
                    console.log('getDepartmentInfo status fail')
                }
            }).catch(err => console.log(err))
            await getWageInfo().then(res => {
                if(res.status){
                    self.positionInfo = res.data;
                }
            }).catch(err => console.log(err))
        })()
    },
    methods:{
        goManage(staff){
            this.currentStaffId = staff.ID ;
            this.manageNow = true;
        },
        submitManage(){
            manage({
                Employee_id:this.currentStaffId,
                Department_name:this.department,
                Position_name:this.position
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