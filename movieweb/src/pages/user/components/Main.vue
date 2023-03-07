<script setup lang="ts">
import { ref,reactive,onMounted } from 'vue'
import useCurrentInstance from '@/utils/useCurrentInstance'
import type { FormInstance, FormRules } from 'element-plus'
const { proxy } = useCurrentInstance()

const userinfo = reactive({
    email:'None',
    name:'用户',

})
onMounted(()=>{
    let user=JSON.parse(sessionStorage.getItem('user')|| '0')
    if(user!=0){
        userinfo.name=user.name
        userinfo.email=user.email
    }
})
</script>

<template>
    <div class="main">
        <div class="info_box">
            <div class="info_title"><h1>账户</h1></div>
            <el-divider />
            <div class="info_m">
                <div class="info_n"><h2>用户信息</h2></div>
                <div class="info_mm">
                    <div class="email">{{userinfo.email}}  <div class="email_c">修改邮箱</div></div>
                    <div class="name">{{userinfo.name}}<div class="name_c">修改名字</div></div>
                    <div class="pwd">密码:******<div class="pwd_c">修改密码</div></div>
                </div>
            </div>
        </div>
        
    </div>
   
    
</template>

<style scoped>
.main{
    min-width: 850px;
}
.info_box{
    width: 80%;
    margin: auto;
}
.info_m{
    padding-left: 10%;
    margin: auto;
    display: flex;
}
.info_n{
    width: 250px;
    left: 0;
}
.info_mm{
    margin-top: 10px;
    width: 700px;
}
.email{
    display: flex;
    margin-top: 8px;
    font-size: 18px;
    font-weight: bold;
    height: 40px;
}


.name{
    display: flex;
    margin-top: 8px;
    font-size: 18px;
    font-weight: 400;
    height: 40px;
}

.pwd{
    display: flex;
    margin-top: 8px;
    font-size: 18px;
    color: #444;
    height: 40px;
}
.email_c , .name_c, .pwd_c{
    margin-left: auto;
    font-weight: 200;
    color: #0073e6;
}
.email_c,.name_c,.pwd_c:hover{
    cursor:pointer
}
:deep(.el-divider){
    border-top: 1px solid #999;
}
h2{
    margin: 0;
    color: #555;
}
</style>