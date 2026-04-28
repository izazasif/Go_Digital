<template>
  <div class="min-h-screen bg-brand-dark">
    <AppHeader @open-login="showLogin = true" @open-signup="showSignup = true" />

    <main class="max-w-5xl mx-auto px-6 pt-28 pb-20">

      <!-- Profile card -->
      <div class="bg-brand-card border border-brand-border rounded-2xl p-6 mb-8 flex items-center gap-5">
        <div class="w-16 h-16 rounded-full bg-brand-cyan/10 border-2 border-brand-cyan flex items-center justify-center text-brand-cyan text-2xl font-bold flex-shrink-0">
          {{ initials }}
        </div>
        <div class="flex-1 min-w-0">
          <h1 class="text-white text-xl font-bold truncate">{{ auth.user?.full_name }}</h1>
          <p class="text-gray-400 text-sm truncate">{{ auth.user?.email }}</p>
        </div>
        <div class="flex-shrink-0">
          <span v-if="auth.user?.is_verified" class="flex items-center gap-1.5 text-xs font-semibold text-emerald-400 bg-emerald-400/10 border border-emerald-400/20 rounded-full px-3 py-1">
            <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            Verified
          </span>
          <span v-else class="flex items-center gap-1.5 text-xs font-semibold text-yellow-400 bg-yellow-400/10 border border-yellow-400/20 rounded-full px-3 py-1">
            <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
            Unverified
          </span>
        </div>
      </div>

      <!-- Tabs -->
      <div class="flex gap-2 mb-6 border-b border-brand-border">
        <button
          v-for="tab in tabs" :key="tab.id"
          @click="activeTab = tab.id"
          class="px-5 py-3 text-sm font-medium transition-colors relative"
          :class="activeTab === tab.id ? 'text-brand-cyan' : 'text-gray-400 hover:text-gray-200'"
        >
          {{ tab.label }}
          <span v-if="activeTab === tab.id" class="absolute bottom-0 left-0 right-0 h-0.5 bg-brand-cyan rounded-t"></span>
        </button>
      </div>

      <!-- Tab: Appointments -->
      <div v-if="activeTab === 'appointments'">
        <div v-if="loadingAppts" class="text-center py-16 text-gray-500">Loading appointments…</div>

        <div v-else-if="appointments.length === 0" class="text-center py-16">
          <svg class="w-12 h-12 text-gray-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          <p class="text-gray-400">No appointments yet.</p>
          <router-link to="/appointment" class="inline-block mt-4 text-brand-cyan text-sm hover:underline">Book your first appointment →</router-link>
        </div>

        <div v-else class="space-y-4">
          <div
            v-for="appt in appointments" :key="appt.id"
            class="bg-brand-card border border-brand-border rounded-xl p-5 hover:border-gray-600 transition-colors"
          >
            <div class="flex items-start justify-between gap-4 flex-wrap">
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <span class="text-white font-semibold">{{ serviceLabel(appt.service_type) }}</span>
                  <span :class="statusClass(appt.status)" class="text-xs font-semibold px-2.5 py-0.5 rounded-full">
                    {{ appt.status.toUpperCase() }}
                  </span>
                </div>
                <p class="text-gray-400 text-sm">{{ appt.preferred_date }} at {{ appt.preferred_time }}</p>
                <p v-if="appt.message" class="text-gray-500 text-sm mt-1 italic">"{{ appt.message }}"</p>
              </div>
              <span class="text-gray-600 text-xs flex-shrink-0">{{ formatDate(appt.created_at) }}</span>
            </div>

            <!-- Admin reply -->
            <div v-if="appt.admin_reply" class="mt-4 bg-brand-dark rounded-lg p-4 border border-brand-border">
              <p class="text-xs text-gray-500 uppercase tracking-widest mb-1">Team Reply</p>
              <p class="text-gray-300 text-sm">{{ appt.admin_reply }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Tab: Notifications -->
      <div v-if="activeTab === 'notifications'">
        <div class="space-y-3">
          <div
            v-for="note in notifications" :key="note.id"
            class="bg-brand-card border border-brand-border rounded-xl p-4 flex items-start gap-4"
          >
            <div class="w-9 h-9 rounded-full flex items-center justify-center flex-shrink-0" :class="note.iconBg">
              <svg class="w-4 h-4" :class="note.iconColor" fill="currentColor" viewBox="0 0 20 20">
                <path :d="note.icon"/>
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-white text-sm font-medium">{{ note.title }}</p>
              <p class="text-gray-400 text-sm mt-0.5">{{ note.body }}</p>
            </div>
            <span class="text-gray-600 text-xs flex-shrink-0">{{ note.time }}</span>
          </div>
        </div>
      </div>

    </main>

    <LoginModal v-if="showLogin" @close="showLogin = false" @switch-to-signup="showLogin = false; showSignup = true" />
    <SignupModal v-if="showSignup" @close="showSignup = false" @switch-to-login="showSignup = false; showLogin = true" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import api from '@/services/api'
import AppHeader from '@/components/layout/AppHeader.vue'
import LoginModal from '@/components/auth/LoginModal.vue'
import SignupModal from '@/components/auth/SignupModal.vue'

const auth = useAuthStore()
const router = useRouter()
const showLogin = ref(false)
const showSignup = ref(false)
const activeTab = ref('appointments')
const appointments = ref([])
const loadingAppts = ref(true)

const tabs = [
  { id: 'appointments', label: 'My Appointments' },
  { id: 'notifications', label: 'Notifications' },
]

const initials = computed(() => {
  const name = auth.user?.full_name || ''
  return name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2) || '?'
})

const serviceLabels = {
  'cloud-infra': 'Cloud Infrastructure',
  'cloud-security': 'Cloud Security',
  'cybersecurity': 'Cybersecurity',
  'ai': 'AI Solutions',
  'ai-security': 'AI Security',
}

function serviceLabel(val) { return serviceLabels[val] || val }

function statusClass(status) {
  return {
    pending: 'text-yellow-400 bg-yellow-400/10 border border-yellow-400/20',
    confirmed: 'text-emerald-400 bg-emerald-400/10 border border-emerald-400/20',
    cancelled: 'text-red-400 bg-red-400/10 border border-red-400/20',
  }[status] || ''
}

function formatDate(dt) {
  return new Date(dt).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

const notifications = computed(() => {
  const notes = []
  if (auth.user) {
    notes.push({
      id: 1,
      title: 'Account created',
      body: `Welcome to GO_Digital, ${auth.user.full_name}! Your account was successfully created.`,
      time: formatDate(auth.user.created_at),
      icon: 'M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z',
      iconBg: 'bg-brand-cyan/10',
      iconColor: 'text-brand-cyan',
    })
    if (auth.user.is_verified) {
      notes.push({
        id: 2,
        title: 'Email verified',
        body: 'Your email address has been verified. You have full access to GO_Digital.',
        time: '',
        icon: 'M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z',
        iconBg: 'bg-emerald-400/10',
        iconColor: 'text-emerald-400',
      })
    } else {
      notes.push({
        id: 2,
        title: 'Verify your email',
        body: 'A verification link was sent to your inbox. Please verify to unlock all features.',
        time: '',
        icon: 'M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884zM18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z',
        iconBg: 'bg-yellow-400/10',
        iconColor: 'text-yellow-400',
      })
    }
  }
  appointments.value.forEach(appt => {
    notes.push({
      id: `appt-${appt.id}`,
      title: `Appointment ${appt.status}`,
      body: `Your ${serviceLabel(appt.service_type)} appointment on ${appt.preferred_date} is ${appt.status}.`,
      time: formatDate(appt.created_at),
      icon: 'M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z',
      iconBg: appt.status === 'confirmed' ? 'bg-emerald-400/10' : appt.status === 'cancelled' ? 'bg-red-400/10' : 'bg-brand-cyan/10',
      iconColor: appt.status === 'confirmed' ? 'text-emerald-400' : appt.status === 'cancelled' ? 'text-red-400' : 'text-brand-cyan',
    })
  })
  return notes
})

onMounted(async () => {
  if (!auth.isLoggedIn) { router.push('/'); return }
  await auth.fetchMe()
  try {
    const { data } = await api.get('/appointments/my', {
      headers: { Authorization: `Bearer ${auth.token}` }
    })
    appointments.value = data
  } catch {
    appointments.value = []
  } finally {
    loadingAppts.value = false
  }
})
</script>
