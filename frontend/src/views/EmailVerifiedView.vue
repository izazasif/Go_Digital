<template>
  <div class="min-h-screen bg-brand-dark grid-bg flex items-center justify-center p-6">
    <div class="bg-brand-card border border-brand-border rounded-2xl p-12 max-w-md w-full text-center">
      <img src="@/assets/logo.svg" alt="GO_Digital" class="h-9 mx-auto mb-8" />

      <div v-if="loading" class="text-gray-400">Verifying your email...</div>

      <div v-else-if="success">
        <div class="w-16 h-16 rounded-full bg-brand-cyan/10 border border-brand-cyan/30 flex items-center justify-center mx-auto mb-5 text-3xl">✅</div>
        <h2 class="text-2xl font-bold text-white mb-3">Email Verified!</h2>
        <p class="text-gray-400 text-sm mb-8">Your account is now active. You can log in to GO_Digital.</p>
        <RouterLink to="/" class="bg-brand-cyan text-brand-dark font-bold px-8 py-3 rounded-xl hover:opacity-90 transition-opacity inline-block">
          Go to Homepage
        </RouterLink>
      </div>

      <div v-else>
        <div class="w-16 h-16 rounded-full bg-red-500/10 border border-red-500/30 flex items-center justify-center mx-auto mb-5 text-3xl">❌</div>
        <h2 class="text-2xl font-bold text-white mb-3">Verification Failed</h2>
        <p class="text-gray-400 text-sm mb-8">{{ error }}</p>
        <RouterLink to="/" class="text-brand-cyan hover:underline text-sm">Return to homepage</RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import api from '@/services/api'

const route = useRoute()
const loading = ref(true)
const success = ref(false)
const error = ref('')

onMounted(async () => {
  const token = route.query.token
  if (!token) {
    loading.value = false
    error.value = 'No verification token found.'
    return
  }
  try {
    await api.get(`/auth/verify-email?token=${token}`)
    success.value = true
  } catch (err) {
    error.value = err.response?.data?.detail || 'Invalid or expired token.'
  } finally {
    loading.value = false
  }
})
</script>
