<template>
    <div class="wrapper">
        <div class="slot-container">
            <slot />
        </div>
    </div>
</template>

<style lang="scss" scoped>
.wrapper {
    background: #191414;
    height: 100vh;
    width: 100vw;
    display: flex;
    align-items: center;
    justify-content: center;
    //margin-left: -8px;
}
</style>