<template>
  <div class="body">
    <form>
      <h2>医生信息修改</h2>
      <div id="bg">
        编号：<input type="text" :value="infos.doctor_id" readonly><br>
        姓名：<input type="text" :value="infos.doctor_name" readonly><br>
        性别：<input type="text" :value="infos.doctor_sex" readonly><br>
        科室：<input type="text" :value="infos.dept_name" readonly><br>
        年龄：<input type="text" v-model="infos.doctor_age" name="age"><br>
        电话：<input type="text" v-model="infos.doctor_telep" name="telep"><br>
        职位：<input type="text" v-model="infos.doctor_position" name="position"><br>
      </div>
      <div class="btn">
        <input type="button" value="确认修改" @click="queren">
        <input type="button" value="返回上一级" @click="back">
      </div>
    </form>
  </div>
</template>

<script>
export default {
  props: {

  },
  data () {
    return {
      infos: {
        dept_name: "神经外科",
        doctor_age: "24",
        doctor_id: "abc123456",
        doctor_name: "abc123456",
        doctor_position: "adwdadwadwawd",
        doctor_sex: "男",
        doctor_telep: "17316289569"
      }
    }
  },
  computed: {

  },
  created () {
    this.init()
  },
  mounted () {

  },
  watch: {

  },
  methods: {
    init () {
      this.$api.showDoctorInfo().then(res => {
        console.log(res)
        this.infos = res.data
      })
    },
    queren () {
      console.log(this.infos)
      this.$api.changeDoctorInfo({
        age: this.infos.doctor_age,
        position: this.infos.doctor_position,
        telep: this.infos.doctor_telep
      }).then(res => {
        console.log(res)
      })
    },
    back(){
      console.log('hello')
      this.$router.go(-1)
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.body {
  height: calc(100vh);
  padding: 1px;
  background: url("../../assets/img/download.jpg") no-repeat center center fixed;
  background-size: 100%;
}

#bg {
  margin-top: 8%;
}

form {
  margin: 100px auto;
  background-color: rgba(100, 149, 237, 0.7);
  height: 520px;
  width: 550px;
  border-radius: 15px;
}

input {
  margin-top: 2%;
  font-size: 16px;
  height: 22px;
}

h2 {
  font-size: 32px;
  margin-top: 5%;
  padding-top: 5%;
}

p {
  height: 22px;
  margin-top: 12px;
  font-size: 18px;
}

p span {
  width: 120px;
  display: inline-block;
  /*将行内元素转换为行内块元素*/
}

.btn input {
  /*设置两个按钮的宽高、边距及边框样式*/
  width: 110px;
  height: 30px;
  background: #f0f8ff;
  border-radius: 20px;
}

.btn {
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
  display: flex;
  margin: 20px 50px;
}

.btn1 {
  padding-top: 10px;
}

input {
  background-color: #8ee5ee;
  border-radius: 5px;
}
</style>
