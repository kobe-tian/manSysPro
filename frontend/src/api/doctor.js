import request from '@/utils/request'
const domain = 'https://c4554896.ngrok.io'
export default {
  mLogin (params) {
    return request.post(domain + '/new_login', params)
  },
  regist (params) {
    return request.post(domain + '/regist', params)
  }
  // updateName (params) {
  //   return request.post(
  //     domain + '/api/v2/account/mod_account_name',
  //     params
  //   )
  // },
  // bindPhone (params) {
  //   return request.post(domain + '/api/v2/account/phone', params)
  // },
  // checkPhone (params) {
  //   return request.get(domain + '/api/v2/account/phone', params)
  // },
  // updatePerson (params) {
  //   return request.post(domain + '/api/v2/account/user_info', params)
  // },
  // internService (params) {
  //   return request.get(domain + '/api/v2/intern/service', params)
  // },
  // serviceTop (params) {
  //   return request.get(domain + '/api/v2/intern/service/top', params)
  // }
}
