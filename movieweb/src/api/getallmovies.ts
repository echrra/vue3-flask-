// 导入axios实例
import service from '@/utils/request'
import type internal from 'stream'

// 定义接口的传参
interface MoiveInfoBody {
	id:'',
    name:'',
    year:number,
    rating:'',
    img:'',
    tags:'',
    summary:'',
    genre:'',
    country:''

}

// 获取用户信息 + 登录
export function apiGetallmovies() {
	return service.post<any,Response<MoiveInfoBody>>('/api/getallmoives')
}
