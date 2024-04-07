// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: {
    enabled: true,

    timeline: {
      enabled: true
    }
  },

  css: [
    '~/assets/css/main.css',
  ],

  modules: ["@nuxt/image", '@pinia/nuxt', '@pinia-plugin-persistedstate/nuxt']
})