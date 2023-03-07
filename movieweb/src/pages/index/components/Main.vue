<script setup lang="ts">
import { ref,reactive } from 'vue'
import useCurrentInstance from '@/utils/useCurrentInstance'
import type { FormInstance, FormRules } from 'element-plus'
const { proxy } = useCurrentInstance()
const datas = reactive({
    email:''
})
const ruleForm=ref()
const isF=ref(false)


const goToLog=()=>{
    ruleForm.value.validate((valid:any) => {
    if (valid) {
        proxy.$bus.$emit('email', datas.email)
        proxy.$bus.$emit('flag', true)
    } else {
      console.log('error submit !')
      return false
    }
  })
    
}
proxy.$bus.$on('flag', (item: any) => {  
    isF.value=item
})

var checkEmail = (rule:any, value:any, callback:any) => {
    const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
    setTimeout(() => {
      if (mailReg.test(value)) {
        callback()
      } else {
        callback(new Error('请输入正确的邮箱格式'))
      }
    }, 100)
  }
const rules = reactive<FormRules>({
  email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' },
    {validator: checkEmail, trigger: 'blur'},
  ],
})
</script>

<template>
    <div v-if="!isF" class="main" >
        <div>
            <h1>根据个人推荐的精彩电影内容</h1>
            <h1>享受不一样的情感治愈</h1>
            <h3>随时都能看，享受你的时光</h3>
        </div>
        <div>
            <h5>请输入你的电子邮件，以注册或登录账户</h5>
            <el-form :model="datas" :rules="rules" ref="ruleForm" @keyup.enter.native="goToLog()">
                <el-form-item  prop="email" class="input_box">
                    <el-input v-model="datas.email" placeholder="请输入邮箱" class="input" />
                    <el-button type="primary" class="button" @click="goToLog">开始使用 ></el-button>
                </el-form-item>
                <el-form-item style="margin-bottom:0;display:none;">
                    <el-input></el-input>
                </el-form-item>
            </el-form>
           
            
        </div>
    </div>
    
</template>

<style scoped>
.main{

    margin: 0 auto;
    max-width: 850px;

}
div{
    color: white;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    text-align: center;
}
h1{
    font-size: 3.125rem;
}
h3{
    font-size: 2.125rem;
}
h5{
    font-size: 1.125rem;
}
:deep(.el-form){

    display: flex;
    justify-content: center;
}
.input{
    width: 500px;
    height: 3.5rem;
    font-size: 20px;
}
.button{
    margin-left: 0.1rem;
    width: 150px;
    height: 3.5rem;
    font-size: 25px;
}
</style>