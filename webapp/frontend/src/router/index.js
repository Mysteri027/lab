import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from "@/views/MainPage";
import LoginPage from "@/views/LoginPage";
import RegistrationPage from "@/views/RegistrationPage";
import MoneyTransferPage from "@/views/MoneyTransferPage";
import TransferHistoryPage from "@/views/TransferHistoryPage";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainPage
  },

  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },

  {
    path: '/registration',
    name: 'registration',
    component: RegistrationPage
  },

  {
    path: '/moneytransfer',
    name: 'moneytransfer',
    component: MoneyTransferPage
  },

  {
    path: '/transferhistory',
    name: 'transferhistory',
    component: TransferHistoryPage
  },

]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
