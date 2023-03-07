
<script setup lang="ts">
import{reactive,ref} from 'vue'
import { type FormInstance, type FormRules,ElMessage} from 'element-plus'

import useCurrentInstance from '@/utils/useCurrentInstance'
const { proxy } = useCurrentInstance()
const userinfo = reactive({
    name:'',
    email:'',
    avatar:'',
})
</script>

<template>
    <div class="header">
        <div class="logo" >
          <img class="logo_img" src="../assets/logo.png">
        </div>
        <div class="user">
            用户中心
        </div>
    </div>

</template>

<style scoped>

.header{
    background-color: rgb(20, 20, 20);
    height: 68px;
    display: flex;
    left:0 ;
    right: 0 ;
    padding: 0 5% ;
}

.logo{
    margin-left: 2.5rem;
    width: 8rem;

}
.logo_img{
    width: 4rem;
}
.list{
    display: flex;
    align-items: center;
}

ul{
    align-items: center;
    display: flex;
    margin: 0;
    padding: 0;
    list-style: none;
}
.navigation-tab{
    margin-left: 20px;
}
a {
  text-decoration: none;
  color: #d4d4d4;
  font-size: 1.5rem;
  transition: color .4s;
}
a:hover{
    color: #939393;
}
.router-link-active{
  text-decoration: none;
  color: white;
  font-size: 1.5rem;

}
.search{
    display: flex;
    align-items: center;
    justify-content: end;
    flex-grow: 0.4;
    margin-left: auto;
}
.search_but{
    margin-left: 4px;
}
.user{
    margin-left: auto;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    color:white;
    font-size: 1.3rem;
}
.username{
    padding-right: 20px;
}
.account{
    display: flex;
    align-items: center;
}
.avatar{
    width: 2.5rem;
}
</style>