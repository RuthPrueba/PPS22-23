import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import TrabajaView from '@/views/TrabajaView.vue'
import InfoView from '@/views/InfoView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/trabaja-con-nosotros',
    name: 'trabaja-con-nosotros',
    component: TrabajaView
  },
  {
    path: '/info',
    name: 'info',
    component: InfoView
  },
  {
    path: "*",
    name: "catchAll",
    component: HomeView,
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
