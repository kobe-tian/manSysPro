// import axios from 'axios'
// import Qs from 'qs'
// import md5 from 'js-md5'
// import store from '@/store/index'
// import { Message } from 'element-ui'

// // 创建一个axios实例
// var http = axios.create({
//   withCredentials: true,
//   headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
// })

// // 请求拦截器
// let cancel
// let promiseArr = {}
// let errorCode = [4038, 4053, 4043, 4143, 4605]
// http.interceptors.request.use(
//   config => {
//     if (config.headers['Content-Type'] === 'application/x-www-form-urlencoded') {
//       config.transformRequest = [(data) => Qs.stringify(data)]
//     }
//     // 发起请求时，取消掉当前正在进行的相同请求
//     if (promiseArr[config.url]) {
//       promiseArr[config.url]('操作取消')
//       promiseArr[config.url] = cancel
//     } else {
//       promiseArr[config.url] = cancel
//     }
//     return config
//   },
//   error => {
//     return Promise.reject(error)
//   }
// )
// http.interceptors.response.use(
//   response => {
//     return response
//   },
//   error => {
//     if (error && error.response) {
//       switch (error.response.status) {
//         case 400:
//           error.message = '错误请求'
//           break
//         case 401:
//           error.message = '未授权，请重新登录'
//           break
//         case 403:
//           error.message = '拒绝访问'
//           break
//         case 404:
//           error.message = '请求错误,未找到该资源'
//           break
//         case 405:
//           error.message = '请求方法未允许'
//           break
//         case 422:
//           error.message = '参数错误'
//           break
//         case 408:
//           error.message = '请求超时'
//           break
//         case 500:
//           error.message = '服务器端出错'
//           break
//         case 501:
//           error.message = '网络未实现'
//           break
//         case 502:
//           error.message = '网络错误'
//           break
//         case 503:
//           error.message = '服务不可用'
//           break
//         case 504:
//           error.message = '网络超时'
//           break
//         case 505:
//           error.message = 'http版本不支持该请求'
//           break
//         default:
//           error.message = `连接错误${error.response.status}`
//       }
//     } else {
//       error.message = '连接到服务器失败'
//     }
//     return Promise.reject(error)
//   }
// )

// export default {
//   get: function (url, params, timeout, isAuth) {
//     return new Promise((resolve, reject) => {
//       http
//         .get(url, { params: params })
//         .then(res => {
//           if (res.data.code === 100) {
//             var resData = ''
//             if (res.data.data) {
//               resData = res.data.data
//             } else {
//               if (res.data.msg !== 'success') {
//                 resData = res.data.msg
//               }
//             }
//             if (!resData) {
//               resData = ''
//             }
//             resolve(resData)
//           } else {
//             // let errCode = res.data.code
//             let err = {
//               code: res.data.code,
//               msg: res.data.msg,
//               data: res.data.data
//             }
//             if (err.code === 401 && !isAuth) {
//               // 服务端强制下线用户，需要清理用户信息，以让beforeeach中判断进入登录页
//               // store.commit('setUserInfo', null)
//               window.location.href = '/#/login'
//             } else if (err.code === 4062) {
//               // 帐号被挤下线
//               if (!store.state.user.logOut) {
//                 store.commit('setLogoutStatus', true)
//               }
//             } else if (err.code > 4000 && errorCode.indexOf(err.code) < 0) {
//               Message({
//                 message: err.msg,
//                 customClass: 'message-alert',
//                 type: 'error'
//               })
//               // console.log(err)
//             }
//             reject(err)
//           }
//         })
//         .catch(res => {
//           let err = {
//             code: (res.response && res.response.status) || 0,
//             msg: res.message
//           }
//           reject(err)
//         })
//     })
//   },
//   delete: function (url, params) {
//     return new Promise((resolve, reject) => {
//       http
//         .delete(url, { params: params })
//         .then(res => {
//           if (res.data.code === 100) {
//             // console.log(`${url}请求成功`)
//             let resData = res.data.data || res.data.msg
//             if (!resData) {
//               resData = ''
//             }
//             resolve(resData)
//           } else {
//             // let errCode = res.data.code
//             let err = {
//               code: res.data.code,
//               msg: res.data.msg
//             }
//             reject(err)
//           }
//         })
//         .catch(res => {
//           let err = {
//             code: (res.response && res.response.status) || 0,
//             msg: res.message
//           }
//           reject(err)
//         })
//     })
//   },
//   put: function (url, params, config) {
//     return new Promise((resolve, reject) => {
//       http
//         .put(url, params, config)
//         .then(res => {
//           if (res.data.code === 100) {
//             // console.log(`${url}请求成功`)
//             let resData = res.data.data || res.data.msg
//             if (!resData) {
//               resData = ''
//             }
//             resolve(resData)
//           } else {
//             // let errCode = res.data.code
//             let err = {
//               code: res.data.code,
//               msg: res.data.msg
//             }
//             reject(err)
//           }
//         })
//         .catch(res => {
//           let err = {
//             code: (res.response && res.response.status) || 0,
//             msg: res.message
//           }
//           reject(err)
//         })
//     })
//   },
//   post: function (url, params, config) {
//     return new Promise((resolve, reject) => {
//       let postingId = md5(url + JSON.stringify(params))
//       if (sessionStorage.getItem(postingId)) {
//         // let err = { code: 1001, msg: '重复提交' }
//         // reject(err)
//         // console.log('重复提交')
//         return false
//       }

//       // assert.deepEqual(Qs.parse(params))
//       // let dt = headers['Content-Type'] === 'application/json' ? Qs.parse(params) : params;
//       // console.log(headers['Content-Type'])
//       sessionStorage.setItem(postingId, 1)
//       http
//         .post(url, params, config)
//         .then(res => {
//           sessionStorage.removeItem(postingId)
//           if (res.data.code === 100) {
//             // alert('data' in res.data)
//             let resData = res.data.data || res.data.msg
//             if (!resData) {
//               resData = ''
//             }
//             resolve(resData)
//           } else {
//             let err = {
//               code: res.data.code,
//               msg: res.data.msg,
//               data: res.data.data
//             }
//             reject(err)
//           }
//         })
//         .catch(res => {
//           sessionStorage.removeItem(postingId)
//           let err = {
//             code: (res.response && res.response.status) || 0,
//             msg: res.message
//           }
//           reject(err)
//         })
//     })
//   },
//   all: function (url, params) {
//     return http.get(url, params)
//   }
// }
