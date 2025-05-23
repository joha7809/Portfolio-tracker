import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Welcome from './views/Welcome.vue'
import Profile from './views/Profile.vue'
import TheWelcome from './components/TheWelcome.vue'
import Login from './views/Login.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/welcome', component: TheWelcome },
  { path: '/profile', component: Profile },
  {path: '/login', component: Login},
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
