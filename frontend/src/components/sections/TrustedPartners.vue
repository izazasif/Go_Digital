<template>
  <section class="py-20 bg-brand-dark overflow-hidden border-t border-brand-border">
    <div class="max-w-7xl mx-auto px-6 mb-12 text-center">
      <p class="text-brand-cyan text-sm font-semibold uppercase tracking-widest mb-3">Ecosystem</p>
      <h2 class="text-3xl md:text-4xl font-bold text-white">
        Trusted by Industry Leaders
      </h2>
      <p class="text-gray-400 mt-4 max-w-xl mx-auto">
        We partner with the world's leading technology companies to deliver best-in-class solutions.
      </p>
    </div>

    <!-- Marquee track -->
    <div class="relative">
      <!-- Fade edges -->
      <div class="absolute left-0 top-0 bottom-0 w-32 z-10 bg-gradient-to-r from-brand-dark to-transparent pointer-events-none"></div>
      <div class="absolute right-0 top-0 bottom-0 w-32 z-10 bg-gradient-to-l from-brand-dark to-transparent pointer-events-none"></div>

      <div class="marquee-wrapper">
        <div class="marquee-track">
          <div v-for="(partner, i) in [...partners, ...partners]" :key="i" class="marquee-item">
            <div class="partner-card">
              <span class="partner-icon" :style="{ color: partner.color }">
                <component :is="partner.icon" />
              </span>
              <span class="partner-name">{{ partner.name }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Second row — reverse direction -->
      <div class="marquee-wrapper mt-6">
        <div class="marquee-track marquee-reverse">
          <div v-for="(partner, i) in [...partnersRow2, ...partnersRow2]" :key="i" class="marquee-item">
            <div class="partner-card">
              <span class="partner-icon" :style="{ color: partner.color }">
                <component :is="partner.icon" />
              </span>
              <span class="partner-name">{{ partner.name }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { h } from 'vue'

const makeIcon = (paths) => ({
  render: () => h('svg', { viewBox: '0 0 24 24', fill: 'currentColor', class: 'w-6 h-6' }, paths.map(d => h('path', { d })))
})

const partners = [
  {
    name: 'Amazon AWS',
    color: '#FF9900',
    icon: makeIcon(['M6.763 10.036c0 .296.032.535.088.71.064.176.144.368.256.576.04.064.056.128.056.184 0 .08-.048.16-.152.24l-.504.336a.383.383 0 01-.208.072c-.08 0-.16-.04-.24-.112a2.47 2.47 0 01-.288-.376 6.18 6.18 0 01-.248-.471c-.622.734-1.405 1.101-2.347 1.101-.67 0-1.205-.191-1.596-.574-.391-.384-.59-.894-.59-1.533 0-.678.239-1.23.726-1.644.487-.415 1.133-.623 1.955-.623.272 0 .551.024.846.064.296.04.6.104.918.176v-.583c0-.607-.127-1.03-.375-1.277-.255-.248-.686-.367-1.3-.367-.28 0-.568.031-.863.103-.295.072-.583.16-.862.272a2.287 2.287 0 01-.28.104.488.488 0 01-.127.023c-.112 0-.168-.08-.168-.247v-.391c0-.128.016-.224.056-.28a.597.597 0 01.224-.167c.279-.144.614-.264 1.005-.36a4.84 4.84 0 011.246-.151c.95 0 1.644.216 2.091.647.439.43.662 1.085.662 1.963v2.586zm-3.24 1.214c.263 0 .534-.048.822-.144.287-.096.543-.271.758-.51.128-.152.224-.32.272-.512.047-.191.08-.423.08-.694v-.335a6.66 6.66 0 00-.735-.136 6.02 6.02 0 00-.75-.048c-.535 0-.926.104-1.19.32-.263.215-.39.518-.39.917 0 .375.095.655.295.846.191.2.47.296.838.296zm6.41.862c-.144 0-.240-.024-.304-.08-.063-.048-.12-.16-.168-.311L7.586 5.55a1.398 1.398 0 01-.072-.32c0-.128.064-.2.191-.2h.783c.151 0 .255.025.31.08.065.048.113.16.16.312l1.342 5.284 1.245-5.284c.04-.16.088-.264.151-.312a.549.549 0 01.32-.08h.638c.152 0 .256.025.32.08.063.048.12.16.151.312l1.261 5.348 1.381-5.348c.048-.16.104-.264.16-.312a.52.52 0 01.311-.08h.743c.127 0 .2.065.2.2 0 .04-.009.08-.017.128a1.137 1.137 0 01-.056.2l-1.923 6.17c-.048.16-.104.263-.168.311a.51.51 0 01-.303.08h-.687c-.151 0-.255-.024-.32-.08-.063-.056-.119-.16-.15-.32l-1.238-5.148-1.23 5.14c-.04.16-.087.264-.15.32-.065.056-.177.08-.32.08zm10.256.215c-.415 0-.83-.048-1.229-.143-.399-.096-.71-.2-.918-.32-.128-.071-.215-.151-.247-.223a.563.563 0 01-.048-.224v-.407c0-.167.064-.247.183-.247.048 0 .096.008.144.024.048.016.12.048.2.08.271.12.566.215.878.279.319.064.63.096.95.096.502 0 .894-.088 1.165-.264a.86.86 0 00.415-.758.777.777 0 00-.215-.559c-.144-.151-.416-.287-.807-.415l-1.157-.36c-.583-.183-1.014-.454-1.277-.813a1.902 1.902 0 01-.4-1.158c0-.335.073-.63.216-.886.144-.255.335-.479.575-.654.24-.184.51-.32.83-.415.32-.096.655-.136 1.006-.136.175 0 .359.008.535.032.183.024.35.056.518.088.16.04.312.08.455.127.144.048.256.096.336.144a.69.69 0 01.24.2.43.43 0 01.071.263v.375c0 .168-.064.256-.184.256a.83.83 0 01-.303-.096 3.652 3.652 0 00-1.532-.311c-.455 0-.815.071-1.062.223-.248.152-.375.383-.375.71 0 .224.08.416.24.567.159.152.454.304.877.44l1.134.358c.574.184.99.44 1.237.767.247.327.367.702.367 1.117 0 .343-.072.655-.207.926-.144.272-.336.511-.583.703-.248.2-.543.343-.886.447-.36.111-.743.167-1.142.167zM21.698 16.207c-2.626 1.94-6.442 2.969-9.722 2.969-4.598 0-8.74-1.7-11.87-4.526-.247-.223-.024-.527.27-.351 3.384 1.963 7.559 3.153 11.877 3.153 2.914 0 6.114-.607 9.06-1.852.439-.2.814.287.385.607zM22.792 14.961c-.336-.43-2.22-.207-3.074-.103-.255.032-.295-.192-.063-.36 1.5-1.053 3.967-.75 4.254-.399.287.36-.08 2.826-1.485 4.007-.215.184-.423.088-.327-.151.32-.79 1.03-2.57.695-2.994z'])
  },
  {
    name: 'Microsoft Azure',
    color: '#0078D4',
    icon: makeIcon(['M13.05 4.24L6.56 14.28l-2.49 4.53H6.6l3.09-5.72 5.97-5.56L13.05 4.24zM14.37 5.19L11.5 13.96l6.7-1.86-3.83-6.91zM3.5 19.76h17L18.41 16H7.67L3.5 19.76z'])
  },
  {
    name: 'Google Cloud',
    color: '#4285F4',
    icon: makeIcon(['M12.19 2.38a9.344 9.344 0 00-9.234 6.893c.053-.02-.055.013 0 0C1.609 9.966 1 11.364 1 12.913 1 16.839 4.185 20 8.15 20H19c3.35 0 4-2.783 4-4.333 0-2.65-1.65-4.942-4.003-5.986A9.34 9.34 0 0012.19 2.38zm0 1.5c.97 0 1.91.17 2.79.47L9.01 10.33A7.84 7.84 0 004.8 9.274a7.86 7.86 0 017.39-5.394zM4.08 10.62a6.36 6.36 0 013.32.93L3.69 15.26A6.845 6.845 0 012.5 12.9c0-.83.16-1.63.44-2.36.37.04.75.08 1.14.08zM19 18.5H8.15c-3.117 0-5.65-2.52-5.65-5.587 0-.19.01-.376.03-.56l4.62-5.29A6.37 6.37 0 0112.19 5.88a7.84 7.84 0 016.54 3.51A4.486 4.486 0 0121.5 13.667C21.5 16.1 20.489 18.5 19 18.5z'])
  },
  {
    name: 'Cisco',
    color: '#049FD9',
    icon: makeIcon(['M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z'])
  },
  {
    name: 'Palo Alto',
    color: '#FA582D',
    icon: makeIcon(['M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5'])
  },
  {
    name: 'IBM',
    color: '#1F70C1',
    icon: makeIcon(['M2 5h2v14H2zm4 0h2v14H6zm4 0h8a5 5 0 010 10h-8zm2 2v10h6a3 3 0 000-6h-6z'])
  },
  {
    name: 'Oracle',
    color: '#F80000',
    icon: makeIcon(['M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z'])
  },
  {
    name: 'CrowdStrike',
    color: '#E1000F',
    icon: makeIcon(['M12 2L3 9v6l9 7 9-7V9L12 2zm0 2.5L19 9v5.5L12 19l-7-4.5V9L12 4.5z', 'M12 7l-4 3v4l4 3 4-3v-4L12 7zm0 1.5L15 11v2.5L12 16l-3-2.5V11L12 8.5z'])
  },
]

const partnersRow2 = [
  {
    name: 'Fortinet',
    color: '#EE3124',
    icon: makeIcon(['M12 2L4 6v5c0 4.5 3.5 8.7 8 9.9 4.5-1.2 8-5.4 8-9.9V6L12 2zm0 2.2l6 3.2V11c0 3.5-2.7 6.8-6 8-3.3-1.2-6-4.5-6-8V7.4l6-3.2z'])
  },
  {
    name: 'Splunk',
    color: '#65A637',
    icon: makeIcon(['M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z'])
  },
  {
    name: 'VMware',
    color: '#607078',
    icon: makeIcon(['M2 6h20v12H2z', 'M5 9h14v6H5z'])
  },
  {
    name: 'Red Hat',
    color: '#EE0000',
    icon: makeIcon(['M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.5 13.5c-1.5 1-5.5 1-7 0-1-.7-1-1.5 0-2 .5-.3 1.5-.5 3.5-.5s3 .2 3.5.5c1 .5 1 1.3 0 2z'])
  },
  {
    name: 'HashiCorp',
    color: '#7B42BC',
    icon: makeIcon(['M12 2L2 7v10l10 5 10-5V7L12 2zm0 2.236L20 8.5v7L12 19.764 4 15.5v-7L12 4.236z'])
  },
  {
    name: 'Datadog',
    color: '#632CA6',
    icon: makeIcon(['M12 3L1 9v12h22V9L12 3zm0 2.236L21 10.5V19H3v-8.5L12 5.236z'])
  },
  {
    name: 'Kubernetes',
    color: '#326CE5',
    icon: makeIcon(['M12 2L4.5 6.75v8.5L12 20l7.5-4.75v-8.5L12 2zm0 2.236l5.5 3.482v6.564L12 17.764l-5.5-3.482V7.718L12 4.236z'])
  },
  {
    name: 'Terraform',
    color: '#7B42BC',
    icon: makeIcon(['M15.5 5.5L12 3.5 8.5 5.5V9.5L12 11.5l3.5-2V5.5zM3.5 8.5L0 10.5v4l3.5 2L7 14.5v-4L3.5 8.5zM20.5 8.5L17 10.5v4l3.5 2 3.5-2v-4l-3.5-2zM12 13.5L8.5 15.5v4l3.5 2 3.5-2v-4L12 13.5z'])
  },
]
</script>

<style scoped>
.marquee-wrapper {
  display: flex;
  overflow: hidden;
  user-select: none;
}

.marquee-track {
  display: flex;
  gap: 1.5rem;
  animation: marquee 30s linear infinite;
  width: max-content;
}

.marquee-track:hover {
  animation-play-state: paused;
}

.marquee-reverse {
  animation-direction: reverse;
}

@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

.marquee-item {
  flex-shrink: 0;
}

.partner-card {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 0.75rem;
  padding: 0.75rem 1.5rem;
  transition: background 0.2s, border-color 0.2s;
  cursor: default;
  white-space: nowrap;
}

.partner-card:hover {
  background: rgba(0, 191, 255, 0.06);
  border-color: rgba(0, 191, 255, 0.25);
}

.partner-icon {
  display: flex;
  align-items: center;
  flex-shrink: 0;
}

.partner-name {
  color: #9ca3af;
  font-size: 0.875rem;
  font-weight: 600;
  letter-spacing: 0.025em;
  transition: color 0.2s;
}

.partner-card:hover .partner-name {
  color: #e5e7eb;
}
</style>
