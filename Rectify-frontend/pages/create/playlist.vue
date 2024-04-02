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
                <input type="text" placeholder="Search">
            </div>
            <button class="grn-btn mobile-btn">
                <span>Use current song</span>
            </button>
        </div>
        <div class="song-layout-container">
            <SongsLayout />
        </div>
        <div class="create-add-buttons">
            <button class="grn-btn mobile-btn">
                <span>Create</span>
            </button>
            <button class="grn-btn mobile-btn-hidden">
                <span>Add to playlist</span>
            </button>
        </div>
        <div class="created-playlist"></div>
        <div class="playlist-btn">
            <button class="desktop-hidden grn-btn mobile-btn">
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
        padding: 10px;
    }
    .desktop-hidden {
        display: none;
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
            .desktop-hidden {
                display: block;
            }
        }
    }
}
</style>