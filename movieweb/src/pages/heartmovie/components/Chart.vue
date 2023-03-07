<template>
<div :option="option" id="chart" class="chart"></div>
</template>

<script lang="ts" setup>
import * as echarts from 'echarts'
import { onMounted } from 'vue';

const props = defineProps({option:{type:Object,required:true}});
//组件挂载后
onMounted(() => {

  const dom = document.getElementById('chart');
  const chart = dom ? echarts.init(dom) : null;
  chart?.setOption(props.option)

})

</script>

<style scoped>
/* .chart{
  width: 600px;
  height: 500px;
} */
</style>