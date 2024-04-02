<script lang="ts">
import { SpeedInsights } from '@vercel/speed-insights/vue';
</script>


<template>
    <div class="pagelayout">
        <SpeedInsights />
        <nav class="navbar">
            <NuxtLink to="/" class="logo-placeholder">
                <div class="logo">
                    <svg viewBox="0 0 38 38" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g>
                            <rect width="38" height="38" rx="19" fill="#04D04D"/>
                            <circle cx="18.8241" cy="19.1759" r="13.1944" stroke="#191414" stroke-width="5"/>
                            <circle cx="18.8241" cy="19.1759" r="4.39815" fill="#191414"/>
                        </g>
                    </svg>
                </div>
                <span>Rectify</span>
            </NuxtLink>
            <div class="product-menu">
                <NuxtLink to="/create/playlist" class="link">Create <span class="mobile-hidden">playlist</span></NuxtLink>
            </div>
            <div class="sign-in">
                <button class="grn-btn mobile-nav-btn">
                    <span>Sign in with spotify</span>
                </button>
            </div>
        </nav>
        <div class="slot-body">
            <slot />
        </div>

        <footer>
            <div class="project-author">
                <span class="project-text">
                    A project by <NuxtLink to="https://github.com/marvellous10" target="_blank" class="footer-link green">marvellous10</NuxtLink>
                </span>
            </div>
            <div class="feedback">
                <span class="feedback-text">
                    Drop a <NuxtLink to="/feedback" class="footer-link green">feedback</NuxtLink>
                </span>
            </div>
        </footer>
    </div>
</template>

<style lang="scss">
html, body {
    margin: 0;
    padding: 0;
    background: #191414; 
}
.text-selection::selection {
    background-color: #04D04D;
}
.green {
    color: #04D04D;
}
.footer-link {
    text-decoration: none;
}
.grn-btn {
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
.pagelayout {
    position: relative;
    display: grid;
    align-content: start;
    justify-items: center;
    width: 98vw;
    margin: 0 auto;
    height: fit-content;
    padding-bottom:30px;
    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 990px;
        padding: 5px;
        border-radius: 25px;
        height: 38px;
        border: 1px solid #FEFEFE;
        position: absolute;
        background: #191414;
        margin-top: 30px;
        .logo-placeholder {
            display: flex;
            align-items: center;
            column-gap: 10px;
            text-decoration: none;
            .logo {
                width: 38px;
                height: 38px;
                display: flex;
                align-items: center;
                justify-content: left;
                svg {
                    width: 38px;
                    height: 38px;
                }
            }
            span {
                font-family:'medium';
                font-size: 24px;
                color: #04D04D;
            }
        }
        .product-menu {
            width: fit-content;
            height: 38px;
            display: flex;
            align-items: center;
            justify-content: center;
            .link {
                color: #FEFEFE;
                text-decoration: none;
                font-family: 'regular';
                font-size: 15px;
            }
            .router-link-active {
                color: #04D04D;
            }
        }
        .sign-in {
            height: fit-content;
            width: fit-content;
            align-items: center;
            justify-content: right;
            border-radius: 20px;
        }
    }
    .slot-body {
        margin-top: 225px;
        margin-bottom: 100px;
    }
    footer {
        width: 1000px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 50px;
        .project-author {
            .project-text {
                color: #FEFEFE;
                font-family: 'regular';
                font-size: 15px;
            }
        }
        .feedback {
            .feedback-text {
                color: #FEFEFE;
                font-family: 'regular';
                font-size: 15px;
            }
        }
    }
}

@media only screen and (max-width: 460px) {
    .mobile-hidden {
        display: none;
    }
    .mobile-btn {
        width: 360px;
    }
    .mobile-btn-hidden {
        display: none;
    }
    .pagelayout {
        width: 100vw;
        height: fit-content;
        justify-items: center;
        .navbar {
            width: 336px;
            padding: 12px;
            height: 24px;
            margin-top: 20px;
            .logo-placeholder {
                column-gap: 5px;
                .logo {
                    width: 24px;
                    height: 24px;
                    svg {
                        width: 24px;
                        height: 24px;
                    }
                }
                span {
                    font-size: 15px;
                }
            }
            .mobile-nav-btn {
                width: 130px;
                height: 24px;
                span {
                    font-size: 12px;
                }
            }
        }
        .slot-body {
            margin-top: 119px;
            width: 360px;
            margin-bottom: 50px;
        }
        footer {
            display: grid;
            justify-content: center;
            align-content: start;
            row-gap: 20px;
            width: 360px;
            .project-author {
                display: flex;
                width: 360px;
                justify-content: center;
                order: 2;
            }
            .feedback {
                display: flex;
                width: 360px;
                justify-content: center;
                order: 1;
            }
        }
    }
}
</style>