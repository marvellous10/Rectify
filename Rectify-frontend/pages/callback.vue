<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '../stores/user.store'

definePageMeta({
    layout: 'authentication'
})


const userstore = useUserStore()
const router = useRouter()
const route = useRoute()


const handleCallback = async() => {
    console.log('Function is running')
    try {
        const code = route.query.code
        if (code) {
            const response = await fetch(`http://127.0.0.1:8000/users/spotify/callback/?code=${code}`)
            const data = await response.json()
            userstore.setUserSessionParams(data.id, data.spotify_display_name, data.access_token)
            router.push('/')

        } else {
          console.error('Authorization code not found in URL')
        }
    } catch (error) {
        console.log(error)
    }
}

handleCallback()
</script>

<template>
    <div class="callback-wrapper">
        <span class="process-text">Processing your authentication, please wait a moment</span>
    </div>
</template>

<style lang="scss" scoped>
.callback-wrapper {
    display: flex;
    width: 98vw;
    height: 50vh;
    align-items: center;
    justify-content: center;
    text-align: center;
    .process-text {
        color: #04D04D;
        font-family: 'medium';
        font-size: 20px;
    }
}

</style>