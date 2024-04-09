// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      SPOTIFY_LOGIN_ENDPOINT: process.env.SPOTIFY_LOGIN_ENDPOINT,
      SPOTIFY_CALLBACK_ENDPOINT: process.env.SPOTIFY_CALLBACK_ENDPOINT,
      SEARCH_SONG_ENDPOINT: process.env.SEARCH_SONG_ENDPOINT,
      CURRENT_SONG_ENDPOINT: process.env.CURRENT_SONG_ENDPOINT,
      GET_PLAYLIST_ENDPOINT: process.env.GET_PLAYLIST_ENDPOINT,
      //LOCAL_SPOTIFY_LOGIN_ENDPOINT: process.env.LOCAL_SPOTIFY_LOGIN_ENDPOINT,
      //LOCAL_SPOTIFY_CALLBACK_ENDPOINT: process.env.LOCAL_SPOTIFY_CALLBACK_ENDPOINT,
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