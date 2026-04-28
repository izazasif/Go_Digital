<template>
  <section id="our-service" class="py-24">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center mb-16">
        <span class="text-brand-cyan text-sm font-semibold uppercase tracking-widest">What We Offer</span>
        <h2 class="text-4xl md:text-5xl font-black text-white mt-3">Our Services</h2>
        <p class="text-gray-400 mt-4 max-w-xl mx-auto">
          Comprehensive digital solutions for modern enterprises — from infrastructure to intelligence.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="service in services"
          :key="service.id"
          class="bg-brand-card border border-brand-border rounded-2xl p-8 hover:border-brand-cyan/50 hover:-translate-y-1 transition-all duration-300 group flex flex-col"
        >
          <div class="w-16 h-16 rounded-2xl flex items-center justify-center mb-6 text-3xl" :class="service.bg">
            {{ service.emoji }}
          </div>
          <h3 class="text-white font-bold text-xl mb-3">{{ service.title }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed flex-1">{{ service.description }}</p>

          <ul class="mt-5 space-y-2">
            <li v-for="feat in service.features" :key="feat" class="flex items-center gap-2 text-xs text-gray-500">
              <span class="w-1 h-1 bg-brand-cyan rounded-full flex-shrink-0"></span>
              {{ feat }}
            </li>
          </ul>

          <RouterLink
            :to="`/appointment?service=${service.id}`"
            class="mt-8 w-full py-3 text-center text-sm font-semibold border border-brand-cyan/40 text-brand-cyan rounded-xl hover:bg-brand-cyan hover:text-brand-dark transition-all duration-200"
          >
            Book Appointment
          </RouterLink>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { RouterLink } from 'vue-router'

const services = [
  {
    id: 'cloud-infra',
    emoji: '☁️',
    bg: 'bg-blue-500/10',
    title: 'Cloud Infrastructure',
    description: 'Design, deploy, and manage scalable cloud architectures that grow with your business — fully automated and cost-optimized.',
    features: ['Multi-cloud deployments', 'Infrastructure as Code', 'Auto-scaling & load balancing', 'Cost optimization'],
  },
  {
    id: 'cloud-security',
    emoji: '🔐',
    bg: 'bg-indigo-500/10',
    title: 'Cloud Security',
    description: 'Protect your cloud environments with enterprise-grade security controls, continuous monitoring, and compliance management.',
    features: ['Zero-trust architecture', 'SIEM & log management', 'Cloud posture management', 'Compliance (SOC2, ISO27001)'],
  },
  {
    id: 'cybersecurity',
    emoji: '🛡️',
    bg: 'bg-red-500/10',
    title: 'Cybersecurity',
    description: 'End-to-end cybersecurity services covering threat detection, incident response, penetration testing, and security operations.',
    features: ['SOC as a service', 'Penetration testing', 'Threat intelligence', 'Incident response'],
  },
  {
    id: 'ai',
    emoji: '🤖',
    bg: 'bg-brand-cyan/10',
    title: 'AI Solutions',
    description: 'Build intelligent automation, predictive analytics, and machine learning systems tailored to your business outcomes.',
    features: ['ML model development', 'AI-powered automation', 'Predictive analytics', 'Natural language processing'],
  },
  {
    id: 'ai-security',
    emoji: '🧠',
    bg: 'bg-purple-500/10',
    title: 'AI Security',
    description: 'Secure your AI/ML systems against adversarial attacks, model poisoning, and data leakage with our specialized AI security framework.',
    features: ['Adversarial robustness', 'Model integrity monitoring', 'AI governance & audit', 'Secure ML pipelines'],
  },
]
</script>
