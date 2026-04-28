<template>
  <footer class="bg-brand-dark border-t border-brand-border">
    <div class="max-w-7xl mx-auto px-6 py-16">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
        <!-- Brand -->
        <div>
          <img src="@/assets/logo.svg" alt="GO_Digital" class="h-10 mb-4" />
          <p class="text-gray-400 text-sm leading-relaxed">
            Empowering businesses with cloud infrastructure, cybersecurity, AI, and digital transformation solutions.
          </p>
          <div class="flex gap-4 mt-6">
            <a v-for="s in socials" :key="s.name" :href="s.url" class="text-gray-500 hover:text-brand-cyan transition-colors" :aria-label="s.name">
              <component :is="s.icon" class="w-5 h-5" />
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="text-white font-semibold mb-4 text-sm uppercase tracking-widest">Navigation</h4>
          <ul class="space-y-2">
            <li v-for="item in navLinks" :key="item.id">
              <a
                href="#"
                @click.prevent="scrollTo(item.id)"
                class="text-gray-400 hover:text-brand-cyan text-sm transition-colors"
              >
                {{ item.label }}
              </a>
            </li>
          </ul>
        </div>

        <!-- Newsletter + Address -->
        <div>
          <h4 class="text-white font-semibold mb-4 text-sm uppercase tracking-widest">Newsletter</h4>
          <p class="text-gray-400 text-sm mb-4">Stay updated on cloud, security & AI innovations.</p>
          <form @submit.prevent="subscribe" class="flex gap-2">
            <input
              v-model="email"
              type="email"
              placeholder="your@email.com"
              class="flex-1 bg-brand-card border border-brand-border rounded-lg px-4 py-2.5 text-sm text-white placeholder-gray-500 focus:outline-none focus:border-brand-cyan transition-colors"
              required
            />
            <button
              type="submit"
              :disabled="loading"
              class="bg-brand-cyan text-brand-dark font-semibold px-4 py-2.5 rounded-lg hover:opacity-90 transition-opacity disabled:opacity-60 text-sm"
            >
              {{ loading ? '...' : 'Join' }}
            </button>
          </form>
          <p v-if="message" :class="success ? 'text-brand-cyan' : 'text-red-400'" class="text-xs mt-2">{{ message }}</p>

          <div class="mt-8">
            <h4 class="text-white font-semibold mb-3 text-sm uppercase tracking-widest">Address</h4>
            <p class="text-gray-400 text-sm leading-relaxed">
              GO_Digital Headquarters<br />
              Innovation District, Tech Hub<br />
              contact@go-digital.com<br />
              +1 (800) GO-DIGITAL
            </p>
          </div>
        </div>
      </div>

      <div class="border-t border-brand-border mt-12 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-gray-500 text-sm">© 2025 GO_Digital. All rights reserved.</p>
        <p class="text-gray-600 text-xs">Cloud · Security · AI · Innovation</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, h } from 'vue'
import api from '@/services/api'

const email = ref('')
const loading = ref(false)
const message = ref('')
const success = ref(false)

const navLinks = [
  { id: 'home', label: 'Home' },
  { id: 'what-we-do', label: 'What We Do' },
  { id: 'our-service', label: 'Our Services' },
  { id: 'goal-commitment', label: 'Goal & Commitment' },
  { id: 'about-us', label: 'About Us' },
]

const socials = [
  { name: 'LinkedIn', url: '#', icon: { render: () => h('svg', { viewBox: '0 0 24 24', fill: 'currentColor' }, [h('path', { d: 'M19 3a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h14m-.5 15.5v-5.3a3.26 3.26 0 00-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 011.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 001.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 00-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z' })]) } },
  { name: 'Twitter', url: '#', icon: { render: () => h('svg', { viewBox: '0 0 24 24', fill: 'currentColor' }, [h('path', { d: 'M22.46 6c-.77.35-1.6.58-2.46.69.88-.53 1.56-1.37 1.88-2.38-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29 0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15 0 1.49.75 2.81 1.91 3.56-.71 0-1.37-.2-1.95-.5v.03c0 2.08 1.48 3.82 3.44 4.21a4.22 4.22 0 01-1.93.07 4.28 4.28 0 004 2.98 8.521 8.521 0 01-5.33 1.84c-.34 0-.68-.02-1.02-.06C3.44 20.29 5.7 21 8.12 21 16 21 20.33 14.46 20.33 8.79c0-.19 0-.37-.01-.56.84-.6 1.56-1.36 2.14-2.23z' })]) } },
]

function scrollTo(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}

async function subscribe() {
  loading.value = true
  message.value = ''
  try {
    await api.post('/newsletter/subscribe', { email: email.value })
    success.value = true
    message.value = 'Subscribed! Check your inbox.'
    email.value = ''
  } catch (err) {
    success.value = false
    message.value = err.response?.data?.detail || 'Subscription failed.'
  } finally {
    loading.value = false
  }
}
</script>
