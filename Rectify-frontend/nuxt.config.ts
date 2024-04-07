// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      SPOTIFY_LOGIN_ENDPOINT: process.env.SPOTIFY_LOGIN_ENDPOINT,
      SPOTIFY_CALLBACK_ENDPOINT: process.env.SPOTIFY_CALLBACK_ENDPOINT
    }
  },
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