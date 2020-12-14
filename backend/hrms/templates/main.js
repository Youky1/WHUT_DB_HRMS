// GET通信函数，传入要访问的接口，返回一个操作该返回数据的Promise
function getData(url){
    return new Promise( resolve => {
        fetch(`http://localhost:8000/${url}`)
        .then(response => response.json())
        .then(myJson => resolve(myJson))
        .catch( e => console.log(e))
    })
}
getData('apitest').then(data => console.log(data))