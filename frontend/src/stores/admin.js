import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { adminApi } from '@/services/api'

export const useAdminStore = defineStore('admin', () => {
  const token = ref(localStorage.getItem('adminToken') || null)
  const isLoggedIn = computed(() => !!token.value)

  async function login(email, password) {
    const { data } = await adminApi.post('/admin/login', { email, password })
    token.value = data.access_token
    localStorage.setItem('adminToken', data.access_token)
  }

  function logout() {
    token.value = null
    localStorage.removeItem('adminToken')
  }

  return { token, isLoggedIn, login, logout }
})
