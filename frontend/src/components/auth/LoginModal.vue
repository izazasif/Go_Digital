<template>
  <div class="fixed inset-0 z-[100] flex items-center justify-center p-4" @click.self="$emit('close')">
    <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>
    <div class="relative bg-brand-card border border-brand-border rounded-2xl w-full max-w-md p-8 shadow-2xl">
      <!-- Close -->
      <button @click="$emit('close')" class="absolute top-4 right-4 text-gray-500 hover:text-white transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>

      <img src="@/assets/logo.svg" alt="GO_Digital" class="h-8 mb-6" />
      <h2 class="text-2xl font-bold text-white mb-1">Welcome back</h2>
      <p class="text-gray-400 text-sm mb-8">Sign in to your GO_Digital account</p>

      <form @submit.prevent="submit" class="space-y-4">
        <div>
          <label class="text-xs text-gray-400 font-medium mb-1.5 block">Email</label>
          <input v-model="form.email" type="email" required placeholder="you@company.com"
            class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-brand-cyan transition-colors" />
        </div>
        <div>
          <label class="text-xs text-gray-400 font-medium mb-1.5 block">Password</label>
          <input v-model="form.password" type="password" required placeholder="••••••••"
            class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-brand-cyan transition-colors" />
        </div>

        <p v-if="error" class="text-red-400 text-xs bg-red-400/10 border border-red-400/20 rounded-lg px-4 py-3">{{ error }}</p>
        <p v-if="success" class="text-brand-cyan text-xs bg-brand-cyan/10 border border-brand-cyan/20 rounded-lg px-4 py-3">{{ success }}</p>

        <button type="submit" :disabled="loading"
          class="w-full bg-brand-cyan text-brand-dark font-bold py-3 rounded-xl hover:opacity-90 transition-opacity disabled:opacity-60 mt-2">
          {{ loading ? 'Signing in...' : 'Sign In' }}
        </button>
      </form>

      <p class="text-center text-sm text-gray-500 mt-6">
        Don't have an account?
        <button @click="$emit('switch-to-signup')" class="text-brand-cyan hover:underline ml-1">Sign up</button>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useAuthStore } from '@/stores/auth'

defineEmits(['close', 'switch-to-signup'])

const auth = useAuthStore()
const form = reactive({ email: '', password: '' })
const loading = ref(false)
const error = ref('')
const success = ref('')

async function submit() {
  loading.value = true
  error.value = ''
  success.value = ''
  try {
    await auth.login(form.email, form.password)
    success.value = 'Signed in successfully!'
    setTimeout(() => emit('close'), 800)
  } catch (err) {
    error.value = err.response?.data?.detail || 'Login failed. Check your credentials.'
  } finally {
    loading.value = false
  }
}
</script>
