<template>
  <div class="login">
    <h3 class="title">
      欢迎登录医院管理平台
    </h3>
    <div class="container">
      <el-form label-position="left" label-width="80px" :model="form">
        <el-form-item label="username">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="password">
          <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
      </el-form>
      <div style="margin-left: 30px;">
        <el-button type="success" @click="mLogin">Manager Login</el-button>
        <el-button type="success" @click="dLogin">Doctor Login</el-button>
      </div>
      <div style="margin-left: 345px;">
        <el-button type="success" @click="regist">regist</el-button>
      </div>
    </div>
  </div>
</template>

<script>
// import doctorApi from '@/api/doctor'

export default {
  props: {

  },
  data () {
    return {
      form: {
        username: '',
        password: ''
      }
    }
  },
  computed: {

  },
  created () {

  },
  mounted () {

  },
  watch: {

  },
  methods: {
    mLogin () {
      // let that = this
      console.log('form >>> ', this.form)
      const { username, password } = this.form
      let params = {
        user_name: username,
        password: password
      }
      this.$api.mLogin(params).then(res => {
        console.log('res >>> ', res)
        if(res.data.status === 0){
          this.$router.push('/Choose')
        }
      })
    },
    dLogin () {
      let that = this
      console.log('form >>> ', this.form)
      const { username, password } = this.form
      let data = {
        api: 'https://c4554896.ngrok.io/doctor_login',
        params: {
          user_name: username,
          password: password
        }
      }
      this.$api.dLogin(data.params).then(res => {
        console.log('res >>> ', res)
        const { data: { status } } = res
        console.log(status)
        if (status === 0) {
          that.$router.push('/DoctorChoose')
        }
      })
        .catch(function (err) {
          console.log(err)
        })
    },
    regist () {
      this.$router.push('/DoctorRegist')
    }
  },
  components: {

  }
}
</script>

<style lang="scss" scoped>
.login {
  width: 100%;
  height: calc(100vh);
  padding: 1px;
  background: #eee;
  background: url("../../assets/img/small.jpg") no-repeat center center fixed;
  background-size: 100% 100%;
  .title {
    font-family: "Roboto", "Lucida Grande", Verdana, Arial, sans-serif;
    font-size: 60px;
    color: dodgerblue;
    text-align: center;
    margin-top: 80px;
  }
  .container {
    padding: 30px;
    width: 400px;
    height: 190px;
    background: lightskyblue;
    border-radius: 15px;
    margin: 30px auto 0;
  }
}
</style>
