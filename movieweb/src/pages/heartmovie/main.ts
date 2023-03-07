import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { bus } from "../../utils/mybus"
import router from './router'
const app = createApp(App)
app.use(ElementPlus)
app.config.globalProperties.$bus = bus
app.use(router)
app.mount('#app')
