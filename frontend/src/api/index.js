import request from '@/utils/request'
const domain = 'https://9c9019e4.ngrok.io'

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
  display (params) {
    return request.post(domain + '/display', params)
  },
  ruyuandengji (params) {
    return request.get(domain + '/patient_manage', params)
  },
  fenpeibingfang (params) {
    return request.get(domain + '/distribute_room', params)
  },
  chaxunkongfang (params) {
    return request.post(domain + '/distribute_room', params)
  },
  dayinbinglidan (params) {
    return request.post(domain + '/insert_deal_method', params)
  },
  keshimingcheng (params) {
    return request.get(domain + '/out_hospital', params)
  },
  keshimingchengSearch (params) {
    return request.post(domain + '/search_room', params)
  },
  roomConfirm (params) {
    return request.post(domain + '/out_hospital', params)
  },
  initDWT (params) {
    return request.get(domain + '/work_time_search', params)
  },
  searchName (params) {
    return request.post(domain + '/work_time_search', params)
  },
  searchNum (params) {
    return request.post(domain + '/return5', params)
  },
  guahao (params) {
    return request.get(domain + '/guahao', params)
  },
  addPatient (params) {
    return request.post(domain + '/add_patient', params)
  },
  getPrint (params) {
    return request.get(domain + '/add_patient', params)
  },
  bingren (params) {
    return request.get(domain + '/search_p', params)
  },
  searchByPName (params) {
    return request.get(domain + '/search_by_patient_name', params)
  },
  seeDetails (params) {
    return request.get(domain + '/diagnosis_detail', params)
  },
  searchDept (params) {
    return request.post(domain + '/search_by_patient_dept', params)
  },
  yisheng (params) {
    return request.get(domain + '/search_d', params)
  },
  yishengName (params) {
    return request.get(domain + '/search_by_doctor_name', params)
  },
  checkDoctorWord (params) {
    return request.get(domain + '/work2', params)
  },
  reviseDOTime (params) {
    return request.get(domain + '/alter_work_time', params)
  },
  showDoctorInfo (params) {
    return request.get(domain + '/alter', params)
  },
  changeDoctorInfo (params) {
    return request.post(domain + '/back3', params)
  },
  checkKeShi (params) {
    return request.get(domain + '/search_by_doctor_dept', params)
  },
  changeDoctorInfo (params) {
    return request.post(domain + '/back3', params)
  },
  checkKeShiWorkTable (params) {
    return request.get(domain + '/work1', params)
  },
  addNewM (params) {
    return request.post(domain + '/add_medicine_type', params)
  },
  medicine (params) {
    return request.get(domain + '/medicine', params)
  },
  searchMedicine (params) {
    return request.post(domain + '/search_medicine', params)
  },
  quyao (params) {
    return request.post(domain + '/take_medicine', params)
  },
  tianyao (params) {
    return request.post(domain + '/add_medicine', params)
  },
}
