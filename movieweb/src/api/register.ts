// 导入axios实例
import service from '@/utils/request'

// 定义接口的传参
interface RegisterInfoBody {
	email: string,
	pwd: string,
    check:string,
}

// 
export function apiRegister(body: RegisterInfoBody) {
	return service.post<any,Response<{token:string}>>('/api/register',body)
}
