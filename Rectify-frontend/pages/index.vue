<script>
import { useUserStore } from '../stores/user.store'

userstore = useUserStore()

const Authenticated = computed(() => userstore.access_token !== null)

</script>

<template>
    <div class="home-container">
        <div class="hero-section">
            <div class="main-title">
                <span class="title-text text-selection">Play with your <span class="green">spotify data</span> anyhow <span class="green">you</span> want to.</span>
            </div>
            <div class="sec-section">
                <div class="subtitle">
                    <span class="subtitle-text text-selection">
                        A project that contains many tools to help you interact with your <span class="green">spotify data</span> anyhow <span class="green">you</span> want to.
                    </span>
                </div>
                <div class="sec-btn" v-if="!Authenticated">
                    <button class="grn-btn"><span>Sign in with spotify</span></button>
                </div>
            </div>
        </div>
        <div class="features-section">
            <div class="features-container">
                <div class="feature-title">
                    <span class="text-selection">Features</span>
                </div>
                <div class="feature-menu">
                    <option value="create">Create playlists.</option>
                    <option value="visualize" class="not-ready">Visualize your stats.</option>
                    <option value="History" class="not-ready">Song history.</option>
                    <option value="AI" class="not-ready">AI recommendations.</option>
                </div>
            </div>
            <div class="feature-detail">
                <div class="feature-detail-text">
                    <div class="feature-detail-title">
                        <span class="det-title text-selection">
                            <span class="green">Create</span> the perfect playlist based on the song of your <span class="green">choice.</span>
                        </span>
                    </div>
                    <div class="feature-detail-subtitle">
                        <span class="det-subtitle text-selection">
                            <span class="green ">Search</span> for a song and <span class="green">create</span> a playlist that aligns closely with that song or create one based on what you’re listening to.
                        </span>
                        <NuxtLink to="/create/playlist" class=" footer-link grn-btn"><span>Create</span></NuxtLink>
                    </div>
                </div>
                <div class="feature-detail-picture">
                    <div class="blob">
                        <svg width="450" height="425" viewBox="0 0 450 425" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <g class="rotating-object">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M243.368 7.55286C300.113 13.8886 353.866 32.071 391.58
                                74.9417C431.906 120.783 458.253 179.636 447.642 239.761C436.418 303.368 393.087 355.408 336.569 386.671C275.366
                                420.525 202.853 438.316 138.587 410.716C71.3482 381.839 27.3807 317.484 9.96795 246.409C-7.82144 173.796 -5.35168
                                89.9277 46.8974 36.4571C95.5705 -13.3538 174.154 -0.174975 243.368 7.55286Z" fill="#04D04D"/>
                            </g>
                        </svg>
                    </div>
                    <div class="blob-pictures">
                        <NuxtImg src="/createplaylist/Songpicture2.png" class="img" />
                        <NuxtImg src="/createplaylist/Songpicture.png" class="img" />
                        <NuxtImg src="/createplaylist/Songpicture3.png" class="img" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.home-container {
    .hero-section {
        position: relative;
        display: flex;
        width: 1000px;
        justify-content: space-between;
        align-items: center;
        margin: 0 auto;
        .main-title {
            width: 500px;
            .title-text {
                font-family: 'medium';
                font-size: 64px;
                color: #FEFEFE;
            }
        }
        .sec-section {
            display: grid;
            align-content: start;
            justify-items: left;
            width: 400px;
            row-gap: 20px;
            .subtitle {
                .subtitle-text {
                    font-family: 'regular';
                    font-size: 24px;
                    color: #FEFEFE;
                }
            }
        }
    }
    .features-section {
        //border: 1px solid green;
        margin: 0 auto;
        margin-top: 150px;
        width: 1000px;
        display: grid;
        align-content: start;
        justify-content: center;
        row-gap: 50px;
        .features-container {
            display: grid;
            align-content: start;
            justify-items: center;
            row-gap: 20px;
            width: 1000px;
            .feature-title {
                display: flex;
                align-items: center;
                justify-content: center;
                span {
                    font-family: 'medium';
                    font-size: 32px;
                    color: #FEFEFE;
                }
            }
            .feature-menu {
                display: flex;
                width: 1000px;
                justify-content: space-between;
                align-content: center;
                option {
                    font-family: 'regular';
                    font-size: 24px;
                    color: #04D04D;
                    cursor: pointer; 
                }
                .not-ready {
                    opacity: 0.7;
                    color: #FEFEFE;
                }
            }
        }
        .feature-detail {
            margin-top: 50px;
            width: 1000px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            .feature-detail-text {
                width: 500px;
                display: grid;
                align-content: start;
                justify-content: left;
                row-gap:20px;
                .feature-detail-title {
                    display: flex;
                    width: 500px;
                    .det-title {
                        color: #FEFEFE;
                        font-family: 'medium';
                        font-size: 36px;
                    }
                }
                .feature-detail-subtitle {
                    display: grid;
                    align-content: start;
                    justify-items: left;
                    row-gap: 20px;
                    .det-subtitle {
                        font-family: 'regular';
                        font-size: 18px;
                        color: #FEFEFE;
                    }
                }
            }
            .feature-detail-picture {
                width: 450px;
                height: fit-content;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                .blob {
                    width: fit-content;
                    height: fit-content;
                    svg {
                        width: 450px;
                        height: 425px;
                        transform-origin: 50% 50%;
                        animation: rotate 2s infinte linear;
                    }
                    @keyframes rotate {
                        0% {
                            transform: rotate(0deg); /* Start at 0 degrees */
                        }
                        100% {
                            transform: rotate(360deg); /* Rotate 360 degrees */
                        }        
                    }
                }
                .blob-pictures {
                    position: absolute;
                    margin: 0 auto;
                    display: grid;
                    height: fit-content;
                    align-content: start;
                    justify-content: center;
                    row-gap: 10px;
                    .img {
                        border-radius: 15px;
                        width: 493px;
                        height: 80px;
                        max-width: 493px;
                        max-height: 80px;
                        border: 1px solid #FEFEFE;
                    }
                }
            }
        }
    }
}

@media only screen and (max-width: 460px) {
    .home-container {
        .hero-section {
            display: grid;
            width: 360px;
            align-content: start;
            justify-content: center;
            text-align: center;
            row-gap: 30px;
            .main-title {
                width: 360px;
                .title-text {
                    font-size: 40px;
                }
            }
            .sec-section {
                width: 360px;
                justify-items: center;
                text-align: center;
                .subtitle {
                    .subtitle-text {
                        font-size: 20px;
                    }
                }
            }
        }
        .features-section {
            width: 360px;
            .features-container {
                width: 360px;
                .feature-menu {
                    width: 360px;
                    justify-content: center;
                    option {
                        font-size: 20px;
                    }
                    .not-ready {
                        display: none;
                    }
                }
            }
            .feature-detail {
                width: 360px;
                display: grid;
                align-content: start;
                justify-items: center;
                row-gap: 30px;
                text-align: center;
                .feature-detail-text {
                    width: 360px;
                    order: 2;
                    text-align: center;
                    .feature-detail-title {
                        width: 360px;
                        .det-title {
                            font-size: 40px;
                        }
                    }
                    .feature-detail-subtitle {
                        justify-items: center;
                        .det-subtitle {
                            font-size: 20px;
                        }
                    }
                }
                .feature-detail-picture {
                    width: 360px;
                    order: 1;
                    .blob {
                        svg {
                            width: 350px;
                            height: 330px;
                        }
                    }
                    .blob-pictures {
                        .img {
                            width: 360px;
                            height: 59px;
                        }
                    }
                }
            }
        }
    }
} 
</style>