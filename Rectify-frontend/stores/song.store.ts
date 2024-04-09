import { defineStore } from 'pinia'

export const useSongStore = defineStore('SongStore', {
    state: () => ({
        thumbnail: '' as string | null,
        owner: '' as string | null,
        title: '' as string | null,
        duration: '' as string | null,
        track_id: '' as string | null,
        artists: [] as Array<[]>,
    }),
    persist: true,
    actions: {
        setSongDetails(thumbnail:string, owner:string, title:string, duration:string, track_id:string, artists:Array<[]>) {
            this.thumbnail = thumbnail
            this.title = title
            this.owner = owner
            this.duration = duration
            this.track_id = track_id
            this.artists = artists
        },
        removeSongDetails() {
            this.thumbnail = null
            this.owner = null
            this.duration = null
            this.track_id = null
            this.artists = []
        }
    }
})