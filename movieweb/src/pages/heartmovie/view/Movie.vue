<script setup lang="ts">
import m_title from '../components/MovieTitle.vue'
import m_content from '../components/MovieContent.vue'
import Header from '../components/Header.vue'
import { onMounted } from 'vue';

</script>

<template>
    <div class="header_box">
        <Header class="header"></Header>
    </div>
    <div class="main">
        <m_title class="m_title"></m_title>
        <m_content class="m_content"></m_content>
    </div>

</template>

    
<style scoped>
.main{
    height: 100%;

}
.header{
    z-index: 18;
}
.main{
    z-index: 1;
}
</style>
