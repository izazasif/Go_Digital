<template>
  <div class="min-h-screen bg-brand-dark grid-bg flex items-center justify-center p-6">
    <div class="bg-brand-card border border-brand-border rounded-2xl w-full max-w-md p-10 shadow-2xl">
      <img src="@/assets/logo.svg" alt="GO_Digital" class="h-9 mb-2" />
      <p class="text-brand-cyan text-xs font-semibold uppercase tracking-widest mb-8">Admin Portal</p>

      <h2 class="text-2xl font-bold text-white mb-1">Admin Sign In</h2>
      <p class="text-gray-400 text-sm mb-8">Access the management dashboard</p>

      <form @submit.prevent="submit" class="space-y-4">
        <div>
          <label class="text-xs text-gray-400 font-medium mb-1.5 block">Admin Email</label>
          <input v-model="form.email" type="email" required placeholder="admin@go-digital.com"
            class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-brand-cyan transition-colors" />
        </div>
        <div>
          <label class="text-xs text-gray-400 font-medium mb-1.5 block">Password</label>
          <input v-model="form.password" type="password" required placeholder="••••••••"
            class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-brand-cyan transition-colors" />
        </div>

        <p v-if="error" class="text-red-400 text-xs bg-red-400/10 border border-red-400/20 rounded-lg px-4 py-3">{{ error }}</p>

        <button type="submit" :disabled="loading"
          class="w-full bg-brand-cyan text-brand-dark font-bold py-3 rounded-xl hover:opacity-90 transition-opacity disabled:opacity-60">
          {{ loading ? 'Signing in...' : 'Sign In to Dashboard' }}
        </button>
      </form>

      <div class="mt-8 pt-6 border-t border-brand-border text-center">
        <RouterLink to="/" class="text-sm text-gray-500 hover:text-gray-300 transition-colors">
          ← Back to website
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { useAdminStore } from '@/stores/admin'

const router = useRouter()
const admin = useAdminStore()
const form = reactive({ email: '', password: '' })
const loading = ref(false)
const error = ref('')

async function submit() {
  loading.value = true
  error.value = ''
  try {
    await admin.login(form.email, form.password)
    router.push('/admin/dashboard')
  } catch (err) {
    error.value = err.response?.data?.detail || 'Invalid credentials.'
  } finally {
    loading.value = false
  }
}
</script>
