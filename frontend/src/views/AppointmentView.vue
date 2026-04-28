<template>
  <div class="min-h-screen bg-brand-dark grid-bg">
    <!-- Header bar -->
    <div class="bg-brand-dark/95 border-b border-brand-border px-6 py-4 flex items-center gap-4">
      <RouterLink to="/" class="text-gray-400 hover:text-brand-cyan transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
        </svg>
      </RouterLink>
      <img src="@/assets/logo.svg" alt="GO_Digital" class="h-8" />
    </div>

    <div class="max-w-2xl mx-auto px-6 py-16">
      <!-- Success state -->
      <div v-if="submitted" class="text-center py-16">
        <div class="w-20 h-20 rounded-full bg-brand-cyan/10 border border-brand-cyan/30 flex items-center justify-center mx-auto mb-6 text-4xl">✅</div>
        <h2 class="text-3xl font-black text-white mb-3">Appointment Requested!</h2>
        <p class="text-gray-400 leading-relaxed mb-8">
          We've received your request and sent a confirmation to <span class="text-brand-cyan">{{ form.email }}</span>. Our team will get back to you within 1 business day.
        </p>
        <RouterLink to="/" class="bg-brand-cyan text-brand-dark font-bold px-8 py-3 rounded-xl hover:opacity-90 transition-opacity inline-block">
          Back to Home
        </RouterLink>
      </div>

      <!-- Form -->
      <div v-else>
        <span class="text-brand-cyan text-sm font-semibold uppercase tracking-widest">Book a Session</span>
        <h1 class="text-4xl font-black text-white mt-2 mb-2">Schedule an Appointment</h1>
        <p class="text-gray-400 mb-10">Fill in your details and we'll be in touch to confirm your session.</p>

        <form @submit.prevent="submit" class="space-y-5">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
            <div>
              <label class="text-xs text-gray-400 font-medium mb-1.5 block">Full Name *</label>
              <input v-model="form.name" type="text" required placeholder="Jane Smith"
                class="input-field" />
            </div>
            <div>
              <label class="text-xs text-gray-400 font-medium mb-1.5 block">Email *</label>
              <input v-model="form.email" type="email" required placeholder="you@company.com"
                class="input-field" />
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
            <div>
              <label class="text-xs text-gray-400 font-medium mb-1.5 block">Phone *</label>
              <input v-model="form.phone" type="tel" required placeholder="+1 (555) 000-0000"
                class="input-field" />
            </div>
            <div>
              <label class="text-xs text-gray-400 font-medium mb-1.5 block">Service *</label>
              <select v-model="form.service_type" required class="input-field">
                <option value="" disabled>Select a service</option>
                <option v-for="s in services" :key="s.value" :value="s.value">{{ s.label }}</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
            <div>
              <label class="text-xs text-gray-400 font-medium mb-1.5 block">Preferred Date *</label>
              <input v-model="form.preferred_date" type="date" required :min="today" class="input-field" />
            </div>
            <div>
              <label class="text-xs text-gray-400 font-medium mb-1.5 block">Preferred Time *</label>
              <select v-model="form.preferred_time" required class="input-field">
                <option value="" disabled>Select time slot</option>
                <option v-for="t in timeSlots" :key="t" :value="t">{{ t }}</option>
              </select>
            </div>
          </div>

          <div>
            <label class="text-xs text-gray-400 font-medium mb-1.5 block">Message / Notes</label>
            <textarea v-model="form.message" rows="4" placeholder="Tell us about your project, goals, or any specific concerns..."
              class="input-field resize-none"></textarea>
          </div>

          <p v-if="error" class="text-red-400 text-xs bg-red-400/10 border border-red-400/20 rounded-lg px-4 py-3">{{ error }}</p>

          <button type="submit" :disabled="loading"
            class="w-full bg-brand-cyan text-brand-dark font-bold py-4 rounded-xl hover:opacity-90 transition-opacity disabled:opacity-60 text-base">
            {{ loading ? 'Submitting...' : 'Book Appointment' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import api from '@/services/api'

const route = useRoute()
const submitted = ref(false)
const loading = ref(false)
const error = ref('')

const today = new Date().toISOString().split('T')[0]

const services = [
  { value: 'cloud-infra', label: 'Cloud Infrastructure' },
  { value: 'cloud-security', label: 'Cloud Security' },
  { value: 'cybersecurity', label: 'Cybersecurity' },
  { value: 'ai', label: 'AI Solutions' },
  { value: 'ai-security', label: 'AI Security' },
]

const timeSlots = ['09:00 AM', '10:00 AM', '11:00 AM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM']

const form = reactive({
  name: '',
  email: '',
  phone: '',
  service_type: route.query.service || '',
  preferred_date: '',
  preferred_time: '',
  message: '',
})

async function submit() {
  loading.value = true
  error.value = ''
  try {
    await api.post('/appointments/', form)
    submitted.value = true
  } catch (err) {
    error.value = err.response?.data?.detail || 'Submission failed. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.input-field {
  @apply w-full bg-brand-card border border-brand-border rounded-xl px-4 py-3 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-brand-cyan transition-colors;
}
.input-field option {
  background: #111827;
}
</style>
