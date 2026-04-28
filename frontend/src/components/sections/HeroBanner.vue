<template>
  <section id="home" class="relative min-h-screen flex items-center justify-center overflow-hidden grid-bg">
    <!-- Glow orbs -->
    <div class="absolute top-1/4 left-1/4 w-96 h-96 bg-brand-cyan/5 rounded-full blur-3xl animate-pulse-slow pointer-events-none"></div>
    <div class="absolute bottom-1/4 right-1/4 w-80 h-80 bg-blue-600/5 rounded-full blur-3xl animate-pulse-slow pointer-events-none" style="animation-delay:2s"></div>

    <div class="relative max-w-7xl mx-auto px-6 text-center pt-24 pb-16">
      <!-- Badge -->
      <div class="inline-flex items-center gap-2 bg-brand-cyan/10 border border-brand-cyan/30 text-brand-cyan text-xs font-semibold px-4 py-2 rounded-full mb-8 animate-float">
        <span class="w-1.5 h-1.5 bg-brand-cyan rounded-full animate-pulse"></span>
        Cloud · Security · AI Platform
      </div>

      <!-- Headline -->
      <h1 class="text-5xl md:text-7xl font-black leading-tight mb-6">
        <span class="text-white">Secure Your Future</span><br />
        <span class="text-brand-cyan glow-cyan-text">With Digital Intelligence</span>
      </h1>

      <p class="text-gray-400 text-lg md:text-xl max-w-2xl mx-auto mb-10 leading-relaxed">
        Cloud infrastructure, cybersecurity, and AI solutions built for the enterprises that can't afford to fail.
      </p>

      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <button
          @click="scrollTo('our-service')"
          class="bg-brand-cyan text-brand-dark font-bold px-8 py-4 rounded-xl hover:opacity-90 transition-all glow-cyan text-base"
        >
          Explore Services
        </button>
        <button
          @click="scrollTo('what-we-do')"
          class="border border-brand-border text-white font-semibold px-8 py-4 rounded-xl hover:border-brand-cyan hover:text-brand-cyan transition-all text-base"
        >
          Learn More
        </button>
      </div>

      <!-- Stats -->
      <div class="grid grid-cols-3 gap-6 mt-20 max-w-xl mx-auto">
        <div v-for="stat in stats" :key="stat.label" class="text-center">
          <div class="text-3xl font-black text-brand-cyan">{{ stat.value }}</div>
          <div class="text-xs text-gray-500 mt-1">{{ stat.label }}</div>
        </div>
      </div>
    </div>

    <!-- Scroll indicator -->
    <div class="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 text-gray-600 animate-bounce">
      <span class="text-xs">Scroll</span>
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </div>
  </section>
</template>

<script setup>
const stats = [
  { value: '500+', label: 'Clients Secured' },
  { value: '99.9%', label: 'Uptime SLA' },
  { value: '24/7', label: 'Support' },
]

function scrollTo(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}
</script>
