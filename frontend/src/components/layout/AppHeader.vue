<template>
  <header
    class="fixed top-0 left-0 right-0 z-50 transition-all duration-300"
    :class="scrolled ? 'bg-brand-dark/95 backdrop-blur-md border-b border-brand-border shadow-lg' : 'bg-transparent'"
  >
    <div class="max-w-7xl mx-auto px-6 flex items-center justify-between h-16">
      <!-- Logo -->
      <a href="#home" @click.prevent="scrollTo('home')">
        <img src="@/assets/logo.svg" alt="GO_Digital" class="h-9" />
      </a>

      <!-- Desktop Nav -->
      <nav class="hidden md:flex items-center gap-8">
        <a
          v-for="item in navItems"
          :key="item.id"
          href="#"
          @click.prevent="scrollTo(item.id)"
          class="text-sm font-medium text-gray-300 hover:text-brand-cyan transition-colors duration-200 relative group"
        >
          {{ item.label }}
          <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-brand-cyan transition-all duration-300 group-hover:w-full"></span>
        </a>
      </nav>

      <!-- Auth buttons -->
      <div class="hidden md:flex items-center gap-3">
        <template v-if="auth.isLoggedIn">
          <span class="text-sm text-gray-400">Hi, {{ auth.user?.full_name?.split(' ')[0] || 'User' }}</span>
          <router-link
            to="/dashboard"
            class="text-sm font-medium text-gray-300 hover:text-brand-cyan transition-colors px-4 py-2"
          >
            Dashboard
          </router-link>
          <button
            @click="handleLogout"
            class="text-sm font-semibold border border-brand-border text-gray-300 hover:border-brand-cyan hover:text-brand-cyan px-5 py-2 rounded-lg transition-colors"
          >
            Logout
          </button>
        </template>
        <template v-else>
          <button
            @click="$emit('open-login')"
            class="text-sm font-medium text-gray-300 hover:text-brand-cyan transition-colors px-4 py-2"
          >
            Login
          </button>
          <button
            @click="$emit('open-signup')"
            class="text-sm font-semibold bg-brand-cyan text-brand-dark px-5 py-2 rounded-lg hover:opacity-90 transition-opacity"
          >
            Sign Up
          </button>
        </template>
      </div>

      <!-- Mobile menu toggle -->
      <button class="md:hidden text-gray-300 hover:text-white" @click="mobileOpen = !mobileOpen">
        <svg v-if="!mobileOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
        <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
    </div>

    <!-- Mobile menu -->
    <Transition name="slide">
      <div v-if="mobileOpen" class="md:hidden bg-brand-dark/98 border-b border-brand-border px-6 pb-6">
        <nav class="flex flex-col gap-4 pt-4">
          <a
            v-for="item in navItems"
            :key="item.id"
            href="#"
            @click.prevent="scrollTo(item.id); mobileOpen = false"
            class="text-gray-300 hover:text-brand-cyan transition-colors py-1"
          >
            {{ item.label }}
          </a>
        </nav>
        <div class="flex gap-3 mt-4 pt-4 border-t border-brand-border">
          <template v-if="auth.isLoggedIn">
            <router-link to="/dashboard" @click="mobileOpen = false" class="flex-1 py-2 text-sm text-center text-gray-300 border border-brand-border rounded-lg hover:border-brand-cyan transition-colors">Dashboard</router-link>
            <button @click="handleLogout; mobileOpen = false" class="flex-1 py-2 text-sm font-semibold bg-brand-cyan text-brand-dark rounded-lg hover:opacity-90 transition-opacity">Logout</button>
          </template>
          <template v-else>
            <button @click="$emit('open-login'); mobileOpen = false" class="flex-1 py-2 text-sm text-gray-300 border border-brand-border rounded-lg hover:border-brand-cyan transition-colors">Login</button>
            <button @click="$emit('open-signup'); mobileOpen = false" class="flex-1 py-2 text-sm font-semibold bg-brand-cyan text-brand-dark rounded-lg hover:opacity-90 transition-opacity">Sign Up</button>
          </template>
        </div>
      </div>
    </Transition>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

defineEmits(['open-login', 'open-signup'])

const auth = useAuthStore()
const router = useRouter()
const scrolled = ref(false)
const mobileOpen = ref(false)

function handleLogout() {
  auth.logout()
  router.push('/')
}

const navItems = [
  { id: 'home', label: 'Home' },
  { id: 'what-we-do', label: 'What We Do' },
  { id: 'our-service', label: 'Our Services' },
  { id: 'goal-commitment', label: 'Goal & Commitment' },
  { id: 'about-us', label: 'About Us' },
]

function scrollTo(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}

function onScroll() {
  scrolled.value = window.scrollY > 20
}

onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<style scoped>
.slide-enter-active, .slide-leave-active { transition: all 0.25s ease; }
.slide-enter-from, .slide-leave-to { opacity: 0; transform: translateY(-8px); }
</style>
