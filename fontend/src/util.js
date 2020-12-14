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
    dom.style = `position:fixed;top:100px;left:48vw;font-size:12px;
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
    dom.style = `position:fixed;top:100px;left:48vw;font-size:12px;
    height:20px;display:flex;align-item:center`;
    dom.innerHTML = `<span class="iconfont iconshibai"></span></span>${content}`
    document.body.appendChild(dom)
    setTimeout(() => {
        document.body.removeChild(dom)
    },1500)
}

export{
    getData,
    postData,
    successfulTip,
    failTip,
}