import request from '@/utils/request'
const domain = 'https://c4554896.ngrok.io'

export default {
  mLogin (params) {
    return request.post(domain + '/new_login', params)
  },
  regist (params) {
    return request.post(domain + '/regist', params)
  }
}
