import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', component: () => import('@/views/HomeView.vue') },
  { path: '/appointment', component: () => import('@/views/AppointmentView.vue') },
  { path: '/verify-email', component: () => import('@/views/EmailVerifiedView.vue') },
  { path: '/dashboard', component: () => import('@/views/UserDashboardView.vue'), meta: { requiresAuth: true } },
  { path: '/admin', component: () => import('@/views/admin/AdminLoginView.vue') },
  {
    path: '/admin/dashboard',
    component: () => import('@/views/admin/DashboardView.vue'),
    meta: { requiresAdmin: true },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    if (to.hash) return { el: to.hash, behavior: 'smooth' }
    return { top: 0 }
  },
})

router.beforeEach((to) => {
  if (to.meta.requiresAdmin && !localStorage.getItem('adminToken')) return '/admin'
  if (to.meta.requiresAuth && !localStorage.getItem('token')) return '/'
})

export default router
