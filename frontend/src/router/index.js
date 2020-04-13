import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import newLogin from '@/pages/User/newLogin'
import doctorRegist from '@/pages/User/doctorRegist'
import Choose from '@/pages/User/Choose'
import AlterDoctorInform from '@/pages/Doctor/AlterDoctorInform'
import Diagnosis from '@/pages/Doctor/Diagnosis'
import Display from '@/pages/Doctor/Display'
import DoctorChoose from '@/pages/Doctor/DoctorChoose'
import DoctorSelect from '@/pages/Doctor/DoctorSelect'
import DoctorWorkTime from '@/pages/Doctor/DoctorWorkTime'
import OutHospitalRegist from '@/pages/Doctor/OutHospitalRegist'
import PrintDiagnosisResults from '@/pages/Doctor/PrintDiagnosisResults'
import SearchByDoctorDept from '@/pages/Doctor/SearchByDoctorDept'
import SearchDoctorChoose from '@/pages/Doctor/SearchDoctorChoose'
import SearchEmptyRoom from '@/pages/Doctor/SearchEmptyRoom'
import UserWork from '@/pages/Doctor/UserWork'
import UsersWork from '@/pages/Doctor/UsersWork'
import AddMedicine from '@/pages/Medicine/AddMedicine'
import AddNewMedicine from '@/pages/Medicine/AddNewMedicine'
import AddType from '@/pages/Medicine/AddType'
import MedicineManage from '@/pages/Medicine/MedicineManage'
import TakeMedicine from '@/pages/Medicine/TakeMedicine'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: newLogin
    },
    // {
    //   path: '/Login',
    //   name: 'Login',
    //   component: newLogin
    // },
    {
      path: '/doctorRegist',
      name: 'doctorRegist',
      component: doctorRegist
    },
    {
      path: '/Choose',
      name: 'Choose',
      component: Choose
    },
    {
      path: '/AlterDoctorInform',
      name: 'AlterDoctorInform',
      component: AlterDoctorInform
    },
    {
      path: '/Diagnosis',
      name: 'Diagnosis',
      component: Diagnosis
    },
    {
      path: '/Display',
      name: 'Display',
      component: Display
    },
    {
      path: '/DoctorChoose',
      name: 'DoctorChoose',
      component: DoctorChoose
    },
    {
      path: '/DoctorSelect',
      name: 'DoctorSelect',
      component: DoctorSelect
    },
    {
      path: '/DoctorWorkTime',
      name: 'DoctorWorkTime',
      component: DoctorWorkTime
    },
    {
      path: '/OutHospitalRegist',
      name: 'OutHospitalRegist',
      component: OutHospitalRegist
    },
    {
      path: '/PrintDiagnosisResults',
      name: 'PrintDiagnosisResults',
      component: PrintDiagnosisResults
    },
    {
      path: '/SearchByDoctorDept',
      name: 'SearchByDoctorDept',
      component: SearchByDoctorDept
    },
    {
      path: '/SearchDoctorChoose',
      name: 'SearchDoctorChoose',
      component: SearchDoctorChoose
    },
    {
      path: '/SearchEmptyRoom',
      name: 'SearchEmptyRoom',
      component: SearchEmptyRoom
    },
    {
      path: '/UserWork',
      name: 'UserWork',
      component: UserWork
    },
    {
      path: '/UsersWork',
      name: 'UsersWork',
      component: UsersWork
    },
    {
      path: '/AddMedicine',
      name: 'AddMedicine',
      component: AddMedicine
    },
    {
      path: '/AddNewMedicine',
      name: 'AddNewMedicine',
      component: AddNewMedicine
    },
    {
      path: '/AddType',
      name: 'AddType',
      component: AddType
    },
    {
      path: '/MedicineManage',
      name: 'MedicineManage',
      component: MedicineManage
    },
    {
      path: '/TakeMedicine',
      name: 'TakeMedicine',
      component: TakeMedicine
    }
  ]
})
