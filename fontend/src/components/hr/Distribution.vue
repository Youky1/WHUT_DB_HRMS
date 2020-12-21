<template>
    <div id="dBox">
        <div id="container">
            <div class="tr">
                <div class="td2" >姓名</div>
                <div class="td1" >性别</div>
                <div class="td3" >电话</div>
                <div class="td4" >邮箱</div>
                <div class="td3" >聘用日期</div>
                <div class="td5" >工作经历</div>
            </div>
            <div class="tr" v-for="staff in staffInfo" :key="staff.ID" @click="distribute(staff)">
                <div class="td2">{{staff.Name}}</div>
                <div class="td1">{{staff.Sex}}</div>
                <div class="td3">{{staff.Phone}}</div>
                <div class="td4">{{staff.Email}}</div>
                <div class="td3">{{staff.Hire_date}}</div>
                <div class="td5">
                    <p class="ex" v-for="ex in staff.Work_experience" :key="ex.Work_experience">
                        {{ex.Work_experience}}；{{ex.Achievement}}
                    </p>
                </div>
            </div>
        </div>

        <!-- 分配选择框 -->
        <div id="disContainer" v-if="distributeNow">
            <div class="line">
                <p>部门</p>
                <select v-model="department">
                    <option v-for="part in departmentInfo" 
                            :key="part.Department_id" 
                            :value="part.Department_id"
                    >{{part.Department_name}}</option>
                </select>
            </div>
            <div class="line">
                <p>职位</p>
                <select v-model="position">
                    <option v-for="position in positionInfo" 
                            :key="position.Position_id" 
                            :value="position.Position_id"
                    >{{position.Position_name}}</option>
                </select>
            </div>
            <div class="line">
                <button @click="submitDis">分配</button>
                <button @click="cancle">取消</button>
            </div>
        </div>
    </div>
</template>

<script>
import { getLeftStaff, getDepartmentInfo, getWageInfo, distribution } from '../../util'
export default {
    data(){
        return{
            staffInfo:[],
            departmentInfo:[],
            positionInfo:[],
            distributeNow:false,
            currentStaffId:'',
            department:'',
            position:'',
        }
    },
    methods:{
        distribute(staff){
            this.currentStaffId = staff.ID ;
            this.distributeNow = true;
        },
        submitDis(){
            distribution({
                ID:this.currentStaffId,
                Department_id:this.department,
                Position_id:this.position
            }).then(res => {
                if(res.status){
                    this.$store.state.successfulTip('分配岗位成功！')
                }else{
                    this.$store.state.failTip('分配岗位失败')
                    console.log(res)
                }
                this.cancle();
            }).catch(err=>{
                console.log(err)
                this.$store.state.failTip('分配岗位失败');
                this.cancle();
            })
        },
        cancle(){
            this.distributeNow = false;
            this.currentStaffId = '';
            this.department = '';
            this.position = '';
        },
    },
    mounted(){
        self = this;
        (async function fn(){
            await getLeftStaff().then(res => {
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
    }
}
</script>

<style scoped>
    #dBox{
        height:75vh;
    }
    #container{
        height: 75vh;
        overflow: auto;
    }
    .tr{
        display: flex;
        border-top: 1px solid #777;
        border-bottom: 1px solid #777;
        height: 30px;
        background-color: #fff;
        cursor: pointer;
    }
    .td1{
        width: 20px;
        border-left: 1px solid #777;
        font-size: 10px;
        height: 30px;
    }
    .td2{
        width: 40px;
        border-left: 1px solid #777;
        font-size: 10px;
        height: 30px;
    }
    .td3{
        width: 90px;
        border-left: 1px solid #777;
        font-size: 10px;
        height: 30px;
    }
    .td4{
        width: 110px;
        border-left: 1px solid #777;
        font-size: 10px;
        height: 30px;
    }
    .td5{
        border-left: 1px solid #777;
        font-size: 10px;
        width: 500px;
        height: 30px;
        display: flex;
        overflow: hidden;
    }
    .ex{
        height: 30px;
        width: 100vw;
        overflow: hidden;
        border-left: 1px solid #777;
        margin: 0;
        font-size: 10px;
        word-break: break-all;
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