/* 封装全局函数 */

// get数据函数
const getData = url =>{
    return new Promise( resolve => {
        fetch(`http://localhost:8000/${url}`)
        .then(response => response.json())
        .then(myJson => resolve(myJson))
        .catch( e => console.log('there is something wrong in getData\n' + e))
    })
}

// post数据函数
const postData = (url,data) => {
  	return new Promise( resolve => {
        fetch(`http://localhost:8000/${url}`,{
          	body:JSON.stringify(data),
          	headers:{
          		'content-type':'aplication/json'
			},
			method:'POST',
			mode:'cors'
        })
        .then(response => response.json())
        .then(myJson => resolve(myJson))
        .catch( e => console.log('there is something wrong in postData\n' + e))
    })
}

// 成功提示
function successfulTip(content){
    let dom = document.createElement('div');
    dom.style = `position:fixed;top:100px;left:46vw;font-size:12px;
    height:20px;display:flex;align-item:center`;
    dom.innerHTML = `<span class="iconfont iconchenggong"></span></span>${content}`
    document.body.appendChild(dom)
    setTimeout(() => {
        document.body.removeChild(dom)
    },1000)
}

// 失败提示
function failTip(content){
    let dom = document.createElement('div');
    dom.style = `position:fixed;top:100px;left:46vw;font-size:12px;
    height:20px;display:flex;align-item:center`;
    dom.innerHTML = `<span class="iconfont iconshibai"></span></span>${content}`
    document.body.appendChild(dom)
    setTimeout(() => {
        document.body.removeChild(dom)
    },1500)
}

// 登录
function login(data){
    return postData('login',JSON.stringify(data))
}

// 获取个人信息
function getUserInfo(id){
    return postData('info/user',JSON.stringify({id}))
}

// 获取公司的职位信息
function getWageInfo(){
    return getData('info/wage')
}

// 获取公司各个部门的信息
function getDepartmentInfo(){
    return getData('department/info');
}

// 修改某个部门的信息
function changeDepartmentInfo(info){
    return postData('department/change',JSON.stringify(info))
}

// 录用新员工
function hire(data){
    return postData('hr/hire',JSON.stringify(data))
}

// 为员工分配岗位
function distribution(data){
    return postData('hr/distribution',JSON.stringify(data))
}

// 调整员工的岗位
function manage(data){
    return postData('hr/manage',JSON.stringify(data))
}

export{
    login,
    getData,
    postData,
    successfulTip,
    failTip,
    getUserInfo,
    getWageInfo,
    getDepartmentInfo,
    changeDepartmentInfo,
    hire,
    distribution,
    manage,
}