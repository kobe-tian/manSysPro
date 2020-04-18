import axios from 'axios'
import Qs from 'qs'

// 创建一个axios实例
var http = axios.create({
  withCredentials: true,
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
})

// 请求拦截器
http.interceptors.request.use(
  config => {
    if (config.headers['Content-Type'] === 'application/x-www-form-urlencoded') {
      config.transformRequest = [(data) => Qs.stringify(data)]
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

http.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error && error.response) {
      switch (error.response.status) {
        case 400:
          error.message = '错误请求'
          break
        case 401:
          error.message = '未授权，请重新登录'
          break
        case 403:
          error.message = '拒绝访问'
          break
        case 404:
          error.message = '请求错误,未找到该资源'
          break
        case 405:
          error.message = '请求方法未允许'
          break
        case 422:
          error.message = '参数错误'
          break
        case 408:
          error.message = '请求超时'
          break
        case 500:
          error.message = '服务器端出错'
          break
        case 501:
          error.message = '网络未实现'
          break
        case 502:
          error.message = '网络错误'
          break
        case 503:
          error.message = '服务不可用'
          break
        case 504:
          error.message = '网络超时'
          break
        case 505:
          error.message = 'http版本不支持该请求'
          break
        default:
          error.message = `连接错误${error.response.status}`
      }
    } else {
      error.message = '连接到服务器失败'
    }
    return Promise.reject(error)
  }
)

export default {
  get: function (url, params) {
    return new Promise((resolve, reject) => {
      http
        .get(url, { params: params })
        .then(res => {
          resolve(res)
        })
        .catch(err => {
          reject(err)
        })
    })
  },
  post: function (url, params, config) {
    return new Promise((resolve, reject) => {
      http
        .post(url, params, config)
        .then(res => {
          resolve(res)
        })
        .catch(err => {
          reject(err)
        })
    })
  },
  delete: function (url, params) {
    return new Promise((resolve, reject) => {
      http
        .delete(url, { params: params })
        .then(res => {
          resolve(res)
        })
        .catch(err => {
          reject(err)
        })
    })
  },
  put: function (url, params, config) {
    return new Promise((resolve, reject) => {
      http
        .put(url, params, config)
        .then(res => {
          resolve(res)
        })
        .catch(err => {
          reject(err)
        })
    })
  },
  all: function (url, params) {
    return http.get(url, params)
  }
}
