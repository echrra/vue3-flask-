// 导入axios实例
import service from '@/utils/request'

// 定义接口的传参
interface LoginInfoBody {
	email: string,
	pwd: string
}

// 获取用户信息 + 登录
export function apiLogin(body: LoginInfoBody) {
	return service.post<any,Response<{token:string}>>('/api/login',body)
}
