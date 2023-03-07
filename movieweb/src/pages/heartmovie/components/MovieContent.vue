
<script setup lang="ts">

import { apiGetallmovies } from '@/api/getallmovies';
import{onMounted, reactive,ref} from 'vue'
import m_card from './MovieCard.vue';
import detail from './MovieDetail.vue';
import { useRoute } from 'vue-router'

import useCurrentInstance from '@/utils/useCurrentInstance'
const { proxy } = useCurrentInstance()

const movinfo = ref<any>()
const route = useRoute()
var lens = ref(0)//生成空div占位数目
var list =JSON.parse('0')
onMounted(()=>{
    let storage=JSON.parse('0')
    if(sessionStorage.getItem('movinfo_search')!=null){
        storage=JSON.parse(sessionStorage.getItem('movinfo_search')|| '0')
        sessionStorage.removeItem('movinfo_search')
    }   
    else if(sessionStorage.getItem('movinfo_recommend')!=null){
        storage=JSON.parse(sessionStorage.getItem('movinfo_recommend')|| '0')
        list = JSON.parse(sessionStorage.getItem('movinfo_list')|| '0')
        console.log(list)
        sessionStorage.removeItem('movinfo_recommend')
        sessionStorage.removeItem('movinfo_list')
    }
        
    
    lens.value=0
    if(storage!=0){
        movinfo.value=storage
        var obj=Object.keys(movinfo.value)
        if(obj.length%5!=0){
            lens.value=obj.length
            lens.value=5-lens.value%5
        }
    } 
    if(movinfo.value==undefined){
        apiGetallmovies().then((res) => {
            movinfo.value=res.data
            var obj=Object.keys(movinfo.value)
            if(obj.length%5!=0){
                lens.value=obj.length
                lens.value=5-lens.value%5
            }
            
        })
    }
    console.log(movinfo.value)
})
proxy.$bus.$on('movinfo_genre', (item: any) => {  
    movinfo.value=item
    var obj=Object.keys(movinfo.value)
    if(obj.length%5!=0){
        lens.value=obj.length
        lens.value=5-lens.value%5
    }
   list=0;
})
proxy.$bus.$on('movinfo_search', (item: any) => {  
    movinfo.value=item
    var obj=Object.keys(movinfo.value)
    if(obj.length%5!=0){
        lens.value=obj.length
        lens.value=5-lens.value%5
    }
    list=0
})

const show_card = (index:number)=>{
    movinfo.value[index].show=true
}
const hide_card = (index:number)=>{
    movinfo.value[index].show=false
}
const detailshow = ref(false)
const clickinfo = ref<any>()
const clicklist = ref<any>()
let li=<any>{
    m:[],
    r:[]
}
const show_detail = (index:number)=>{
    clickinfo.value=movinfo.value[index]
    if(list!=0){
        li.r=list[0]
        li.m=list[index+1]
        clicklist.value=li
    }
    else{
        li.r=[-1,-1,-1,-1,-1,-1,-1,-1]
        li.m=[-1,-1,-1,-1,-1,-1,-1,-1]
        clicklist.value=li
    }
    detailshow.value=true
    movinfo.value[index].show=false
}
</script>

<template>
    <div class="m_main">
        <div class="m_m">
            <div class="m_c" v-for="(item,index) in movinfo" key="index" @mouseover="show_card(index)">
                
                
                <m_card  class="card" v-show="item.show" @mouseout="hide_card(index)" :m-info="item" @click="show_detail(index)"></m_card>
                <div class="s_card">
                    <img :src="item.img">
                    <span >{{item.name}}</span>
                </div>
            </div>
            <div class="m_hide"  v-for="item in lens"></div>
        </div>
            
        <el-dialog v-model="detailshow" width="800px" align-center class="detail_box" v-if="detailshow">
                <detail class="detail" :d-info="clickinfo" :list="clicklist" ></detail>
        </el-dialog>
    </div>


</template>



<style scoped>

.m_main{
    width: 85%;
    margin: auto;
    margin-top: 25px;
}
.m_m{
  min-width: 1200px;
  max-width: 1350px;
  margin: auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  flex-direction: row;
}
.m_hide  {
    margin: 0 45px 25px 0; 
    padding: 5px;
    width: 185px;

}
.m_c{
   
    margin: auto;
    display: flex;
    flex-direction: column;
    margin: 0 45px 25px 0; 
    padding: 5px;
    width: 185px;
    flex:none;
    position: relative;
}
.s_card{
    margin: auto;
    display: flex;
    width: 185px;
    flex-direction: column;
    margin: 0 25px 25px 0; 
    padding: 5px;
    width: 185px;
    flex:none;
    z-index: 1;
}
.m_c img{
    width: 185px;
    height: 250px;
}
.m_c span{
    margin-top: 2px;
    font-size: 25px;
    color: white;
    margin-left: 5px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.card{
    position: absolute;
    z-index: 10;
    margin-left: -35px;
    margin-top: -45px;
}
:deep(.el-dialog){
    background-color: #181818;
}
.detail_box{
    min-width: 600px;

}
</style>