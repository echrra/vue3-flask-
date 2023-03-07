// 导入axios实例
import service from '@/utils/request'
import type internal from 'stream'

// 定义接口的传参
interface CommentInfoBody {
	id:'',
    name:'',
    comment:''

}

// 获取用户信息 + 登录
export function apiGetcomment(body:string) {
	return service.post<any,Response<CommentInfoBody>>('/api/getcomment/'+body)
}
