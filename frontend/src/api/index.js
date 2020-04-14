import request from '@/utils/request'
const domain = 'https://d9c27533.ngrok.io'

export default {
  mLogin (params) {
    return request.post(domain + '/new_login', params)
  },
  regist (params) {
    return request.post(domain + '/doctor_regist', params)
  },
  dLogin (params) {
    return request.post(domain + '/doctor_login', params)
  }
}
