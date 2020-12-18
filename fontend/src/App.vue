<template>
  <div id="app">
	  <page-header></page-header>
	  <transition>
		  <router-view></router-view>
	  </transition>
	  <page-footer></page-footer>
  </div>
</template>

<script>

import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'

Vue.use(Vuex);
Vue.use(VueRouter);

import {getData,postData,successfulTip,failTip} from './util.js'

import Header from './components/stable/Header'
import Footer from './components/stable/Footer'
import Entry from './components/account/Entry'
import Signup from './components/account/Signup'
import ChangePassword from './components/account/ChangePassword'
import ChangeUserInfo from './components/account/ChangeUserInfo'
import Index from './components/Index'

const state = {
	getData,					// get函数
	postData,					// post函数
	successfulTip,				// 成功提示框函数
	failTip,					// 失败提示框函数

	userId:'',					// 当前账户的ID
	userPassword:'',			// 当前账户的密码
	hasLogin:false,				// 登录状态：是否已经登录
	signupPermission:false,		// 注册状态检查：ID是否已经授权
	infoInput:{					// 用户输入的信息，在注册或修改个人信息时使用
		name: '',
		sex: '',
		phone: '',
		email: '',
	},
	hrIdentity:true,			// 管理员权限
	userInfo:{					// 根据ID查询的当前用户的信息
		name: 'name',
		sex: '男',
		phone: '15623687738',
		email: 'youkyf@qq.com',
        department:'计算机1803',
        position:'学生',
        hireDate:'2018.9.8',
        workExperience:'3',
        achievement:'90',
	},
	companyInfo:{				// 公司的部门信息
	},
	
}

const mutations = {
	// 登录
	login(state,payload){
		state.userId = payload.user_id;
		state.userPassword = payload.user_password;
		state.hasLogin = true;
	},
	// 跳转至注册页面
	goSignup(state,payload){
		state.userId = payload.id;
		state.signupPermission = true;
	},
	// 修改密码
	changeUserPassword(state,payload){
		state.userPassword = payload.user_password
	},
	// 存储当前输入的个人信息
	setUserInfo(state,{name,sex,phone,email}){
		state.infoInput.name = name;
		state.infoInput.sex = sex;
		state.infoInput.phone = phone;
		state.infoInput.email = email;
	},
	// 注销登录
	logout(state){
		for(let key of Object.keys(state.userInfo)){
			state.userInfo.key = ''
		}
		state.hrIdentity = false;
		state.signupPermission = false;
		state.hasLogin = false;
		state.userId = '';
		state.userPassword = '';
	},
}

const store = new Vuex.Store({
  	state,
	mutations,
})

const router = new VueRouter({
	routes:[
		{path:'', component:Entry},								// 首页，注册或登录
		{path:'/signup',component:Signup},						// 填写注册的个人信息
		{path:'/index', component:Index},						// 登录后的首页
		{path:'/change/password',component:ChangePassword},		// 修改密码页面
		{path:'/change/userinfo',component:ChangeUserInfo},		// 修改用户信息

	]
})

export default {
  	name: 'App',
  	store,
  	router,
  	components: {
		'page-header':Header,
		'page-footer':Footer
	},
}

</script>

<style lang="stylus" scoped>
	html,body
		margin 0
		padding 0
	.v-enter,.v-leave-to
		opacity 0
	.v-enter-to,.v-leave
		transition 0.5s all
		opacity 1
</style>