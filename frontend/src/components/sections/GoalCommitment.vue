<template>
  <section id="goal-commitment" class="py-24 bg-brand-card/30 relative overflow-hidden">
    <div class="absolute inset-0 grid-bg opacity-50 pointer-events-none"></div>

    <div class="relative max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <span class="text-brand-cyan text-sm font-semibold uppercase tracking-widest">Our Purpose</span>
        <h2 class="text-4xl md:text-5xl font-black text-white mt-3">Goal & Commitment</h2>
      </div>

      <!-- Mission statement -->
      <div class="max-w-3xl mx-auto text-center mb-20">
        <blockquote class="text-xl md:text-2xl text-gray-300 leading-relaxed font-light">
          "Our goal is to make enterprise-grade cloud security and AI accessible to every organization — empowering businesses to operate with confidence in a world of increasing digital threats."
        </blockquote>
        <cite class="mt-6 block text-brand-cyan font-semibold not-italic">— GO_Digital Mission</cite>
      </div>

      <!-- Commitment pillars -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
        <div
          v-for="c in commitments"
          :key="c.title"
          class="bg-brand-card border border-brand-border rounded-2xl p-8 text-center group hover:border-brand-cyan/50 transition-all"
        >
          <div class="w-16 h-16 rounded-full bg-brand-cyan/10 flex items-center justify-center mx-auto mb-5 group-hover:bg-brand-cyan/20 transition-colors text-2xl">
            {{ c.emoji }}
          </div>
          <h3 class="text-white font-bold text-lg mb-3">{{ c.title }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">{{ c.description }}</p>
        </div>
      </div>

      <!-- Numbers bar -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
        <div v-for="m in metrics" :key="m.label" class="text-center p-6 bg-brand-card border border-brand-border rounded-xl">
          <div class="text-3xl font-black text-brand-cyan">{{ m.value }}</div>
          <div class="text-gray-400 text-xs mt-1">{{ m.label }}</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const commitments = [
  {
    emoji: '🎯',
    title: 'Outcome-Driven',
    description: 'We measure success by your results, not deliverables. Every engagement is anchored to clear, measurable business outcomes.',
  },
  {
    emoji: '🔒',
    title: 'Security First',
    description: 'We never compromise on security. Every solution we deliver meets the highest standards of protection and compliance.',
  },
  {
    emoji: '🌱',
    title: 'Long-term Partnership',
    description: 'We\'re not a vendor — we\'re your strategic technology partner, invested in your long-term success and growth.',
  },
]

const metrics = [
  { value: '500+', label: 'Enterprise Clients' },
  { value: '12+', label: 'Years Experience' },
  { value: '0', label: 'Major Breaches' },
  { value: '4.9★', label: 'Client Rating' },
]
</script>
