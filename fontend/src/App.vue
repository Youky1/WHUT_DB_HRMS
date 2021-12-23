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

import {successfulTip,failTip} from './util.js'

import Header from './components/stable/Header'
import Footer from './components/stable/Footer'
import Entry from './components/Entry'
import Index from './components/Index'

const state = {
	successfulTip,				// 成功提示框函数
	failTip,					// 失败提示框函数
	userId:'',					// 当前用户的ID
}

const mutations = {
	// 登录
	login(state,payload){
		state.userId = payload.id;
	},
}

const store = new Vuex.Store({
  	state,
	mutations,
})

const router = new VueRouter({
	routes:[
		{path:'', component:Entry},								// 登录页面
		{path:'/index', component:Index},						// 登录后的首页
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
		font-size 16px
	.v-enter,.v-leave-to
		opacity 0
	.v-enter-to,.v-leave
		transition 0.5s all
		opacity 1
</style>