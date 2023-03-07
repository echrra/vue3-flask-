import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { bus } from "../../utils/mybus"
const app = createApp(App)

app.use(ElementPlus)
app.config.globalProperties.$bus = bus

app.mount('#app')
