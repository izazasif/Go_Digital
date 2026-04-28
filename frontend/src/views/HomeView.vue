<template>
  <div class="min-h-screen bg-brand-dark">
    <AppHeader @open-login="showLogin = true" @open-signup="showSignup = true" />

    <main>
      <HeroBanner />
      <WhatWeDo />
      <OurServices />
      <GoalCommitment />
      <AboutUs />
      <TrustedPartners />
    </main>

    <AppFooter />

    <LoginModal v-if="showLogin" @close="showLogin = false" @switch-to-signup="showLogin = false; showSignup = true" />
    <SignupModal v-if="showSignup" @close="showSignup = false" @switch-to-login="showSignup = false; showLogin = true" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import AppHeader from '@/components/layout/AppHeader.vue'
import AppFooter from '@/components/layout/AppFooter.vue'
import HeroBanner from '@/components/sections/HeroBanner.vue'
import WhatWeDo from '@/components/sections/WhatWeDo.vue'
import OurServices from '@/components/sections/OurServices.vue'
import GoalCommitment from '@/components/sections/GoalCommitment.vue'
import AboutUs from '@/components/sections/AboutUs.vue'
import TrustedPartners from '@/components/sections/TrustedPartners.vue'
import LoginModal from '@/components/auth/LoginModal.vue'
import SignupModal from '@/components/auth/SignupModal.vue'

const showLogin = ref(false)
const showSignup = ref(false)
</script>
