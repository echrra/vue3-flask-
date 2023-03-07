// history模式
import {createRouter,createWebHashHistory,} from 'vue-router'

import Home from '../view/Home.vue'
import Movie from '../view/Movie.vue'

const routes = [
// 路由的默认路径
    {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/movie",
    name: "Movie",
    component: Movie,
    props: true
  },
]

// 创建路由对象
const router = createRouter({
    history: createWebHashHistory(),
    routes
})
export default router;