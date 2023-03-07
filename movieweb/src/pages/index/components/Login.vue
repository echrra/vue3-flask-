<script setup lang="ts">
import { ref,reactive, onUnmounted } from 'vue'
import useCurrentInstance from '@/utils/useCurrentInstance'
import{apiLogin} from '../../../api/login'
import{apiRegister} from '../../../api/register'
import { type FormInstance, type FormRules,ElMessage} from 'element-plus'
import { apiGetemail } from '@/api/emailget'

const { proxy } = useCurrentInstance()
const isF=ref(false)

const data=reactive({
    email:'',
    show:true
})

proxy.$bus.$on('email', (item: any) => {  

    data.email=item
    if(data.email!=''){
        data.show=false
        loginfo.email=item
    }
    else data.show=true
    console.log(data.show)   
})
proxy.$bus.$on('flag', (item: any) => {  
    isF.value=item
})

const ruleFormr =ref()
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
const reginfo = reactive({
  email: '',
  pwd: '',
  check: '',
  
})
const rrules = reactive<FormRules>({
  email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' },
    {validator: checkEmail, trigger: 'blur'},
  ],
  pwd: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, max: 15, message: '长度在6-15位', trigger: 'blur' },
  ],
  check: [
    { required: true, message: '请输入验证码', trigger: 'blur' },
  ],

})
const ruleForml = ref()
const loginfo = reactive({
  email: '',
  pwd: '',
  
})
const lrules = reactive<FormRules>({
  email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' },
    {validator: checkEmail, trigger: 'blur'},
  ],
  pwd: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, max: 15, message: '长度在6-15位', trigger: 'blur' },
  ],

})

const login =  () => {
    ruleForml.value.validate((valid:any) => {
      
    if (valid) {
        apiLogin(loginfo).then((res) => {
          console.log(res)
            if(res.code==0) {
              ElMessage({
                message: '登录成功',
                type: 'success',
              })
              sessionStorage.setItem('user',JSON.stringify(res.data))
              // console.log(process.env.APP_WEB_URL+'/heartmovie.html')
              window.location.href ='/heartmovie.html';
            }
            else if(res.code==1) {
              ElMessage.error('邮箱不存在')
            }
            else if(res.code==2) {
              ElMessage.error('密码错误')
            }
            else{
              ElMessage.error('错误')
            }
        })
    } else {
      console.log('error submit !')
      return false
    }
  })
};

const register = (()=>{
  ruleFormr.value.validate((valid:any) => {
      
      if (valid) {
          apiRegister(reginfo).then((res) => {
            console.log(res)
              if(res.code==0) {
                ElMessage({
                  message: '注册成功',
                  type: 'success',
                })
                sessionStorage.setItem('user',JSON.stringify(res.data))
                window.location.href = '/heartmovie.html';
              }
              else if(res.code==1) {
                ElMessage.error('邮箱已存在')
              }
              else if(res.code==2) {
                ElMessage.error('验证码错误')
              }
              else{
                ElMessage.error('错误')
              }
          })
      } else {
        console.log('error submit !')
        return false
      }
    })
})
const getemail =  () => {
  const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/

  if(mailReg.test(reginfo.email)){
    const em = reactive({email:reginfo.email})
    apiGetemail(em).then((res) => {
      if(res.code==1) {
          ElMessage.error('邮箱已存在')
        }
    })
    //倒计时
    if (state.sendAuthCode) {
    state.sendAuthCode = false;
    let interval = window.setInterval(function () {
      if (state.second-- <= 0) {
        /* 如果 倒计时完毕 重新赋值*/
        state.second = 60;
        state.sendAuthCode = true;
        window.clearInterval(interval);
      }
    }, 1000);
  }

  }
  
}

const state = reactive({
  sendAuthCode: true,/* 布尔值，通过v-show控制显示‘获取按钮’还是‘倒计时’ */
  second: 60, /* 一分钟 倒计时*/
  timer:null   /* 倒计时 计数器,防止点击的时候触发多个setInterval*/
})


</script>

<template>
    <div class="main" v-if="isF">
        <div v-if="data.show">
            <h1>创建账户！</h1>
            <h1>赶快加入心映。</h1>
            <h2>输入邮箱，创建密码即可开通会员身份</h2>
            <el-form :model="reginfo" :rules="rrules" ref="ruleFormr" @keyup.enter.native="register()">
                <el-form-item label="电子邮箱" prop="email" class="input_box">
                    <el-input v-model="reginfo.email" placeholder="请输入邮箱" class="email" />
                </el-form-item>
                <el-form-item label="输入密码" prop="pwd" class="input_box">
                    <el-input v-model="reginfo.pwd" placeholder="请输入密码" class="pwd" type="password" show-password />
                </el-form-item>    
                <el-form-item label="验证码" prop="check" class="input_box">
                    <el-input v-model="reginfo.check" placeholder="请输入验证码" class="check" />
                    <el-button v-show="state.sendAuthCode" type="success" class="check_button"  @click="getemail()">获取验证码</el-button>
                    <el-button v-show="!state.sendAuthCode" type="info" class="check_button"  >{{state.second}}S</el-button>
                </el-form-item>   
                <el-button type="primary" class="button"  @click="register()">进入心映</el-button>
            </el-form>
        </div>
        <div v-else>
            <h1>欢迎回来！</h1>
            <h1>赶快加入心映。</h1>
            <h2>输入你的密码，马上享受你的情绪导师。</h2>
            <el-form :model="loginfo" :rules="lrules" ref="ruleForml" @keyup.enter.native="login()">
                <el-form-item label="电子邮箱" prop="email" class="input_box">
                    <el-input v-model="loginfo.email" placeholder="请输入邮箱" class="email" />
                </el-form-item>
                <el-form-item label="输入密码" prop="pwd" class="input_box">
                    <el-input v-model="loginfo.pwd" placeholder="请输入密码" class="pwd" type="password" show-password/>
                </el-form-item>    

                <el-button type="primary" class="button"  @click="login()">回到心映</el-button>
            </el-form>
        </div>
    </div>
    
</template>

<style scoped>
.main{
    
    margin: 0 auto;
    max-width: 650px;
    padding-top: 5px;
    padding-bottom: 60px;
    background-color:rgba(0,0,0,0.85);
    border-radius: 30px;

}

h1{
    font-size: 2.5rem;
}
div{
    color: white;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    text-align: center;
}
:deep(.el-form-item){
    
    margin-left: 60px;
}

:deep(.el-form label){
    text-align: center;
    display: inline-flex;
    font-size: 1.1rem;
    font-weight: bold;
    color: white;
    width: 100px;
}

.input_box label{
    width: 72px;
}
.email,.pwd{
    font-size: 20px;
    height: 45px;
    width: 400px;
    margin: 0 5px 0 10px;
}
.check{
    font-size: 20px;
    height: 45px;
    width: 250px;
    margin: 0 5px 0 10px;
}
.check_button{
    width: 150px;
    height: 45px;
    font-size: 20px;
}
.el-button+.el-button{
  margin: 0;
}
.button{
    margin-top: 20px;
    height: 50px;
    width: 200px;
    font-size: 20px;
}

</style>