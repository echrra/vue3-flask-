// 导入axios实例
import service from '@/utils/request'
import type internal from 'stream'
interface e {
	email:string

}

// 获取用户信息 + 登录
export function apiGetemail(body:e) {
	return service.post<any,Response<{email:string}>>('/api/getemail',body)
}
