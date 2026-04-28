<template>
  <div class="min-h-screen bg-brand-dark">
    <!-- Top bar -->
    <header class="bg-brand-card border-b border-brand-border px-6 py-4 flex items-center justify-between">
      <div class="flex items-center gap-4">
        <img src="@/assets/logo.svg" alt="GO_Digital" class="h-8" />
        <span class="text-brand-cyan text-xs font-semibold uppercase tracking-widest border-l border-brand-border pl-4">Admin Dashboard</span>
      </div>
      <div class="flex items-center gap-4">
        <RouterLink to="/" class="text-xs text-gray-400 hover:text-brand-cyan transition-colors">View Site</RouterLink>
        <button @click="logout" class="text-xs text-gray-400 hover:text-red-400 transition-colors">Sign Out</button>
      </div>
    </header>

    <div class="max-w-7xl mx-auto px-6 py-10">
      <!-- Tabs -->
      <div class="flex gap-2 mb-8 border-b border-brand-border">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          class="px-5 py-3 text-sm font-medium transition-all border-b-2 -mb-px"
          :class="activeTab === tab.id
            ? 'text-brand-cyan border-brand-cyan'
            : 'text-gray-400 border-transparent hover:text-white'"
        >
          {{ tab.label }}
          <span v-if="tab.count" class="ml-2 text-xs bg-brand-cyan/10 text-brand-cyan px-2 py-0.5 rounded-full">{{ tab.count }}</span>
        </button>
      </div>

      <!-- Users tab -->
      <div v-if="activeTab === 'users'">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-xl font-bold text-white">Users <span class="text-gray-500 font-normal text-base">({{ users.length }})</span></h2>
          <button @click="loadUsers" class="text-xs text-gray-400 hover:text-brand-cyan transition-colors">↻ Refresh</button>
        </div>
        <div class="bg-brand-card border border-brand-border rounded-2xl overflow-hidden">
          <table class="w-full text-sm">
            <thead>
              <tr class="border-b border-brand-border text-gray-500 text-xs">
                <th class="text-left px-6 py-4 font-medium">Name</th>
                <th class="text-left px-6 py-4 font-medium">Email</th>
                <th class="text-left px-6 py-4 font-medium">Status</th>
                <th class="text-left px-6 py-4 font-medium">Joined</th>
                <th class="text-left px-6 py-4 font-medium">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="users.length === 0"><td colspan="5" class="text-center text-gray-500 py-12">No users yet.</td></tr>
              <tr v-for="u in users" :key="u.id" class="border-b border-brand-border/50 hover:bg-white/2 transition-colors">
                <td class="px-6 py-4 text-white">{{ u.full_name }}</td>
                <td class="px-6 py-4 text-gray-400">{{ u.email }}</td>
                <td class="px-6 py-4">
                  <span class="text-xs px-2 py-1 rounded-full" :class="u.is_verified ? 'bg-green-500/10 text-green-400' : 'bg-yellow-500/10 text-yellow-400'">
                    {{ u.is_verified ? 'Verified' : 'Unverified' }}
                  </span>
                  <span class="ml-2 text-xs px-2 py-1 rounded-full" :class="u.is_active ? 'bg-brand-cyan/10 text-brand-cyan' : 'bg-gray-500/10 text-gray-500'">
                    {{ u.is_active ? 'Active' : 'Inactive' }}
                  </span>
                </td>
                <td class="px-6 py-4 text-gray-500 text-xs">{{ formatDate(u.created_at) }}</td>
                <td class="px-6 py-4">
                  <div class="flex gap-3">
                    <button @click="toggleUser(u)" class="text-xs text-gray-400 hover:text-brand-cyan transition-colors">
                      {{ u.is_active ? 'Deactivate' : 'Activate' }}
                    </button>
                    <button @click="deleteUser(u.id)" class="text-xs text-gray-400 hover:text-red-400 transition-colors">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Newsletter tab -->
      <div v-if="activeTab === 'newsletter'">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-xl font-bold text-white">Newsletter <span class="text-gray-500 font-normal text-base">({{ subscribers.length }})</span></h2>
          <button @click="showBroadcast = true" class="bg-brand-cyan text-brand-dark text-xs font-bold px-4 py-2 rounded-lg hover:opacity-90 transition-opacity">
            Broadcast Email
          </button>
        </div>
        <div class="bg-brand-card border border-brand-border rounded-2xl overflow-hidden">
          <table class="w-full text-sm">
            <thead>
              <tr class="border-b border-brand-border text-gray-500 text-xs">
                <th class="text-left px-6 py-4 font-medium">Email</th>
                <th class="text-left px-6 py-4 font-medium">Subscribed</th>
                <th class="text-left px-6 py-4 font-medium">Status</th>
                <th class="text-left px-6 py-4 font-medium">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="subscribers.length === 0"><td colspan="4" class="text-center text-gray-500 py-12">No subscribers yet.</td></tr>
              <tr v-for="s in subscribers" :key="s.id" class="border-b border-brand-border/50 hover:bg-white/2 transition-colors">
                <td class="px-6 py-4 text-white">{{ s.email }}</td>
                <td class="px-6 py-4 text-gray-500 text-xs">{{ formatDate(s.subscribed_at) }}</td>
                <td class="px-6 py-4">
                  <span class="text-xs px-2 py-1 rounded-full" :class="s.is_active ? 'bg-green-500/10 text-green-400' : 'bg-gray-500/10 text-gray-500'">
                    {{ s.is_active ? 'Active' : 'Inactive' }}
                  </span>
                </td>
                <td class="px-6 py-4">
                  <button @click="removeSub(s.id)" class="text-xs text-gray-400 hover:text-red-400 transition-colors">Remove</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Broadcast modal -->
        <div v-if="showBroadcast" class="fixed inset-0 z-50 flex items-center justify-center p-4" @click.self="showBroadcast = false">
          <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>
          <div class="relative bg-brand-card border border-brand-border rounded-2xl w-full max-w-lg p-8">
            <h3 class="text-white font-bold text-lg mb-6">Send Newsletter Broadcast</h3>
            <div class="space-y-4">
              <input v-model="broadcast.subject" placeholder="Email subject" class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-brand-cyan transition-colors" />
              <textarea v-model="broadcast.content" rows="6" placeholder="Email content (HTML supported)" class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-brand-cyan transition-colors resize-none"></textarea>
              <p v-if="broadcastMsg" class="text-brand-cyan text-xs">{{ broadcastMsg }}</p>
              <div class="flex gap-3">
                <button @click="sendBroadcast" :disabled="broadcastLoading" class="flex-1 bg-brand-cyan text-brand-dark font-bold py-3 rounded-xl hover:opacity-90 disabled:opacity-60 text-sm">
                  {{ broadcastLoading ? 'Sending...' : 'Send to All Subscribers' }}
                </button>
                <button @click="showBroadcast = false" class="px-6 border border-brand-border text-gray-400 rounded-xl hover:border-gray-500 transition-colors text-sm">Cancel</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Appointments tab -->
      <div v-if="activeTab === 'appointments'">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-xl font-bold text-white">Appointments <span class="text-gray-500 font-normal text-base">({{ appointments.length }})</span></h2>
          <div class="flex gap-2">
            <button v-for="f in filters" :key="f" @click="apptFilter = f; loadAppointments()"
              class="text-xs px-3 py-1.5 rounded-lg border transition-colors"
              :class="apptFilter === f ? 'bg-brand-cyan/10 border-brand-cyan text-brand-cyan' : 'border-brand-border text-gray-400 hover:border-gray-500'">
              {{ f || 'All' }}
            </button>
          </div>
        </div>

        <div class="space-y-4">
          <div v-if="appointments.length === 0" class="text-center text-gray-500 py-12">No appointments.</div>
          <div
            v-for="a in appointments"
            :key="a.id"
            class="bg-brand-card border border-brand-border rounded-xl p-6 hover:border-brand-cyan/30 transition-all cursor-pointer"
            @click="selectedAppt = a"
          >
            <div class="flex items-start justify-between gap-4">
              <div>
                <div class="flex items-center gap-3 mb-1">
                  <h4 class="text-white font-semibold">{{ a.name }}</h4>
                  <span class="text-xs px-2 py-0.5 rounded-full font-medium"
                    :class="{
                      'bg-yellow-500/10 text-yellow-400': a.status === 'pending',
                      'bg-green-500/10 text-green-400': a.status === 'confirmed',
                      'bg-red-500/10 text-red-400': a.status === 'cancelled',
                    }">
                    {{ a.status }}
                  </span>
                </div>
                <p class="text-gray-400 text-sm">{{ a.email }} · {{ a.phone }}</p>
                <p class="text-gray-500 text-xs mt-1">{{ serviceLabel(a.service_type) }} · {{ a.preferred_date }} at {{ a.preferred_time }}</p>
              </div>
              <span class="text-xs text-gray-600">{{ formatDate(a.created_at) }}</span>
            </div>
          </div>
        </div>

        <!-- Appointment detail modal -->
        <div v-if="selectedAppt" class="fixed inset-0 z-50 flex items-center justify-center p-4" @click.self="selectedAppt = null">
          <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>
          <div class="relative bg-brand-card border border-brand-border rounded-2xl w-full max-w-lg p-8 max-h-[90vh] overflow-y-auto">
            <button @click="selectedAppt = null" class="absolute top-4 right-4 text-gray-500 hover:text-white">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
            <h3 class="text-white font-bold text-lg mb-6">Appointment Details</h3>
            <div class="space-y-3 text-sm mb-6">
              <div class="flex gap-4"><span class="text-gray-500 w-28 flex-shrink-0">Name</span><span class="text-white">{{ selectedAppt.name }}</span></div>
              <div class="flex gap-4"><span class="text-gray-500 w-28 flex-shrink-0">Email</span><span class="text-white">{{ selectedAppt.email }}</span></div>
              <div class="flex gap-4"><span class="text-gray-500 w-28 flex-shrink-0">Phone</span><span class="text-white">{{ selectedAppt.phone }}</span></div>
              <div class="flex gap-4"><span class="text-gray-500 w-28 flex-shrink-0">Service</span><span class="text-white">{{ serviceLabel(selectedAppt.service_type) }}</span></div>
              <div class="flex gap-4"><span class="text-gray-500 w-28 flex-shrink-0">Date</span><span class="text-white">{{ selectedAppt.preferred_date }} at {{ selectedAppt.preferred_time }}</span></div>
              <div v-if="selectedAppt.message" class="flex gap-4"><span class="text-gray-500 w-28 flex-shrink-0">Message</span><span class="text-gray-300">{{ selectedAppt.message }}</span></div>
            </div>

            <div class="space-y-3">
              <div>
                <label class="text-xs text-gray-400 font-medium mb-1.5 block">Update Status</label>
                <select v-model="replyForm.status" class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-brand-cyan transition-colors">
                  <option value="pending">Pending</option>
                  <option value="confirmed">Confirmed</option>
                  <option value="cancelled">Cancelled</option>
                </select>
              </div>
              <div>
                <label class="text-xs text-gray-400 font-medium mb-1.5 block">Reply to Client (sends email)</label>
                <textarea v-model="replyForm.admin_reply" rows="4" placeholder="Your message to the client..."
                  class="w-full bg-brand-dark border border-brand-border rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-brand-cyan transition-colors resize-none"></textarea>
              </div>
              <button @click="updateAppt" :disabled="replyLoading"
                class="w-full bg-brand-cyan text-brand-dark font-bold py-3 rounded-xl hover:opacity-90 disabled:opacity-60 text-sm">
                {{ replyLoading ? 'Saving...' : 'Save & Send Email' }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { useAdminStore } from '@/stores/admin'
import { adminApi } from '@/services/api'

const router = useRouter()
const admin = useAdminStore()

const activeTab = ref('users')
const users = ref([])
const subscribers = ref([])
const appointments = ref([])
const apptFilter = ref('')
const filters = ['', 'pending', 'confirmed', 'cancelled']
const showBroadcast = ref(false)
const broadcast = reactive({ subject: '', content: '' })
const broadcastLoading = ref(false)
const broadcastMsg = ref('')
const selectedAppt = ref(null)
const replyForm = reactive({ status: 'pending', admin_reply: '', send_email: true })
const replyLoading = ref(false)

const tabs = computed(() => [
  { id: 'users', label: 'Users', count: users.value.length },
  { id: 'newsletter', label: 'Newsletter', count: subscribers.value.length },
  { id: 'appointments', label: 'Appointments', count: appointments.value.length },
])

const serviceLabels = {
  'cloud-infra': 'Cloud Infrastructure',
  'cloud-security': 'Cloud Security',
  cybersecurity: 'Cybersecurity',
  ai: 'AI Solutions',
  'ai-security': 'AI Security',
}

function serviceLabel(val) { return serviceLabels[val] || val }
function formatDate(dt) { return new Date(dt).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) }

async function loadUsers() {
  const { data } = await adminApi.get('/admin/users')
  users.value = data
}
async function loadSubscribers() {
  const { data } = await adminApi.get('/newsletter/')
  subscribers.value = data
}
async function loadAppointments() {
  const params = apptFilter.value ? `?status=${apptFilter.value}` : ''
  const { data } = await adminApi.get(`/appointments/${params}`)
  appointments.value = data
}

async function toggleUser(u) {
  await adminApi.patch(`/admin/users/${u.id}?is_active=${!u.is_active}`)
  u.is_active = !u.is_active
}
async function deleteUser(id) {
  if (!confirm('Delete this user?')) return
  await adminApi.delete(`/admin/users/${id}`)
  users.value = users.value.filter(u => u.id !== id)
}
async function removeSub(id) {
  if (!confirm('Remove this subscriber?')) return
  await adminApi.delete(`/newsletter/${id}`)
  subscribers.value = subscribers.value.filter(s => s.id !== id)
}
async function sendBroadcast() {
  broadcastLoading.value = true
  broadcastMsg.value = ''
  try {
    const { data } = await adminApi.post('/newsletter/broadcast', broadcast)
    broadcastMsg.value = `Sent to ${data.sent_to} subscribers!`
    broadcast.subject = ''
    broadcast.content = ''
  } finally {
    broadcastLoading.value = false
  }
}
async function updateAppt() {
  replyLoading.value = true
  try {
    const { data } = await adminApi.patch(`/appointments/${selectedAppt.value.id}`, replyForm)
    const idx = appointments.value.findIndex(a => a.id === data.id)
    if (idx > -1) appointments.value[idx] = data
    selectedAppt.value = null
    replyForm.admin_reply = ''
    replyForm.status = 'pending'
  } finally {
    replyLoading.value = false
  }
}

function logout() {
  admin.logout()
  router.push('/admin')
}

onMounted(() => {
  loadUsers()
  loadSubscribers()
  loadAppointments()
})
</script>
