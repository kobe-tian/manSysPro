<template>
  <div class="body">
    <p class="biaoyu">为了一切病人，为了病人一切，一切为了病人</p>
    <div class="hezi">
      <form>
        <div id="bg">
          账&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号：
          <input class="kuang1" type="text" maxlength="10" v-model="form.username" /><br><br>
          密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码：
          <input class="kuang1" type="password" size="40" v-model="form.password" /><br><br>
          医生编号：
          <input class="kuang1" type="text" size="40" v-model="form.number" /><br><br>
          <el-button class="btn02 btn-success" @click="confirm">注册</el-button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: {

  },
  data () {
    return {
      form: {
        username: '',
        password: '',
        number: ''
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
    confirm () {
      let that = this
      console.log('form >>> ', this.form)
      const { username, password, number } = this.form
      let params = {
        user_name: username,
        password: password,
        doctor_id: number
      }
      console.log('params >>> ', params)
      this.$api.regist(params).then(res => {
        console.log('res >>> ', res)
        const { data: { status, info } } = res
        console.log(status)
        if (status === 2) {
          that.$router.push('/')
        } else {
          alert(info)
        }
      })
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.hezi {
  height: 300px;
  width: 400px;
  margin-top: 6%;
  margin-left: 35%;
  border-radius: 20px;
  background-color: lightskyblue;
}
.body {
  background-color: mediumorchid;
  background: url("../../assets/img/xiandaiyiyuanlansediaoshuyedating_9400303_small.jpg")
    no-repeat center center fixed;
  background-size: 100% 100%;
  padding: 1px;
  height: calc(100vh);
}
.kuang1 {
  width: 180px;
  height: 25px;
  border-radius: 8px;
  color: midnightblue;
  padding-top: 2%;
  margin-top: 2%;
  margin-left: 5%;
}
.btn02 {
  font-family: "Source Sans Pro", sans-serif;
  width: 80px;
  border-radius: 10px;
  float: right;
  margin-right: 5%;
  margin-top: 6%;
  border-radius: 45px;
  margin-left: 190px;
  background: #5cb85c;

  &:hover {
    background: green;
  }
}
input {
  border-color: lavender;
  border-radius: 45px;
  height: 18px;
  margin-top: 5%;
}
.biaoyu {
  margin-top: 5%;
  color: darkslateblue;
  font-size: 36px;
  font-family: "Adobe 黑体 Std R";
  text-align: center;
}
#bg {
  margin-left: 10%;
  padding-top: 9%;
}
</style>
