import axios from 'axios'
let m=import.meta.env.VITE_APP_URL
// 创建axios实例
const request = axios.create({
    
    baseURL: m,
    timeout: 80000, // 请求超时时间(毫秒)
    withCredentials: true,
    headers: {
		// 设置后端需要的传参类型
		// 'token': 'your token',
		// 'X-Requested-With': 'XMLHttpRequest',
		// "Access-Control-Allow-Credentials":"true",
	},
})
 
// request拦截器
request.interceptors.request.use(
    config => {  
        let token = localStorage.getItem("x-auth-token");
        if (token) {
            config.headers = {"x-auth-token": token}
        }
        return config
    },
    error => {
        // 对请求错误做些什么
        Promise.reject(error)
    }
)
 
// response 拦截器
request.interceptors.response.use(
    response => {
        // 对响应数据做点什么
        return response.data
    },
    error => {  
        // 对响应错误做点什么
        return Promise.reject(error)
    }
)
export default request