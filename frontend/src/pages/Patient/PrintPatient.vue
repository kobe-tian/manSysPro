<template>
  <div class="body">
    <div class="div1">
      <form>
        <h2>打印挂号单</h2>
        门&nbsp;诊&nbsp;&nbsp;号:
        <input disabled class="input1" name="patient_name" :value="msg.id"><br><br>
        姓&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;名:<input disabled class="input1" name="patient_name"
          :value="msg.name"><br><br>
        性&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;别:<input disabled class="input1" name="patient_sex"
          :value="msg.sex"><br><br>
        年&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;龄:<input disabled class="input1" name="patient_age"
          :value="msg.age"><br><br>
        身份证号:<input disabled class="input1" name="patient_idcard" :value="msg.id_card"><br><br>
        科&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;室:<input disabled class="input1" name="patient_dept"
          :value="msg.dept"><br><br>
        <input class="input02" type="submit" value="返回主界面" @click="go('/Choose')"><br><br>
        <input class="input02" type="submit" value="返回上一级" @click="go('/Insert')">
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
      msg: {
        age: "",
        dept: "神经外科",
        id: 5,
        id_card: "",
        name: "",
        sex: "女"
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
      this.$api.getPrint({
        patient_id: this.$route.query.id
      }).then(res => {
        console.log(res)
        this.msg = res.data
      })
      // console.log(this.$route.query)
    },
    go (url) {
      this.$router.push(url)
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
  background: url("../../assets/img/2475_wh300.jpg") no-repeat;
  background-size: 100%;
}

.div1 {
  height: 465px;
  width: 450px;
  margin-left: 530px;
  margin-top: -100px;
  background-color: gainsboro;
  opacity: 0.68;
  filter: alpha(opacity=70);
  border-radius: 30px;
}

.input1 {
  width: 200px;
  height: 30px;
  border-style: solid;
  border-top: 0px;
  border-left: 0px;
  border-right: 0px;
  background-color: gainsboro;
  opacity: 0.7;
  filter: alpha(opacity=70);
}

.input02 {
  border-radius: 30px;
  height: 26px;
  width: 100px;
  border-color: black;
  margin-left: 200px;
  font-size: 14px;
}

h2 {
  text-align: center;
  font-size: 22px;
  padding: 20px;
}

body {
  background: url("../../assets/img/2475.jpg_wh300.jpg") no-repeat center center
    fixed;
  background-size: 100%;
}

form {
  width: 400px;
  height: 400px;
  margin: 200px auto;
}

h2 {
  padding: auto;
}

p {
  height: 20px;
  margin-top: 10px;
}

span {
  width: 100px;
  display: inline-block;
  /*将行内元素转换为行内块元素*/
}

.btn input {
  /*设置两个按钮的宽高、边距及边框样式*/
  width: 100px;
  height: 24px;

  margin-right: 100px;
  background: #f0f8ff;
  border-radius: 20px;
}

input {
  text-align: center;
  font-size: 17px;
}
</style>
