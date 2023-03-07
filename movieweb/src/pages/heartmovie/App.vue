<script setup lang="ts">

import {computed,ref,reactive, onMounted} from 'vue'
import useCurrentInstance from '@/utils/useCurrentInstance'
const { proxy } = useCurrentInstance()




</script>

<template>
  <div class="all" >
        
    <router-view></router-view>
  </div>
  
</template>

<style>
html,#app{
  height: 100%;

}
body{
  background-color: #141414;
  height: 100%;

}
.all{
  height: 100%;
}

</style>

<style scoped>

</style>