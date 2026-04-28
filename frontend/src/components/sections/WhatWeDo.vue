<template>
  <section id="what-we-do" class="py-24 bg-brand-card/30">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <span class="text-brand-cyan text-sm font-semibold uppercase tracking-widest">Our Approach</span>
        <h2 class="text-4xl md:text-5xl font-black text-white mt-3">What We Do</h2>
        <p class="text-gray-400 mt-4 max-w-xl mx-auto">
          We bridge the gap between cutting-edge technology and business resilience — delivering integrated platforms that protect, scale, and innovate.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div
          v-for="item in pillars"
          :key="item.title"
          class="bg-brand-card border border-brand-border rounded-2xl p-8 hover:border-brand-cyan/50 transition-all duration-300 group"
        >
          <div class="w-14 h-14 rounded-xl bg-brand-cyan/10 flex items-center justify-center mb-6 group-hover:bg-brand-cyan/20 transition-colors">
            <span class="text-2xl">{{ item.emoji }}</span>
          </div>
          <h3 class="text-white font-bold text-xl mb-3">{{ item.title }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">{{ item.description }}</p>
        </div>
      </div>

      <!-- Process steps -->
      <div class="mt-20 grid grid-cols-1 md:grid-cols-4 gap-6">
        <div v-for="(step, i) in steps" :key="step.title" class="text-center relative">
          <div class="w-10 h-10 rounded-full bg-brand-cyan/10 border border-brand-cyan/30 flex items-center justify-center text-brand-cyan font-bold text-sm mx-auto mb-4">
            {{ i + 1 }}
          </div>
          <h4 class="text-white font-semibold mb-2">{{ step.title }}</h4>
          <p class="text-gray-500 text-xs">{{ step.desc }}</p>
          <div v-if="i < steps.length - 1" class="hidden md:block absolute top-5 left-[60%] w-[80%] h-px bg-gradient-to-r from-brand-cyan/30 to-transparent"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const pillars = [
  {
    emoji: '☁️',
    title: 'Cloud-First Architecture',
    description: 'We design and deploy scalable cloud environments on AWS, Azure, and GCP — optimized for performance, cost, and resilience from day one.',
  },
  {
    emoji: '🛡️',
    title: 'Security by Default',
    description: 'Every solution ships with enterprise-grade cybersecurity baked in — zero-trust networking, threat detection, and compliance frameworks.',
  },
  {
    emoji: '🤖',
    title: 'AI-Powered Intelligence',
    description: 'We integrate AI and machine learning to automate threat response, optimize infrastructure, and unlock business insights at scale.',
  },
]

const steps = [
  { title: 'Assess', desc: 'Audit your current infrastructure and security posture' },
  { title: 'Design', desc: 'Architect a tailored cloud and security strategy' },
  { title: 'Deploy', desc: 'Implement with zero-downtime delivery pipelines' },
  { title: 'Monitor', desc: 'Continuous 24/7 monitoring, response and optimization' },
]
</script>
