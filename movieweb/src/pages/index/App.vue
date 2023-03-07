<script setup lang="ts">
import Header from './components/Header.vue'
import {computed,ref,reactive, onMounted} from 'vue'
import Main from './components/Main.vue'
import Login from './components/Login.vue'
import useCurrentInstance from '@/utils/useCurrentInstance'
const { proxy } = useCurrentInstance()



</script>

<template>
  <div class="all" >
    <header>
    <Header></Header>
  </header>
  <main class="main_box">
      <Main ></Main>
      <Login></Login>
  </main>
  </div>
  
</template>
<style>
body{
  
  background:linear-gradient( rgba(0,0,0,0.6), rgba(0, 0, 0, 0.6) ),url("./assets/website.jpg");

}
</style>
<style scoped>

main{
  margin-top: 6rem;
}
</style>
