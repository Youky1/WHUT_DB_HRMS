(function(t){function e(e){for(var i,s,r=e[0],c=e[1],u=e[2],f=0,d=[];f<r.length;f++)s=r[f],Object.prototype.hasOwnProperty.call(a,s)&&a[s]&&d.push(a[s][0]),a[s]=0;for(i in c)Object.prototype.hasOwnProperty.call(c,i)&&(t[i]=c[i]);l&&l(e);while(d.length)d.shift()();return o.push.apply(o,u||[]),n()}function n(){for(var t,e=0;e<o.length;e++){for(var n=o[e],i=!0,r=1;r<n.length;r++){var c=n[r];0!==a[c]&&(i=!1)}i&&(o.splice(e--,1),t=s(s.s=n[0]))}return t}var i={},a={app:0},o=[];function s(e){if(i[e])return i[e].exports;var n=i[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.m=t,s.c=i,s.d=function(t,e,n){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var i in t)s.d(n,i,function(e){return t[e]}.bind(null,i));return n},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],c=r.push.bind(r);r.push=e,r=r.slice();for(var u=0;u<r.length;u++)e(r[u]);var l=c;o.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"06cd":function(t,e,n){"use strict";n("96e9")},"15a8":function(t,e,n){},"19e0":function(t,e,n){"use strict";n("6353")},"1d5a":function(t,e,n){"use strict";n("a0b5")},2885:function(t,e,n){"use strict";n("f4f8")},"2db8":function(t,e,n){"use strict";n("ef4d")},"2f0f":function(t,e,n){},"369f":function(t,e,n){},"3fae":function(t,e,n){"use strict";n("ea8d")},4171:function(t,e,n){"use strict";n("369f")},5134:function(t,e,n){},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var i=n("2b0e"),a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("page-header"),n("transition",[n("router-view")],1),n("page-footer")],1)},o=[],s=n("2f62"),r=n("8c4f"),c=(n("d3b7"),function(t){return new Promise((function(e){fetch("http://localhost:8000/".concat(t)).then((function(t){return t.json()})).then((function(t){return e(t)})).catch((function(t){return console.log("there is something wrong in getData\n"+t)}))}))}),u=function(t,e){return new Promise((function(n){fetch("http://localhost:8000/".concat(t),{body:JSON.stringify(e),headers:{"content-type":"aplication/json"},method:"POST",mode:"cors"}).then((function(t){return t.json()})).then((function(t){return n(t)})).catch((function(t){return console.log("there is something wrong in postData\n"+t)}))}))};function l(t){var e=document.createElement("div");e.style="position:fixed;top:50px;left:46vw;font-size:12px;\n    height:20px;display:flex;align-item:center",e.innerHTML='<span class="iconfont iconchenggong"></span></span>'.concat(t),document.body.appendChild(e),setTimeout((function(){document.body.removeChild(e)}),1e3)}function f(t){var e=document.createElement("div");e.style="position:fixed;top:50px;left:46vw;font-size:12px;\n    height:20px;display:flex;align-item:center",e.innerHTML='<span class="iconfont iconshibai"></span></span>'.concat(t),document.body.appendChild(e),setTimeout((function(){document.body.removeChild(e)}),1500)}var d=function(t,e,n){var i=t.$echarts.init(e);i.setOption(n)};function p(t){return u("login",JSON.stringify(t))}function m(t){return u("info/user",JSON.stringify({ID:t}))}function v(){return u("info/wage",JSON.stringify({}))}function _(){return c("department/info")}function h(t){return u("department/change",JSON.stringify(t))}function g(t){return u("hr/hire",JSON.stringify(t))}function y(t){return u("department/staff",JSON.stringify(t))}function x(){return c("hr/staff/yes")}function b(){return c("hr/staff/no")}function C(t){return u("hr/distribution",JSON.stringify(t))}function w(t){return u("hr/manage",JSON.stringify(t))}var I=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("Header",[i("img",{attrs:{id:"logo",src:n("cf05")}}),i("div",{attrs:{id:"title"}},[t._v("人力资源管理系统")]),i("div",{staticStyle:{position:"absolute",right:"10vw"}},[i("a",{attrs:{href:"https://github.com/Youky1/WHUT_DB_HRMS",target:"_blank"}},[t._v(" Github "),i("span",{staticClass:"iconfont icongithub"})])])])},D=[],O=n("5530"),k={computed:Object(O["a"])({},Object(s["b"])(["hasLogin","failTip"]))},P=k,S=(n("2db8"),n("2877")),N=Object(S["a"])(P,I,D,!1,null,"3fe0ac60",null),j=N.exports,$=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},T=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("footer",[n("p",[t._v("Copyright © 2020")])])}],E={},A=E,M=(n("2885"),Object(S["a"])(A,$,T,!1,null,"2eeaffca",null)),B=M.exports,H=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"totalContainer"}},[n("div",{attrs:{id:"contentBox"}},[n("div",{attrs:{id:"infoInputContainer"}},[n("input",{directives:[{name:"model",rawName:"v-model",value:t.user_id,expression:"user_id"}],staticClass:"infoInputBox",attrs:{type:"text",placeholder:"请输入用户ID"},domProps:{value:t.user_id},on:{input:function(e){e.target.composing||(t.user_id=e.target.value)}}}),n("input",{directives:[{name:"model",rawName:"v-model",value:t.user_password,expression:"user_password"}],staticClass:"infoInputBox",attrs:{type:"password",placeholder:"请输入密码"},domProps:{value:t.user_password},on:{input:function(e){e.target.composing||(t.user_password=e.target.value)}}})]),n("button",{attrs:{id:"operationBtn"},on:{click:t.login}},[t._v("登录")])])])},W=[],J={name:"Entry",methods:{login:function(){var t=this,e={id:this.user_id,password:this.user_password};p(e).then((function(n){n.status?(t.$store.commit("login",e),t.successfulTip("登录成功！"),t.$router.push("index")):(t.failTip("ID或密码错误，登录失败！"),t.user_id="",t.user_password="")}))}},data:function(){return{user_id:"0001",user_password:"123456"}},computed:Object(O["a"])({},Object(s["b"])(["postData","successfulTip","failTip"]))},R=J,z=(n("1d5a"),Object(S["a"])(R,H,W,!1,null,null,null)),F=z.exports,L=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"totalBox"}},[n("div",{attrs:{id:"functionBar"}},[n("div",{staticClass:"functionTitle"},[t._v("信息查询")]),n("div",{staticClass:"functionItem",on:{click:function(e){return t.changeShowingComponent("Self")}}},[n("strong",{staticClass:"icon iconfont icongerenxinxi-copy"}),t._v(" 个人信息 ")]),n("div",{staticClass:"functionItem",on:{click:function(e){return t.changeShowingComponent("CompanyWage")}}},[n("span",{staticClass:"icon iconfont iconxinzidaiyu"}),t._v(" 薪资待遇 ")]),n("div",{staticClass:"functionTitle"},[t._v("公司业务管理")]),n("div",{staticClass:"functionItem",on:{click:function(e){return t.changeShowingComponent("DepartmentInfo")}}},[n("span",{staticClass:"icon iconfont iconbumen"}),t._v(" 部门管理 ")]),n("div",{staticClass:"functionItem",on:{click:function(e){return t.changeShowingComponent("PositionCount")}}},[n("span",{staticClass:"icon iconfont iconzhiwei"}),t._v(" 职位统计 ")]),n("div",{staticClass:"functionTitle"},[t._v("人事管理")]),n("div",{staticClass:"functionItem",on:{click:function(e){return t.changeShowingComponent("Hire")}}},[n("span",{staticClass:"icon iconfont iconluyong"}),t._v(" 员工录用 ")]),n("div",{staticClass:"functionItem",on:{click:function(e){return t.changeShowingComponent("Distribution")}}},[n("span",{staticClass:"icon iconfont iconfenpei"}),t._v(" 岗位分配 ")]),n("div",{staticClass:"functionItem",on:{click:function(e){return t.changeShowingComponent("Manage")}}},[n("span",{staticClass:"icon iconfont icontiaozheng"}),t._v(" 岗位调整 ")])]),n(t.currentComponent,{tag:"component"})],1)},Y=[],G=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"outsideBox"}},[n("h3",{attrs:{id:"welcome"}},[t._v("欢迎使用本系统")]),n("p",[t._v("您的身份是 "),n("strong",{domProps:{innerHTML:t._s(t.identity)}})]),n("p",{attrs:{id:"date"}},[t._v(t._s(t.date))])])},U=[],q=(n("99af"),{computed:Object(O["a"])(Object(O["a"])({},Object(s["b"])(["hrIdentity"])),{},{identity:function(){return"管理员<span class='iconfont iconadmin'></span>"},date:function(){var t=new Date,e="".concat(t.getFullYear(),"/").concat(t.getMonth(),"/").concat(t.getDate(),",周").concat(t.getDay());return"现在是".concat(e)}})}),K=q,Q=(n("a164"),Object(S["a"])(K,G,U,!1,null,"4a8828c4",null)),V=Q.exports,X=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"outsideBox"}},[n("div",{attrs:{id:"name"}},[n("span",{staticClass:"iconfont iconadmin"},[t._v(t._s(t.userInfo.Name))])]),n("div",{attrs:{id:"container"}},t._l(t.infoToShow,(function(e){return n("div",{key:e[0],staticClass:"infoItem"},[n("strong",[t._v(t._s(e[0]))]),n("p",[t._v(t._s(e[1]))])])})),0),t._m(0),n("div",{attrs:{id:"experienceList"}},t._l(t.userInfo.Work_experience,(function(e){return n("div",{key:e.description,staticClass:"experienceItem"},[n("p",{staticClass:"listItem"},[t._v(t._s(e.Work_experience))]),n("p",{staticClass:"listItem"},[t._v(t._s(e.Achievement))])])})),0)])},Z=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"listTitle"}},[n("div",{staticClass:"listItem",staticStyle:{border:"none"}},[t._v("工作经历")]),n("div",{staticClass:"listItem",staticStyle:{border:"none"}},[t._v("成绩")])])}],tt={data:function(){return{userInfo:{Name:""}}},computed:Object(O["a"])(Object(O["a"])({},Object(s["b"])(["userId"])),{},{name:function(){return""},infoToShow:function(){var t=["Sex","Phone","Email","Department_name","Position_name","Hire_date"],e=["性别","电话","邮箱","部门","职位","招聘日期"],n=[];for(var i in t)n.push([e[i],this.userInfo[t[i]]]);return console.log(n),n}}),mounted:function(){var t=this;m(this.userId).then((function(e){e.status?t.userInfo=e.data:console.log("查找个人信息失败")}))}},et=tt,nt=(n("3fae"),Object(S["a"])(et,X,Z,!1,null,"25d86dda",null)),it=nt.exports,at=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},ot=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"totalBox"}},[n("div",{attrs:{id:"chartBox"}})])}],st=n("b85c"),rt=(n("96cf"),n("1da1")),ct={name:"Manage",data:function(){return{minePosition:null,option:null}},mounted:function(){var t=this;Object(rt["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return console.log("ID is ",t.$store.state.userId),e.next=3,m(t.$store.state.userId).then((function(e){e.status?(console.log(e.data),t.minePosition=e.data.Position_name,console.log(t.minePosition)):console.log("fuck")})).catch((function(t){return console.log(t)}));case 3:return e.next=5,v().then((function(e){if(e.status){var n,i=[],a=Object(st["a"])(e.data);try{for(a.s();!(n=a.n()).done;){var o=n.value;i.push({position:o.Position_name,salary:o.Salary})}}catch(s){a.e(s)}finally{a.f()}t.option={title:{text:"各职位薪资情况对比"},dataset:{dimensions:["position","salary"],source:i},xAxis:{type:"category"},yAxis:{},tooltip:{},series:[{type:"bar",itemStyle:{normal:{color:function(e){return console.log(t.minePosition),console.log(e.data.position),e.data.position==t.minePosition?"#FFA500":"#FF6347"}}}}]}}}));case 5:return e.next=7,d(t,document.getElementById("chartBox"),t.option);case 7:case"end":return e.stop()}}),e)})))()}},ut=ct,lt=(n("7689"),Object(S["a"])(ut,at,ot,!1,null,"26f08152",null)),ft=lt.exports,dt=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"outsideBox"}},[n("div",{attrs:{id:"infoBox"}},t._l(t.departmentInfo,(function(e){return n("div",{key:e.Department_id,staticClass:"departmentInfo",on:{click:function(n){return t.changeInfo(e)}}},[n("div",{attrs:{id:"line"}},[n("p",{attrs:{id:"name"}},[t._v(t._s(e.Department_name))]),n("p",{attrs:{id:"host"}},[t._v("主管："),n("span",[t._v(t._s(e.Manager))])])]),n("div",{attrs:{id:"description"}},[t._v(t._s(e.Affairs))])])})),0),t.changeNow?n("div",{attrs:{id:"infoChart"}},[n("div",{staticClass:"part"},[n("p",[t._v("部门名称")]),n("input",{directives:[{name:"model",rawName:"v-model",value:t.currentDepartment.Department_name,expression:"currentDepartment.Department_name"}],attrs:{type:"text"},domProps:{value:t.currentDepartment.Department_name},on:{input:function(e){e.target.composing||t.$set(t.currentDepartment,"Department_name",e.target.value)}}})]),n("div",{staticClass:"part"},[n("p",[t._v("部门主管")]),n("select",{directives:[{name:"model",rawName:"v-model",value:t.currentDepartment.Manager,expression:"currentDepartment.Manager"}],attrs:{id:"managerContainer"},on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.$set(t.currentDepartment,"Manager",e.target.multiple?n:n[0])}}},t._l(t.staffOfCurrentDepartment,(function(e){return n("option",{key:e.id,domProps:{value:e.Employee_id}},[t._v(t._s(e.Employee_name))])})),0)]),n("div",{staticClass:"part"},[n("p",[t._v("部门事务")]),n("input",{directives:[{name:"model",rawName:"v-model",value:t.currentDepartment.Affairs,expression:"currentDepartment.Affairs"}],attrs:{type:"text"},domProps:{value:t.currentDepartment.Affairs},on:{input:function(e){e.target.composing||t.$set(t.currentDepartment,"Affairs",e.target.value)}}})]),n("div",{staticClass:"part"},[n("button",{staticClass:"hideBtn",on:{click:t.submit}},[t._v("修改")]),n("button",{staticClass:"hideBtn",on:{click:t.cancel}},[t._v("取消")])])]):t._e()])},pt=[],mt={data:function(){return{departmentInfo:[],currentDepartment:{},changeNow:!1,staffOfCurrentDepartment:[]}},methods:{changeInfo:function(t){var e=this;console.log(t),this.currentDepartment=JSON.parse(JSON.stringify(t)),this.changeNow=!0,y({department_id:t.Department_id}).then((function(t){t.status&&(e.staffOfCurrentDepartment=t.data)}))},submit:function(){var t=this;console.log(this.currentDepartment.Manager),h({Department_id:this.currentDepartment.Department_id,New_Department_name:this.currentDepartment.Department_name,New_Manager_id:this.currentDepartment.Manager,New_Affairs:this.currentDepartment.Affairs}).then((function(e){e.status?(t.successfulTip("部门信息修改成功"),t.cancel()):t.failTip("部门信息修改失败")}))},cancel:function(){this.currentDepartment={},this.changeNow=!1,this.staffOfCurrentDepartment=[]}},mounted:function(){var t=this;_().then((function(e){e.status&&(t.departmentInfo=e.data)}))},computed:Object(O["a"])({},Object(s["b"])(["successfulTip","failTip"]))},vt=mt,_t=(n("ee4b"),Object(S["a"])(vt,dt,pt,!1,null,"75876819",null)),ht=_t.exports,gt=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},yt=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"totalBox"}},[n("div",{attrs:{id:"countChart"}})])}],xt={mounted:function(){var t=this;v().then((function(e){if(e.status){var n,i=[],a=Object(st["a"])(e.data);try{for(a.s();!(n=a.n()).done;){var o=n.value;i.push({name:o.Position_name,"共需要":o.Post_number,"已安排":o.Post_already})}}catch(r){a.e(r)}finally{a.f()}console.log(i);var s={legend:{},tooltip:{},dataset:{dimensions:["name","共需要","已安排"],source:i},xAxis:{type:"category"},yAxis:{},series:[{type:"bar"},{type:"bar"}]};d(t,document.getElementById("countChart"),s)}}))},data:function(){return{}}},bt=xt,Ct=(n("9b60"),Object(S["a"])(bt,gt,yt,!1,null,"7f6d586f",null)),wt=Ct.exports,It=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"dBox"}},[n("div",{attrs:{id:"container"}},[t._m(0),t._l(t.staffInfo,(function(e){return n("div",{key:e.ID,staticClass:"tr",on:{click:function(n){return t.distribute(e)}}},[n("div",{staticClass:"td2"},[t._v(t._s(e.Name))]),n("div",{staticClass:"td1"},[t._v(t._s(e.Sex))]),n("div",{staticClass:"td3"},[t._v(t._s(e.Phone))]),n("div",{staticClass:"td4"},[t._v(t._s(e.Email))]),n("div",{staticClass:"td3"},[t._v(t._s(e.Hire_date))]),n("div",{staticClass:"td5"},t._l(e.Work_experience,(function(e){return n("p",{key:e.Work_experience,staticClass:"ex"},[t._v(" "+t._s(e.Work_experience)+"；"+t._s(e.Achievement)+" ")])})),0)])}))],2),t.distributeNow?n("div",{attrs:{id:"disContainer"}},[n("div",{staticClass:"line"},[n("p",[t._v("部门")]),n("select",{directives:[{name:"model",rawName:"v-model",value:t.department,expression:"department"}],on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.department=e.target.multiple?n:n[0]}}},t._l(t.departmentInfo,(function(e){return n("option",{key:e.Department_id,domProps:{value:e.Department_id}},[t._v(t._s(e.Department_name))])})),0)]),n("div",{staticClass:"line"},[n("p",[t._v("职位")]),n("select",{directives:[{name:"model",rawName:"v-model",value:t.position,expression:"position"}],on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.position=e.target.multiple?n:n[0]}}},t._l(t.positionInfo,(function(e){return n("option",{key:e.Position_id,domProps:{value:e.Position_id}},[t._v(t._s(e.Position_name))])})),0)]),n("div",{staticClass:"line"},[n("button",{on:{click:t.submitDis}},[t._v("分配")]),n("button",{on:{click:t.cancle}},[t._v("取消")])])]):t._e()])},Dt=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"tr"},[n("div",{staticClass:"td2"},[t._v("姓名")]),n("div",{staticClass:"td1"},[t._v("性别")]),n("div",{staticClass:"td3"},[t._v("电话")]),n("div",{staticClass:"td4"},[t._v("邮箱")]),n("div",{staticClass:"td3"},[t._v("聘用日期")]),n("div",{staticClass:"td5"},[t._v("工作经历")])])}],Ot={data:function(){return{staffInfo:[],departmentInfo:[],positionInfo:[],distributeNow:!1,currentStaffId:"",department:"",position:""}},methods:{distribute:function(t){this.currentStaffId=t.ID,this.distributeNow=!0},submitDis:function(){var t=this;C({ID:this.currentStaffId,Department_id:this.department,Position_id:this.position}).then((function(e){e.status?t.$store.state.successfulTip("分配岗位成功！"):(t.$store.state.failTip("分配岗位失败"),console.log(e)),t.cancle()})).catch((function(e){console.log(e),t.$store.state.failTip("分配岗位失败"),t.cancle()}))},cancle:function(){this.distributeNow=!1,this.currentStaffId="",this.department="",this.position=""}},mounted:function(){self=this,function(){var t=Object(rt["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,b().then((function(t){t.status?self.staffInfo=t.data:console.log("getAllStaffInfo status false")})).catch((function(t){return console.log(t)}));case 2:return t.next=4,_().then((function(t){t.status?self.departmentInfo=t.data:console.log("getDepartmentInfo status fail")})).catch((function(t){return console.log(t)}));case 4:return t.next=6,v().then((function(t){t.status&&(self.positionInfo=t.data)})).catch((function(t){return console.log(t)}));case 6:case"end":return t.stop()}}),t)})));function e(){return t.apply(this,arguments)}return e}()()}},kt=Ot,Pt=(n("06cd"),Object(S["a"])(kt,It,Dt,!1,null,"503af38e",null)),St=Pt.exports,Nt=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"hireBox"}},[n("div",{attrs:{id:"basicInfo"}},[n("div",{staticClass:"line"},[n("p",{staticClass:"key"},[t._v("姓名")]),n("input",{directives:[{name:"model",rawName:"v-model",value:t.info.Name,expression:"info.Name"}],staticClass:"value",attrs:{type:"text"},domProps:{value:t.info.Name},on:{input:function(e){e.target.composing||t.$set(t.info,"Name",e.target.value)}}})]),n("div",{staticClass:"line"},[n("p",{staticClass:"key"},[t._v("性别")]),n("select",{directives:[{name:"model",rawName:"v-model",value:t.info.Sex,expression:"info.Sex"}],staticClass:"value",on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.$set(t.info,"Sex",e.target.multiple?n:n[0])}}},[n("option",{attrs:{value:"男"}},[t._v("男")]),n("option",{attrs:{value:"女"}},[t._v("女")])])]),n("div",{staticClass:"line"},[n("p",{staticClass:"key"},[t._v("手机号")]),n("input",{directives:[{name:"model",rawName:"v-model",value:t.info.Phone,expression:"info.Phone"}],staticClass:"value",attrs:{type:"text"},domProps:{value:t.info.Phone},on:{input:function(e){e.target.composing||t.$set(t.info,"Phone",e.target.value)}}})]),n("div",{staticClass:"line"},[n("p",{staticClass:"key"},[t._v("邮箱")]),n("input",{directives:[{name:"model",rawName:"v-model",value:t.info.Email,expression:"info.Email"}],staticClass:"value",attrs:{type:"text"},domProps:{value:t.info.Email},on:{input:function(e){e.target.composing||t.$set(t.info,"Email",e.target.value)}}})]),n("div",{staticClass:"line"},[n("p",{staticClass:"key"},[t._v("聘用日期")]),n("input",{directives:[{name:"model",rawName:"v-model",value:t.info.Hire_date,expression:"info.Hire_date"}],staticClass:"value",attrs:{type:"text"},domProps:{value:t.info.Hire_date},on:{input:function(e){e.target.composing||t.$set(t.info,"Hire_date",e.target.value)}}})])]),n("div",{attrs:{id:"experienceInfo"}},[n("h3",[t._v("工作经验")]),t._m(0),t._l(t.info.Work_experience,(function(e){return n("div",{key:e.ID,staticClass:"line",staticStyle:{"margin-bottom":"20px"}},[n("input",{directives:[{name:"model",rawName:"v-model",value:e.Work_experience,expression:"e.Work_experience"}],staticClass:"value",attrs:{type:"text"},domProps:{value:e.Work_experience},on:{input:function(n){n.target.composing||t.$set(e,"Work_experience",n.target.value)}}}),n("input",{directives:[{name:"model",rawName:"v-model",value:e.Achievement,expression:"e.Achievement"}],staticClass:"value",attrs:{type:"text"},domProps:{value:e.Achievement},on:{input:function(n){n.target.composing||t.$set(e,"Achievement",n.target.value)}}})])})),n("div",{attrs:{id:"btnContainer"}},[n("button",{on:{click:t.add}},[t._v("添加")]),n("button",{on:{click:t.confirmHire}},[t._v("录用")])])],2)])},jt=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"line"},[n("p",{staticClass:"value",staticStyle:{border:"none"}},[t._v("工作经历")]),n("p",{staticClass:"value",staticStyle:{border:"none"}},[t._v("成绩")])])}],$t=(n("b64b"),{name:"Manage",data:function(){return{info:{Sex:"",Name:"",Email:"",Phone:"",Hire_date:"",Work_experience:[]}}},computed:Object(O["a"])({},Object(s["b"])(["failTip","successfulTip"])),methods:{add:function(){this.info.Work_experience.length>4?this.failTip("工作记录最多五条"):this.info.Work_experience.push({Work_experience:"",Achievement:""})},confirmHire:function(){var t=this;g(this.info).then((function(e){if(e.status){t.successfulTip("录用成功！");for(var n=0,i=Object.keys(t.info);n<i.length;n++){var a=i[n];t.info[a]=""}t.info.experience=[]}}))}}}),Tt=$t,Et=(n("4171"),Object(S["a"])(Tt,Nt,jt,!1,null,"179ec4fc",null)),At=Et.exports,Mt=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"dBox"}},[n("div",{attrs:{id:"container"}},[t._m(0),t._l(t.staffInfo,(function(e){return n("div",{key:e.ID,staticClass:"tr",on:{click:function(n){return t.goManage(e)}}},[n("div",{staticClass:"td"},[t._v(t._s(e.Name))]),n("div",{staticClass:"td"},[t._v(t._s(e.Department_name))]),n("div",{staticClass:"td"},[t._v(t._s(e.Position_name))]),n("div",{staticClass:"td"},[t._v(t._s(e.Hire_date))])])}))],2),t.manageNow?n("div",{attrs:{id:"disContainer"}},[n("div",{staticClass:"line"},[n("p",[t._v("部门")]),n("select",{directives:[{name:"model",rawName:"v-model",value:t.department,expression:"department"}],on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.department=e.target.multiple?n:n[0]}}},t._l(t.departmentInfo,(function(e){return n("option",{key:e.Department_id,domProps:{value:e.Department_name}},[t._v(t._s(e.Department_name))])})),0)]),n("div",{staticClass:"line"},[n("p",[t._v("职位")]),n("select",{directives:[{name:"model",rawName:"v-model",value:t.position,expression:"position"}],on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.position=e.target.multiple?n:n[0]}}},t._l(t.positionInfo,(function(e){return n("option",{key:e.Position_id,domProps:{value:e.Position_name}},[t._v(t._s(e.Position_name))])})),0)]),n("div",{staticClass:"line"},[n("button",{on:{click:t.submitManage}},[t._v("调度")]),n("button",{on:{click:t.cancle}},[t._v("取消")])])]):t._e()])},Bt=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"tr"},[n("div",{staticClass:"td"},[t._v("姓名")]),n("div",{staticClass:"td"},[t._v("部门")]),n("div",{staticClass:"td"},[t._v("职位")]),n("div",{staticClass:"td"},[t._v("聘用日期")])])}],Ht={data:function(){return{staffInfo:[],departmentInfo:[],positionInfo:[],manageNow:!1,currentStaffId:"",department:"",position:""}},mounted:function(){self=this,function(){var t=Object(rt["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,x().then((function(t){t.status?self.staffInfo=t.data:console.log("getAllStaffInfo status false")})).catch((function(t){return console.log(t)}));case 2:return t.next=4,_().then((function(t){t.status?self.departmentInfo=t.data:console.log("getDepartmentInfo status fail")})).catch((function(t){return console.log(t)}));case 4:return t.next=6,v().then((function(t){t.status&&(self.positionInfo=t.data)})).catch((function(t){return console.log(t)}));case 6:case"end":return t.stop()}}),t)})));function e(){return t.apply(this,arguments)}return e}()()},methods:{goManage:function(t){this.currentStaffId=t.ID,this.manageNow=!0},submitManage:function(){var t=this;w({Employee_id:this.currentStaffId,Department_name:this.department,Position_name:this.position}).then((function(e){e.status?t.$store.state.successfulTip("调度成功！"):t.$store.state.failTip("调度失败"),t.cancle()})).catch((function(){t.$store.state.failTip("调度失败"),t.cancle()}))},cancle:function(){this.manageNow=!1,this.currentStaffId="",this.department="",this.position=""}}},Wt=Ht,Jt=(n("579a"),Object(S["a"])(Wt,Mt,Bt,!1,null,"8980de92",null)),Rt=Jt.exports,zt={name:"Index",data:function(){return{currentComponent:"default"}},components:{Default:V,Self:it,CompanyWage:ft,DepartmentInfo:ht,PositionCount:wt,Distribution:St,Hire:At,Manage:Rt},methods:{changeShowingComponent:function(t){this.currentComponent=t}},mounted:function(){}},Ft=zt,Lt=(n("19e0"),Object(S["a"])(Ft,L,Y,!1,null,"40a47322",null)),Yt=Lt.exports;i["a"].use(s["a"]),i["a"].use(r["a"]);var Gt={successfulTip:l,failTip:f,userId:""},Ut={login:function(t,e){t.userId=e.id}},qt=new s["a"].Store({state:Gt,mutations:Ut}),Kt=new r["a"]({routes:[{path:"",component:F},{path:"/index",component:Yt}]}),Qt={name:"App",store:qt,router:Kt,components:{"page-header":j,"page-footer":B}},Vt=Qt,Xt=(n("a2b4"),Object(S["a"])(Vt,a,o,!1,null,"4cd072c9",null)),Zt=Xt.exports,te=n("63e3");i["a"].config.productionTip=!1,i["a"].prototype.$echarts=te,new i["a"]({render:function(t){return t(Zt)}}).$mount("#app")},"579a":function(t,e,n){"use strict";n("f031")},6353:function(t,e,n){},7689:function(t,e,n){"use strict";n("eca3")},"96e9":function(t,e,n){},"9b60":function(t,e,n){"use strict";n("15a8")},"9daf":function(t,e,n){},a0b5:function(t,e,n){},a164:function(t,e,n){"use strict";n("9daf")},a2b4:function(t,e,n){"use strict";n("5134")},cf05:function(t,e,n){t.exports=n.p+"img/logo.84ccb464.png"},ea8d:function(t,e,n){},eca3:function(t,e,n){},ee4b:function(t,e,n){"use strict";n("2f0f")},ef4d:function(t,e,n){},f031:function(t,e,n){},f4f8:function(t,e,n){}});