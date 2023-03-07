<script setup lang="ts">
import Chat from '../components/Chat.vue'
import Header from '../components/Header.vue'
</script>

<template>
    <div class="header_box">
        <Header class="header"></Header>
    </div>
    <div class="main">
        <Chat></Chat>
    </div>

</template>

    
<style scoped>
.main{
    width: 100%;
    background: #bbbbbb;
    height: 100%;
    
}
</style>
