<script setup lang="ts">
import { apiGetrecommend } from '@/api/recommend';
import {ref,reactive,watch} from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage} from 'element-plus'

const robot = reactive([
    {me:false,avatar:new URL('../assets/robot.png', import.meta.url).href,
    content:'你好,你今天心情怎么样'},
    {me:false,avatar:new URL('../assets/robot.png', import.meta.url).href,
    content:'你能描述一下想看的电影是怎么样的吗'},
    
])
const fin = reactive({
    me:false,avatar:new URL('../assets/robot.png', import.meta.url).href,
    content:'我将给你推荐电影，请稍等'})
const msgs = reactive([
    {me:false,avatar:new URL('../assets/robot.png', import.meta.url).href,
    content:'你好,您今天心情怎么样'},
    
    
])
const movinfo = ref()
const input=ref('')
const count =ref(1)
var str={info:''}
const router = useRouter()
const sub=()=>{
    
    var add={me:true,avatar:new URL('../assets/i.png', import.meta.url).href,
        content:input.value}
    if(count.value>=2){
        msgs.push(add)
        setTimeout(()=>{   msgs.push(fin) }, 300)
        if(count.value==2){
            str.info=str.info+','+input.value
            
            setTimeout(()=>{   
                apiGetrecommend(str).then((res:any) => {
                    console.log(res.data)
                    if(res.code==1000){
                        movinfo.value=res.data
                        let emos
                        emos=res.list
                        sessionStorage.setItem('movinfo_list',JSON.stringify(emos))
                        sessionStorage.setItem('movinfo_recommend',JSON.stringify(movinfo.value))
                        router.push({
                            name:'Movie',

                        })
                    
                    }
                    else ElMessage.error('出现错误')
                })
            }, 500)
            
        }
    }
    if(count.value<2){

        msgs.push(add)
        let n=count.value
        setTimeout(()=>{   msgs.push(robot[n]) }, 300) 
        if(count.value!=1)       
            str.info=str.info+','+input.value
        else str.info=str.info+input.value
    }
    count.value++
    input.value=''
    
}
</script>
<template>
    <div class="chatting">
        <div class="chatting-header">
            <div class="chatting-title">
                <h2>情绪问答</h2>
            </div>
        </div>
        <div class="chatting-content">
            <div class="list" v-for="item in msgs">
                <div v-if="item.me" class="chatting-item self">
                    
                    <div class="msg-user">
                        <img class="img" :src="item.avatar" />
                    </div>
                    
                    <div class="msg-content">{{ item.content }}</div>
                    
                </div>
                <div v-else class="chatting-item other">
                    
                    <div class="msg-robot">
                        <img class="img" :src="item.avatar" />
                    </div>
                    
                    <div class="msg-content">{{ item.content }}</div>
                </div>
            </div>

        </div>
        <div class="chatting-input" @keyup.enter.native="sub()">
            <el-input v-model="input" placeholder="" />
            <el-button type="success"  round  @click="sub()">发送</el-button>
            
        </div>
    </div>
</template>

<style scoped>
.chatting {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 500px;
    height: 80%;
    margin: auto;
    top: 100px;

}    
.chatting-header {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50px;
    width: 100%;
    background-color: #2196f3;
    color: white;

}

.chatting-content {
    flex: 1;
    width: 100%;
    background-color: #ecf5ff;
    overflow: auto;
    padding-bottom: 100px;
}
.chatting-item {
    padding: 10px;
    overflow: hidden;
}
.msg-date {
    text-align: center;
    color: gray;
    font-size: 80%;
}
img {
    width: 30px;
    height: 30px;

}

.msg-content {
    margin-top: 5px;
    background-color: white;
    width: 200px;
    padding: 6px 10px;
    border-radius: 10px;
}
.msg-user{
    display: flex;
    justify-content: flex-end;
}
.self  .msg-content {
    float: right;
    margin-right: 10px;
}

.self img {
    margin-right: 10px;
}
.msg-robot{
    display: flex;
    justify-content: flex-start;
}
.other  .msg-content {
    float: left;
    margin-left: 10px;
}
.other img {

    margin-left: 10px;
}
.chatting-input{
    width: 380px;
    position: absolute;
    bottom: 10px;
    left: 60px;
    display: flex;
    align-items: center;
}
.el-input{
    height: 40px;
    font-size: 17px;
}
.el-button{
    margin-left: 15px;
    height: 40px;
    font-size: 17px;
}
</style>