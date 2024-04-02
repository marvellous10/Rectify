<template>
    <div class="song-container">
        <div class="thumbnail-name">
            <NuxtImg src="/createplaylist/image-lady.png" class="song-thumbnail" />
            <div class="song-title-artist">
                <div class="song-name">
                    <span>A lady</span>
                </div>
                <div class="song-artist">
                    <span>Tally Hall</span>
                </div>
            </div>
        </div>
        <div class="stream-number">
            <span>34,121,405</span>
        </div>
        <div class="song-duration">
            <span>1:48</span>
        </div>
        <div class="liked-song">
            <svg viewBox="0 0 150 150" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g>
                    <path d="M125.784 35.0369C113.039 22.2916 92.9859 21.3682 79.1227 32.8994C79.1062 32.9135 77.318 34.3807 75 34.3807C72.6234 34.3807 70.9266 32.9416 70.8609 32.8853C57.0141 21.3682 36.9609 22.2916 24.2156 35.0369C17.6695 41.583 14.0625 50.2877 14.0625 59.5478C14.0625 68.808 17.6695 77.5127 24.0914 83.9228L64.3078 131.006C66.9844 134.14 70.882 135.938 75 135.938C79.1203 135.938 83.0156 134.14 85.6922 131.009L125.782 84.0611C139.301 70.5447 139.301 48.5533 125.784 35.0369ZM122.346 80.8807L82.1297 127.964C80.3461 130.05 77.7469 131.25 75 131.25C72.2531 131.25 69.6562 130.053 67.8703 127.964L27.532 80.7447C21.8695 75.0822 18.75 67.5541 18.75 59.5478C18.75 51.5392 21.8695 44.0135 27.5297 38.351C33.3961 32.4822 41.0555 29.5127 48.7336 29.5127C55.4742 29.5127 62.2289 31.8025 67.7977 36.4338C68.0977 36.7033 70.8586 39.0682 75 39.0682C79.0266 39.0682 81.8578 36.7314 82.1367 36.49C94.1109 26.5291 111.45 27.3307 122.47 38.351C134.159 50.0393 134.159 69.0564 122.346 80.8807Z" fill="#FEFEFE"/>
                </g>
            </svg>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.song-container {
    width:  430px;
    padding: 10px;
    height: fit-content;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1.5px solid #FEFEFE;
    border-radius: 15px;
    .thumbnail-name {
        display: flex;
        column-gap: 10px;
        align-items: center;
        justify-content: center;
        height: 40px;
    }
    .song-thumbnail {
        width: 40px;
        height: 40px;
        max-height: 40px;
        max-width: 40px;
        border-radius: 5px;
    }
    .song-title-artist {
        display: grid;
        height: 40px;
        .song-name {
            align-self: start;
            span {
                font-family: 'medium';
                font-size: 20px;
                color: #FEFEFE;
            }
        }
        .song-artist {
            align-self: end;
            span {
                font-family: 'regular';
                font-size: 13px;
                color: #FEFEFE;
            }
        }
    }
    .stream-number {
        height: 40px;
        width: 100px;
        display: flex;
        align-items: center;
        justify-content: left;
        span {
            font-family: 'regular';
            font-size: 15px;
            color: #FEFEFE;
        }
    }
    .song-duration {
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: left;
        span {
            font-family: 'regular';
            font-size: 15px;
            color: #FEFEFE;
        }
    }
    .liked-song {
        height: 28px;
        width: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        //border: 1px solid white;
        padding-bottom: 4px;
        svg {
            height: 24px;
            width: 24px;
        }
    }
}

@media only screen and (max-width: 460px) {
    .song-container {
        width: 340px;
    }
}
</style>