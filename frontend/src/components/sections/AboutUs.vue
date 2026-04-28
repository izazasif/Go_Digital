<template>
  <section id="about-us" class="py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <!-- Left: content -->
        <div>
          <span class="text-brand-cyan text-sm font-semibold uppercase tracking-widest">Who We Are</span>
          <h2 class="text-4xl md:text-5xl font-black text-white mt-3 mb-6">About GO_Digital</h2>
          <p class="text-gray-400 leading-relaxed mb-5">
            GO_Digital was founded with a singular mission: to bring Fortune 500-level digital security and cloud capabilities to businesses of all sizes. We are a team of engineers, security experts, and AI researchers who've spent careers defending critical infrastructure.
          </p>
          <p class="text-gray-400 leading-relaxed mb-8">
            From hyper-scalable cloud deployments to AI-powered threat hunting, we build systems that businesses rely on when the stakes are highest. Our customers operate in finance, healthcare, government, and high-growth tech — sectors where downtime and breaches are simply not an option.
          </p>

          <div class="flex flex-wrap gap-3">
            <span v-for="tag in tags" :key="tag" class="bg-brand-cyan/10 border border-brand-cyan/20 text-brand-cyan text-xs font-medium px-4 py-2 rounded-full">
              {{ tag }}
            </span>
          </div>
        </div>

        <!-- Right: visual card stack -->
        <div class="space-y-4">
          <div
            v-for="(item, i) in highlights"
            :key="item.title"
            class="bg-brand-card border border-brand-border rounded-xl p-6 flex items-start gap-5 hover:border-brand-cyan/40 transition-all"
            :style="`animation-delay: ${i * 100}ms`"
          >
            <div class="w-12 h-12 rounded-xl bg-brand-cyan/10 flex items-center justify-center flex-shrink-0 text-xl">
              {{ item.emoji }}
            </div>
            <div>
              <h4 class="text-white font-semibold mb-1">{{ item.title }}</h4>
              <p class="text-gray-400 text-sm">{{ item.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const tags = ['Cloud Native', 'Zero Trust', 'AI-Powered', 'Compliant', 'Always-On', 'Global']

const highlights = [
  {
    emoji: '🌍',
    title: 'Global Operations',
    description: 'Serving clients across 30+ countries with regional cloud deployments and 24/7 follow-the-sun support.',
  },
  {
    emoji: '🏆',
    title: 'Industry Recognition',
    description: 'Recognized by Gartner, Forrester, and leading cybersecurity bodies for innovation in cloud and AI security.',
  },
  {
    emoji: '👥',
    title: 'Expert Team',
    description: '200+ certified engineers, ethical hackers, and AI specialists with deep domain expertise.',
  },
  {
    emoji: '⚡',
    title: 'Rapid Deployment',
    description: 'Our DevSecOps pipelines deliver production-ready solutions in days, not months.',
  },
]
</script>
