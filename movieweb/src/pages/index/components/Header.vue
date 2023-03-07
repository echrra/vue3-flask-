<script setup lang="ts">
import { ref,reactive } from 'vue'
import useCurrentInstance from '@/utils/useCurrentInstance'
const { proxy } = useCurrentInstance()
const email = ref('')

const goToLog=()=>{
    proxy.$bus.$emit('email',email )
    proxy.$bus.$emit('flag',true )
}

const value1 = ref('')
const options = [
  {
    value: 'chinese',
    label: '中文',
  },
  {
    value: 'english',
    label: '英文',
  }
]
const func1= () => {
    value1.value=options[0].value;
  }
func1();
</script>

<template>
    <div class="header">
        <div class="logo" >
          <img class="logo_img" src="../assets/logo.png">
        </div>
        <div class="translate">
            <el-select v-model="value1" class="m-2"  size="large">
              <template #prefix>
                <span style="padding-left: 5px; ">
                  <img  class="icon" src="../assets/tran.png">
                </span>
              </template>
                <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                />
            </el-select>
        </div>
        <div class="login" >
            <el-button type="primary" size="large" @click="goToLog">注册</el-button>
        </div>
    </div>
    
</template>

<style scoped>
.header{
    display: flex;
    margin-top: 1rem;
    margin-left: 3rem;
    margin-right: 3rem;
}
.m-2{
    width: 7rem;
}
.logo{
  width: 60rem;
  margin-right: auto;
}
.logo_img{
  width: 5rem;
}
.icon{
  width: 1rem;
  height: 1rem;
}
.translate{
   padding-right: 3rem;
}
.login{

}
</style>