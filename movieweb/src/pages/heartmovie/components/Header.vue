
<script setup lang="ts">
import { UserFilled } from '@element-plus/icons-vue'
import{onMounted, reactive,ref} from 'vue'
import { type FormInstance, type FormRules,ElMessage} from 'element-plus'
import { useRouter } from 'vue-router'
import {apiGetsearch} from '@/api/getsearch'
import useCurrentInstance from '@/utils/useCurrentInstance'
const { proxy } = useCurrentInstance()
const userinfo = reactive({
    name:'用户',
    avatar:'',
})
const items = reactive([
    {path:'/',name:'推荐'},
    {path:'/Movie',name:'电影'},
    // {path:'/Actor',name:'演员'}
])
const router = useRouter()
const input = ref('')
const movinfo = ref()
const search= ()=>{
    let str=''
    str = input.value.replace(/\s*/g,''); // 去除字符串内所有的空格
    let path=router.currentRoute.value.fullPath
    if(str!=''){
        apiGetsearch(str).then((res:any) => {
            if(res.code==1000){
                movinfo.value=res.data

                if(path=='/movie') {
                    proxy.$bus.$emit('movinfo_search',movinfo.value )
                    
                }
                else{
                    sessionStorage.setItem('movinfo_search',JSON.stringify(movinfo.value))
                    router.push({
                        name:'Movie',

                    })
                }
                
            }
            else ElMessage.error('电影不存在')
        })
    }
    input.value=''
}
const gotoinfo=()=>{
    window.location.href='/user.html'
}
onMounted(()=>{
    let user=JSON.parse(sessionStorage.getItem('user')|| '0')
    console.log(user)
    if(user!=0){
        userinfo.name=user.name
    }
})
</script>

<template>
    <div class="header">
        <div class="logo" >
          <img class="logo_img" src="../assets/logo.png">
        </div>
        <div class="list">
            <ul>
                <li class="navigation-tab" v-for="(item,index) in items" :key="index" >
                    <router-link :to=item.path >{{item.name}}</router-link>
                </li>
                
            </ul>
        </div>
        <div class="search" @keyup.enter.native="search()">
            <el-input v-model="input"  />
            <el-button  class="search_but" @click="search">搜索</el-button>
        </div>
        <div class="user" >
            <div class="username" >
                {{userinfo.name}}
            </div>
            <div class="account" @click="gotoinfo()">
                <img class='avatar' src="../assets/head.png"/>
                <span>

                </span>
            </div>
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
    position: fixed;
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
.account:hover{
    cursor:pointer
}
.avatar{
    width: 2.5rem;
}
</style>