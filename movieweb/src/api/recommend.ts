// 导入axios实例
import service from '@/utils/request'
import type internal from 'stream'

// 定义接口的传参
interface e {
	info:string

}

// 获取用户信息 + 登录
export function apiGetrecommend(body:e) {
	return service.post<any,Response<e>>('/api/getrecommend',body)
}
