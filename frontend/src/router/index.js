import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ComposeView from '../views/ComposeView.vue'
import SentView from '../views/SentView.vue'
import ErrorView from '../views/ErrorView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'

import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/compose',
    name: 'compose',
    component: ComposeView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/sent',
    name: 'sent',
    component: SentView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  { path: '/:pathMatch(.*)*', name: 'not-found', component: ErrorView }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
