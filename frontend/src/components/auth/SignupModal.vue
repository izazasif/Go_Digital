<template>
  <div class="fixed inset-0 z-[100] flex items-center justify-center p-4" @click.self="$emit('close')">
    <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>
    <div class="relative bg-brand-card border border-brand-border rounded-2xl w-full max-w-md p-8 shadow-2xl">
      <button @click="$emit('close')" class="absolute top-4 right-4 text-gray-500 hover:text-white transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>

      <img src="@/assets/logo.svg" alt="GO_Digital" class="h-8 mb-6" />

      <div v-if="!registered">
        <h2 class="text-2xl font-bold text-white mb-1">Create account</h2>
        <p class="text-gray-400 text-sm mb-8">Join GO_Digital today</p>

        <form @submit.prevent="submit" class="space-y-4">
          <div>
            <label class="text-xs text-gray-400 font-medium mb-1.5 block">Full Name</label>
            <input v-model="form.full_name" type="text" required placeholder="Jane Smith"
              class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-brand-cyan transition-colors" />
          </div>
          <div>
            <label class="text-xs text-gray-400 font-medium mb-1.5 block">Email</label>
            <input v-model="form.email" type="email" required placeholder="you@company.com"
              class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-brand-cyan transition-colors" />
          </div>
          <div>
            <label class="text-xs text-gray-400 font-medium mb-1.5 block">Password</label>
            <input v-model="form.password" type="password" required placeholder="Min. 8 characters"
              minlength="8"
              class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-brand-cyan transition-colors" />
          </div>

          <p v-if="error" class="text-red-400 text-xs bg-red-400/10 border border-red-400/20 rounded-lg px-4 py-3">{{ error }}</p>

          <button type="submit" :disabled="loading"
            class="w-full bg-brand-cyan text-brand-dark font-bold py-3 rounded-xl hover:opacity-90 transition-opacity disabled:opacity-60 mt-2">
            {{ loading ? 'Creating account...' : 'Create Account' }}
          </button>
        </form>
      </div>

      <!-- Success state -->
      <div v-else class="text-center py-6">
        <div class="w-16 h-16 rounded-full bg-brand-cyan/10 border border-brand-cyan/30 flex items-center justify-center mx-auto mb-5 text-3xl">✉️</div>
        <h3 class="text-white font-bold text-xl mb-3">Check your email</h3>
        <p class="text-gray-400 text-sm leading-relaxed">
          We sent a verification link to <span class="text-brand-cyan">{{ form.email }}</span>.<br />Click the link to activate your account.
        </p>
        <button @click="$emit('close')" class="mt-6 text-sm text-gray-500 hover:text-white transition-colors">Close</button>
      </div>

      <p v-if="!registered" class="text-center text-sm text-gray-500 mt-6">
        Already have an account?
        <button @click="$emit('switch-to-login')" class="text-brand-cyan hover:underline ml-1">Sign in</button>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useAuthStore } from '@/stores/auth'

defineEmits(['close', 'switch-to-login'])

const auth = useAuthStore()
const form = reactive({ full_name: '', email: '', password: '' })
const loading = ref(false)
const error = ref('')
const registered = ref(false)

async function submit() {
  loading.value = true
  error.value = ''
  try {
    await auth.register(form.full_name, form.email, form.password)
    registered.value = true
  } catch (err) {
    error.value = err.response?.data?.detail || 'Registration failed. Try again.'
  } finally {
    loading.value = false
  }
}
</script>
