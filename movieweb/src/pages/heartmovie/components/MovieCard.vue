
<script setup lang="ts">

import{reactive,ref,onMounted} from 'vue'
const minfo = ref()
const props=defineProps<{
  mInfo:{
    id:'',
    name:'',
    year:number,
    rating:'',
    img:'',
    tags:[],
    summary:'',
    genre:'',
    country:'',
    show:false
},
}>()

</script>

<template>
    <div class="c-card">
        <el-card :body-style="{ padding: '0px' }" class="c-main">
        <img
            :src="props.mInfo.img"
            class="image"
        />
        <div class="c-des">
            <div class="c-d-t">
                <div class="name">{{props.mInfo.name}}</div>
                <div class="rating">{{props.mInfo.rating}}</div>
            </div>
            
            <div class="bottom">
                <div class="tagbox">
                    <span class="tag" v-for="(item,index) in props.mInfo.tags " key="index" ><div class="tagname" v-if="index<3">{{item}}</div></span>
                </div>
                <div class="summary">{{ props.mInfo.summary }}</div>
                
            </div>
        </div>
        </el-card>
    </div>
    
</template>



<style scoped>
.c-card{
    width: 250px;

}
.c-main{
    width: 244px;
}
.c-des{
    padding:5px;
    padding-bottom: 10px;
    margin-top: -5px;
}
.image{
    margin-left: 12px;
    margin-top: 2px;
    width: 220px;
    height: 300px;
}
.c-d-t{
    display: flex;
}
.name{
    font-size: 20px;
    font-weight: bold;
    width: 150px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.tagbox{
    display: flex;
    flex-direction: row;
    margin-top: 2px;
}
.tagname{
    margin-right: 12px;
    font-size: 15px;
    font-weight: 600;
}
.rating{
    color: red;
    font-size: 25px;
    margin-left: 30px;
}
.summary{ 
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-top: 2px;
}
</style>