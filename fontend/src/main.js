import Vue from 'vue'
Vue.config.productionTip = false;

import App from './App.vue'

import * as echarts from 'echarts'
Vue.prototype.$echarts = echarts

new Vue({
  	render: h => h(App),
}).$mount('#app')
