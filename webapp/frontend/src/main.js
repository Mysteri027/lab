import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { BootstrapVue } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueBankCard from "@avto-dev/bank-card-vue-component"
import "@avto-dev/bank-card-vue-component/dist/bank-card-vue-component.css"
import axios from "axios";

Vue.component("VueBankCard", VueBankCard)

Vue.config.productionTip = false

// // подключаем axios
Vue.prototype.$http = axios.create({
  baseURL: 'http://localhost:8000/'
})

new Vue({
  router,
  store,
  vuetify,
  BootstrapVue,
  render: h => h(App)
}).$mount('#app')


