import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Welcome from './views/Welcome.vue'
import Profile from './views/Profile.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/welcome', component: Welcome },
  { path: '/profile', component: Profile }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
