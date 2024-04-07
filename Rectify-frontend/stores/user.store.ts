import { defineStore } from 'pinia'

export const useUserStore = defineStore('userStore', {
    state: () => ({
        id: '' as string | null,
        access_token: '' as string | null,
        spotify_display_name: '' as String | null,
    }),
    persist: true,
    actions: {
        setUserSessionParams(id: string, display_name: string, access_token: string) {
            this.id = id
            this.access_token = access_token
            this.spotify_display_name = display_name
        },
        clearUserSession() {
            this.id = null
            this.access_token = null
            this.spotify_display_name = null
        }
    }
})