import request from '@/utils/request'
const domain = 'https://8b0b9f95.ngrok.io'

export default {
  mLogin (params) {
    return request.post(domain + '/new_login', params)
  },
  regist (params) {
    return request.post(domain + '/doctor_regist', params)
  },
  dLogin (params) {
    return request.post(domain + '/doctor_login', params)
  },
  ruyuandengji (params) {
    return request.get(domain + '/patient_manage', params)
  },
  fenpeibingfang (params) {
    return request.get(domain + '/distribute_room', params)
  }
}
