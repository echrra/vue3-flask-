
<script setup lang="ts">
import { ref,reactive } from 'vue'
import { apiGetgenre } from '@/api/getgenre';
import { apiGetallmovies } from '@/api/getallmovies';
import useCurrentInstance from '@/utils/useCurrentInstance'
const { proxy } = useCurrentInstance()

const value = ref('所有')
const options = reactive([
  {value: '所有',label: '所有',},
  {value: '爱情',label: '爱情',},{value: '动作',label: '动作',},{value: '动画',label: '动画',},{value: '家庭',label: '家庭',},
  {value: '喜剧',label: '喜剧',},{value: '科幻',label: '科幻',},{value: '悬疑',label: '悬疑',},{value: '犯罪',label: '犯罪',},
  {value: '惊悚',label: '惊悚',},{value: '音乐',label: '音乐',},{value: '历史',label: '历史',},{value: '冒险',label: '冒险',},
  {value: '奇幻',label: '奇幻',},{value: '恐怖',label: '恐怖',},{value: '战争',label: '战争',},{value: '传记',label: '传记',},
  {value: '歌舞',label: '歌舞',},{value: '武侠',label: '武侠',},{value: '情色',label: '情色',},{value: '灾难',label: '灾难',},
  {value: '西部',label: '西部',},{value: '纪录片',label: '纪录片',},
])
const movinfo= ref()
const genrechoose = () =>{
  if (value.value=='所有') {
    apiGetallmovies().then((res:any) => {
        
        movinfo.value=res.data
        proxy.$bus.$emit('movinfo_genre',movinfo.value )
    })
  }
  else{
    apiGetgenre(value.value).then((res:any) => {
        
        movinfo.value=res.data
        proxy.$bus.$emit('movinfo_genre',movinfo.value )
    })
  }
  
}

</script>

<template>
    <div class="m_t">
      <div class="m_tbox">
        <span class="m-ct">电影</span>
          <el-select v-model="value" class="m-2" placeholder="Select" size="large" @change="genrechoose">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            class="m-cho"
          />
          </el-select>
      </div>

    </div>
</template>



<style scoped>
.m_t{
  height: 50px;
  display: flex;
  align-items: center;
  padding: 0 5%;
  padding-top: 75px;
}
.m_tbox{
  margin-left: 2.5rem;
}
.m-ct{
  color:white;
  font-size: 40px;

}
.m-2{
  width: 150px;
  margin-left: 2rem;
  height: 55px;
  position: static;
}
:deep(.el-input){
  position: static;
  font-size: 20px;
}
.m-cho{
  font-size: 20px;

}
</style>