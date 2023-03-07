<script setup lang="ts">
import Header from './components/Header.vue'
import {computed,ref,reactive, onMounted} from 'vue'
import Main from './components/Main.vue'
import useCurrentInstance from '@/utils/useCurrentInstance'
const { proxy } = useCurrentInstance()



</script>

<template>
  <div class="all" >
    <Header></Header>
  <div class="main_box">
      <Main ></Main>
  </div>
  </div>
  
</template>
<style>
body{
  
  background:#f3f3f3;

}
.main_box{
  min-width: 850px;
}

</style>
<style scoped>


</style>
