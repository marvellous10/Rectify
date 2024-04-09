<script setup lang="ts">
import { useUserStore } from '../../stores/user.store'
import { useSongStore } from '../../stores/song.store'
import { reactive, ref } from 'vue'

const userStore = useUserStore()
const songStore = useSongStore()
const config = useRuntimeConfig()

const access_token = userStore.access_token

const thumbnail = computed(() => songStore.thumbnail)
const owner = computed(() => songStore.owner)
const duration = computed(() => songStore.duration)
const title = computed(() => songStore.title)
const artists = computed(() => songStore.artists)

const song_checked = computed(() => songStore.owner !== null)

const searched_song = ref('')

const searchSong = async () => {
    try {
        const searchData = {
            'song_query': searched_song.value,
            'access_token': access_token
        }
        const response = await fetch(`${config.public.SEARCH_SONG_ENDPOINT}`, {
            method: 'POST',
            body: JSON.stringify(searchData),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        if (response.ok) {
            const data = await response.json()
            const data_det = data.Song_details
            songStore.setSongDetails(data_det.thumbnail, data_det.owner, data_det.title, data_det.duration, data_det.track_id, data_det.artists)
            searched_song.song = ''
        }
    } catch(error:any) {
        console.error(error)
    }
}

const getCurrentSong = async () => {
    try {
        const response = await fetch(`${config.public.CURRENT_SONG_ENDPOINT}`)
        const data = await response.json()
        const data_det = data.Song_details
        songStore.setSongDetails(data_det.thumbnail, data_det.owner, data_det.title, data_det.duration, data_det.track_id, data_det.artists)
    }catch (error) {
        console.error(error)
    }
}

const playlist_song_list = ref([] as Array<[]>)
var playlist_added = ref(false)
const createPlaylist = async () => {
    try {
        console.log('running create')
        const playlist_data = {
            'track_id': songStore.track_id,
            'token': userStore.access_token
        }
        const response = await fetch(`${config.public.GET_PLAYLIST_ENDPOINT}`, {
            method: 'POST',
            body: JSON.stringify(playlist_data),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        if (response.ok) {
            const data = await response.json()
            playlist_song_list.value = data.playlist
            playlist_added.value = true
        }
    } catch (error) {
        console.error(error)
    }
}


</script>

<template>
    <div class="playlist-wrapper">
        <div class="playlist-header">
            <span class="playlist-header-text"><span class="green">Create</span> your playlist by using a <span class="green">searched</span> song or a song you are <span class="green">currently</span> listening to</span>
        </div>
        <div class="search-buttons">
            <div class="search-container">
                <div class="search-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#FEFEFE">
                        <g>
                            <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                        </g>
                    </svg>
                </div>
                <input type="text" placeholder="Search" v-model="searched_song.song" @keyup.enter="searchSong">
            </div>
            <button @click="getCurrentSong" class="grn-btn mobile-btn">
                <span>Use current song</span>
            </button>
        </div>
        <div class="song-layout-container">
            <SongsLayout v-if="song_checked"
                :thumbnail="thumbnail"
                :duration="duration"
                :artists="artists"
                :owner="owner"
                :title="title"
            />
        </div>
        <div class="create-add-buttons">
            <button @click="createPlaylist" class="grn-btn mobile-btn">
                <span>Create</span>
            </button>
            <button class="grn-btn mobile-btn-hidden" v-if="playlist_added === true">
                <span>Add to playlist</span>
            </button>
        </div>
        <div class="created-playlist">
            <div class="songlayout-container" v-for="song_details in playlist_song_list" :key="song_details.track_id">
                <SongsLayout
                :thumbnail="song_details.thumbnail"
                :duration="song_details.duration"
                :artists="song_details.artists"
                :owner="song_details.owner"
                :title="song_details.title"
                />
            </div>
        </div>
        <div class="playlist-btn">
            <button class="grn-pl-btn" v-if="playlist_added === true">
                <span>Add to playlist</span>
            </button>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.playlist-wrapper {
    display: grid;
    row-gap: 30px;
    align-content: start;
    justify-items: center;
    width: 1000px;
    min-height: 100vh;
    .playlist-header {
        width: 1000px;
        text-align: center;
        .playlist-header-text {
            color: #FEFEFE;
            font-family: 'medium';
            font-size: 32px;
        }
        .playlist-header-text::selection {
            background-color: #04D04D;
        }
    }
    .search-buttons {
        display: flex;
        column-gap: 30px;
        .search-container {
            height: 38px;
            width: 150px;
            border: 1px solid #FEFEFE;
            display: flex;
            background: transparent;
            padding-left: 10px;
            padding-right: 10px;
            column-gap: 5px;
            align-items: center;
            border-radius: 20px;
            .search-icon {
                width: 15px;
                height: 15px;
                svg {
                    width: 15px;
                    height: 15px;
                }
            }
            input {
                width: 125px;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 34px;
                outline: 0;
                border: 0;
                background: transparent;
                //border-radius: 20px;
                font-family: 'regular';
                font-size: 15px;
                color: #FEFEFE;
            }
        }
    }
    .create-add-buttons {
        display: flex;
        column-gap: 30px;
    }
    .created-playlist {
        display: grid;
        row-gap: 10px;
        align-content: start;
        justify-items: center;
        .songlayout-container {
            height: fit-content;
            width: fit-content;
        }
    }
    .playlist-btn {
        display: none;
        .grn-pl-btn {
            background: #04D04D;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 38px;
            width: 170px;
            border: 0;
            outline: 0;
            border-radius: 20px;
            span {
                font-family: 'medium';
                font-size: 15px;
                color: #191414;
            }
        }
    }
}

@media only screen and (max-width: 460px) {
    .playlist-wrapper {
        width: 360px;
        .playlist-header {
            width: 360px;
        }
        .search-buttons {
            display: grid;
            row-gap: 20px;
            justify-items: center;
            align-content: start;
            .search-container {
                width: 340px;
                input {
                    width: 320px;
                }
            }
            .create-add-buttons {
                display: grid;
                row-gap: 20px;
                column-gap: 0;
                align-content: start;
                justify-items: center;
            }
        }
        .playlist-btn {
            display: block;
            .grn-pl-btn {
                width: 360px;
            }
        }
    }
}
</style>