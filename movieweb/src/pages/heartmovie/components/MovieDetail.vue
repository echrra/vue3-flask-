<script setup lang="ts">
import { ElMessage } from 'element-plus'
import { apiGetcomment } from '@/api/getcomment';
import { CloseBold } from '@element-plus/icons-vue';
// import { listenerCount } from 'process';
import{reactive,ref,onMounted,watch} from 'vue'
import Chart from '../components/Chart.vue'

const flag= ref(true)
const isfeedback=ref(false)
const feedb = ()=>{
    isfeedback.value=true
	console.log(isfeedback)
}
const props=defineProps<{
  dInfo:{id:'',
    name:'',
    year:number,
    rating:'',
    img:'',
    tags:[],
    summary:'',
    genre:'',
    country:'',
    show:false,

},
    list:{
        m:[-1],
        r:[-1]
    }
}>()
onMounted(()=>{
    
})
const value1 = ref(0)
const value2 = ref(0)
const value3 = ref(0)
const value4 = ref(0)
const value5 = ref(0)
const value6 = ref(0)
const comfirm = ()=>{
	ElMessage({
    message: '提交成功',
    type: 'success',
  	})
    isfeedback.value=false
	value1.value = 0
	value2.value = 0
	value3.value = 0
	value4.value = 0
	value5.value = 0
	value6.value = 0
}


    

const options = ref({
    

    legend: {                        // 图例组件
	        show: true,         
	        icon: 'rect',                   // 图例项的 icon。ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'也可以通过 'image://url' 设置为图片，其中 url 为图片的链接，或者 dataURI。可以通过 'path://' 将图标设置为任意的矢量路径。         
	        top : '20%',                    // 图例距离顶部边距
	        left : '5%',                   // 图例距离左侧边距
	        itemWidth: 15,                  // 图例标记的图形宽度。[ default: 25 ]
	        itemHeight: 15,                 // 图例标记的图形高度。[ default: 14 ]
	        itemGap: 30,                	// 图例每项之间的间隔。[ default: 10 ]横向布局时为水平间隔，纵向布局时为纵向间隔。
	        orient: 'vertical',             // 图例列表的布局朝向,'horizontal'为横向,''为纵向.
	        textStyle: {                    // 图例的公用文本样式。
	            fontSize: 20,
	            color: '#fff'
	        },
	        data: [{                    // 图例的数据数组。数组项通常为一个字符串，每一项代表一个系列的 name（如果是饼图，也可以是饼图单个数据的 name）。图例组件会自动根据对应系列的图形标记（symbol）来绘制自己的颜色和标记，特殊字符串 ''（空字符串）或者 '\n'（换行字符串）用于图例的换行。
	            name: '推荐',                 // 图例项的名称，应等于某系列的name值（如果是饼图，也可以是饼图单个数据的 name）。                    
	            icon: 'rect',               // 图例项的 icon。
	            textStyle: {                // 图例项的文本样式。
	                color: 'rgb(51,0,255)',
	                fontWeight: 'bold'		// 文字字体的粗细，可选'normal'，'bold'，'bolder'，'lighter'
	            }
	        },{
	            name: '电影',
	            icon: 'rect',
	            textStyle: {
	                color: 'rgb(255,0,0)',
	                fontWeight: 'bold'		// 文字字体的粗细，可选'normal'，'bold'，'bolder'，'lighter'
	            }
	        }],
	    },
        radar: [{                       // 雷达图坐标系组件，只适用于雷达图。
	        center: ['50%', '50%'],             // 圆中心坐标，数组的第一项是横坐标，第二项是纵坐标。[ default: ['50%', '50%'] ]
	        radius: 200,                        // 圆的半径，数组的第一项是内半径，第二项是外半径。
	        startAngle: 90,                     // 坐标系起始角度，也就是第一个指示器轴的角度。[ default: 90 ]
	        name: {                             // (圆外的标签)雷达图每个指示器名称的配置项。
	            formatter: '{value}',
	            textStyle: {
	                fontSize: 20,
	                color: '#fff'
	            }
	        },
	        nameGap: 15,                        // 指示器名称和指示器轴的距离。[ default: 15 ]
	        splitNumber: 4,                     // (这里是圆的环数)指示器轴的分割段数。[ default: 5 ]
	        shape: 'circle',                    // 雷达图绘制类型，支持 'polygon'(多边形) 和 'circle'(圆)。[ default: 'polygon' ]
	        axisLine: {                         // (圆内的几条直线)坐标轴轴线相关设置
	            lineStyle: {
	                color: '#fff',                   // 坐标轴线线的颜色。
	                width: 1,                      	 // 坐标轴线线宽。
	                type: 'solid',                   // 坐标轴线线的类型。
	            }
	        },
	        splitLine: {                        // (这里是指所有圆环)坐标轴在 grid 区域中的分隔线。
	            lineStyle: {
	                color: '#fff',                       // 分隔线颜色
	                width: 2, 							 // 分隔线线宽
	            }
	        },
	        splitArea: {                        // 坐标轴在 grid 区域中的分隔区域，默认不显示。
	            show: true,
	            areaStyle: {                            // 分隔区域的样式设置。
	                color: ['rgba(250,250,250,0.3)','rgba(200,200,200,0.3)'],       // 分隔区域颜色。分隔区域会按数组中颜色的顺序依次循环设置颜色。默认是一个深浅的间隔色。
	            }
	        },
	        indicator: [{               // 雷达图的指示器，用来指定雷达图中的多个变量（维度）,跟data中 value 对应
	            name: '乐',                           // 指示器名称   
	            max: 1.2,                               // 指示器的最大值，可选，建议设置 
	            // color: '#fff'                           // 标签特定的颜色。
	        }, {
	            name: '好',
	            max: 1.2,                 
	        }, {
	            name: '怒',
	            max: 1.2,                
	        }, {
	            name: '哀',
	            max: 1.2,                
	        }, {
	            name: '惧',
	            max: 1.2,                
	        }, {
	            name: '恶',
	            max: 1.2,          
	        }, {
	            name: '惊',
	            max: 1.2,             
	        }]
	    }],
        series: [{
	        name: '雷达图',             // 系列名称,用于tooltip的显示，legend 的图例筛选，在 setOption 更新数据和配置项时用于指定对应的系列。
	        type: 'radar',              // 系列类型: 雷达图
	        itemStyle: {                // 折线拐点标志的样式。
	            normal: {                   // 普通状态时的样式
	                lineStyle: {
	                    width: 1
	                },
	                opacity: 0.8
	            },
	            emphasis: {                 // 高亮时的样式
	                lineStyle: {
	                    width: 5
	                },
	                opacity: 1
	            }
	        },
	        data: [{                    // 雷达图的数据是多变量（维度）的
	            name: '电影',                 // 数据项名称
	            value: props.list.m,        // 其中的value项数组是具体的数据，每个值跟 radar.indicator 一一对应。
	            symbol: 'circle',                   // 单个数据标记的图形。
	            symbolSize: 8,                      // 单个数据标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，例如 [20, 10] 表示标记宽为20，高为10。
	            label: {                    // 单个拐点文本的样式设置                            
	                    normal: {  
	                        show: true,             // 单个拐点文本的样式设置。[ default: false ]
	                        position: 'top',        // 标签的位置。[ default: top ]
	                        distance: 5,            // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。[ default: 5 ]
	                        color: 'rgba(255,0,0)',          // 文字的颜色。如果设置为 'auto'，则为视觉映射得到的颜色，如系列色。[ default: "#fff" ]
	                        fontSize: 18,  // 文字的字体大小
                            fontWeight:CloseBold,   
	                        formatter:function(params:any) {  
	                            return params.value;  
	                        }  
	                    }  
	                },
	            itemStyle: {                // 单个拐点标志的样式设置。
	                normal: {
	                    borderColor: 'rgba(255,0,0,1)',       // 拐点的描边颜色。[ default: '#000' ]
	                    borderWidth: 3,                        // 拐点的描边宽度，默认不描边。[ default: 0 ]
	                }
	            },
	            lineStyle: {                // 单项线条样式。
	                normal: {
	                    opacity: 0.8            // 图形透明度
	                }
	            },
	            areaStyle: {                // 单项区域填充样式
	                normal: {
	                    color: 'rgba(255,0,0,0.8)'       // 填充的颜色。[ default: "#000" ]
	                }
	            }
	        }, {
	            name: '推荐',
	            value: props.list.r,
	            symbol: 'circle',
	            symbolSize: 8,
	            label: {                        
	                    normal: {  
	                        show: true,
	                        position: 'top',
	                        distance: 5,
	                        color: 'rgba(51,0,255,1)',
	                        fontSize: 18,
                            fontWeight:CloseBold,   
	                        formatter:function(params:any) {  
	                            return params.value;  
	                        }  
	                    }  
	                },
	            itemStyle: {
	                normal: {
	                    borderColor: 'rgba(51,0,255,1)',
	                    borderWidth: 3,
	                }
	            },
	            lineStyle: {
	                normal: {
	                    opacity: 0.8
	                }
	            },
	            areaStyle: {
	                normal: {
	                    color: 'rgba(51,0,255,0.8)'
	                }
	            }
	        }]
	    }, ]

  
})
const com = ref<any>()
onMounted(()=>{ 
    console.log(props)
    apiGetcomment(props.dInfo.id).then((res) => {
        console.log(res)
        if(res.code==1000){
            com.value=res.data            
        }
    })  
})
</script>

<template>
    
    <div class="d_main">
        <div class="d_top">
            <div class="image_box">
                <img :src="props.dInfo.img" class="image" />
            </div>
            <div class="info_topbox">
                <div class="info_t">
                    <div class="name">{{props.dInfo.name}}</div><div class="rating">{{props.dInfo.rating}}</div>
                </div>
                
                <div class="year">{{props.dInfo.year}}</div>
                
                <div class="tags">
                    <span class="sp">标签：</span>
                    <span class="tag" v-for="(item,index) in props.dInfo.tags " key="index" >{{item}}</span>
                </div>
                <div class="genre"><span class="sp">类型：</span>{{props.dInfo.genre}}</div>
                <div class="country"><span class="sp">国家：</span>{{props.dInfo.country}}</div>
                <div class="summary">{{props.dInfo.summary}}</div>
            </div>

        </div>
        <div class="chart" v-if="(props.list.m[0]!=-1)">
            <Chart :option="options" ></Chart>
        </div>
        <div class="comment">
			<div class="com_lbox">
				<div class="com_title">评论</div>
				<el-button class="feedback" type="danger"  round  @click="feedb()">观影反馈</el-button>

				<el-dialog  v-model="isfeedback" v-if="isfeedback" width="800px">
                	<div class="pj">评价</div>
						<div class="slider-demo-block">
							<span class="demonstration">乐</span>
							<el-slider v-model="value1" />
						</div>
						<div class="slider-demo-block">
							<span class="demonstration">好</span>
							<el-slider v-model="value2" />
						</div>
						<div class="slider-demo-block">
							<span class="demonstration">怒</span>
							<el-slider v-model="value3"  />
						</div>
						<div class="slider-demo-block">
							<span class="demonstration">哀</span>
							<el-slider v-model="value4" />
						</div>
						<div class="slider-demo-block">
							<span class="demonstration">惧</span>
							<el-slider v-model="value5"  />
						</div>
						<div class="slider-demo-block">
							<span class="demonstration">惊</span>
							<el-slider v-model="value6"  />
						</div>
						<el-button class="comfire" type="danger"  round  @click="comfirm()">确认</el-button>
       			</el-dialog>
			</div>

            <div class="comments" v-for="(item,index) in com" key="index" >
                <div class="com_name">{{item.name}} : </div>
                <div class="com_cont">
                    {{item.comment}}
                </div>
                <el-divider />
            </div>
        </div>
    </div>
         
</template>



<style scoped>
.d_main{
   margin-top: -25px;
   color: white;
}
.d_top{
    padding: 5px;
    display: flex;

}
.image_box{

}
.image{
    width: 350px;
    height: 490px;
}
.info_topbox{
    margin-left: 2.5%;
    width: 365px;
}
.sp{
    color:#777;
    font-size: 15px;
}
.info_t{
    position: relative;
    min-height: 50px;
}
.name{
    display: inline-block;
    width: 280px;
    font-size: 30px;
    font-weight: 700;
}

.rating{
    margin-left: 10px;
    display: inline-block;
    font-size: 41px;
    font-weight: bold;
    color: red;
    position: absolute;
    top:10%
}
.year{
    font-size: 20px;
    text-align: end;
    margin-right: 25px;
}
.tags{
    margin-top: 3px;
}
.tag{
    font-size: 17px;
}
.genre{
    margin-top: 3px;
    font-size: 17px;
}
.country{
    margin-top: 3px;
    font-size: 17px;
}
.summary{
    margin-top: 5px;
    font-size: 15px;

}
.com_lbox{
	display: flex;
}
.com_title{

    margin: 11px;
    font-size: 24px;
    color: rgb(245, 82, 61);
    font-weight: 600;
}
.feedback{
    margin: 11px;
	margin-left: 550px;
    font-size: 20px;

}
.comments{
    color: white;
    margin-top: 5px;
    width: 90%;
    margin: auto;
}
.com_name{
    font-size: 16px;
    color: #a0a0a0;
}
:deep(.el-divider ){
    margin: 10px;
}
.chart{
    margin: auto;
    width: 750px;
    height: 500px;
}


.pj{
    color: white;
    font-size: 30px;
    margin-left: 50%;
    margin-top: -10px;
    margin-bottom: 10px;
}
.slider-demo-block {
  display: flex;
  align-items: center;
}
.slider-demo-block .el-slider {
  margin-top: 0;
  margin-left: -15px;
}
.slider-demo-block .demonstration {
    margin-left: 55px;
  font-size: 18px;
  color: white;;
  line-height: 44px;
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-bottom: 0;
}
.slider-demo-block .demonstration + .el-slider {
  flex: 0 0 70%;
}
.comfire{
    margin: 11px;
	margin-left: 600px;
    font-size: 20px;
}
</style>