<template>
  <div class="body">
    <h2>医&nbsp;生&nbsp;信&nbsp;息&nbsp;表</h2>
    <div class="hello">
      <table>
        <tr>
          <th v-for="(item,index) in result_keys" :key="index">{{item}}</th>
        </tr>
        <tr>
          <th v-for="(item,index) in result_values" :key="index">{{item}}</th>
        </tr>
      </table>
      <form class="f">
        <input type="button" class="a1 btn-info" value="修改医生信息" @click="setDoctorMsg">
        <input type="button" class="a2 btn-info" value="返回上一级" @click="back">
        <input type="button" class="a1 btn-info" value="查看工作时间" @click="checkWorkTime">
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
      result_keys: [],
      result_values: []
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
      this.$api.yishengName({
        doctor_name: this.$route.query.name
      }).then(res => {
        console.log(res)
        if (res.data.result_keys) {
          this.result_keys = res.data.result_keys
          this.result_values = res.data.result_values
        } else {
          alert('没有该医生的信息！')
          this.$router.push('/SearchDoctorChoose')
        }
      })
    },
    back () {
      this.$router.push('/SearchDoctorChoose')
    },
    setDoctorMsg () {
      this.$router.push('/AlterDoctorInform')
    },
    checkWorkTime () {
      this.$router.push('/UserWork')
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.body {
  padding: 1px;
  height: calc(100vh);
  background: url("../../assets/img/display.png") no-repeat center center fixed;
  background-size: 100%;
}
.hello {
  width: 900px;
  height: 400px;
  margin: 100px auto;
  border-radius: 10px;
}
.f {
  width: 780px;
  height: 150px;
  margin-top: 80px;
  margin-left: 70px;
}
span {
  width: 100px;
  display: inline-block; /*将行内元素转换为行内块元素*/
}
table {
  border-radius: 5px;
  text-align: center;
  margin: 50px auto;
}
table th {
  background-color: cornflowerblue;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #999999;
  color: black;
  width: 100px;
  text-align: center;
}
table td {
  background-color: cornflowerblue;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #999999;
  color: black;
  width: 2px;
  text-align: center;
}
.a1 {
  width: 120px;
  height: 40px;
  float: right;
  margin-top: 60px;
  background-color: cornflowerblue;
  border-radius: 10px;
  font-family: "Adobe 宋体 Std L";
  font-size: 16px;
}
.a2 {
  width: 120px;
  height: 40px;
  float: left;
  margin-top: 60px;
  background-color: cornflowerblue;
  border-radius: 10px;
  font-family: "Adobe 宋体 Std L";
  font-size: 16px;
}
h2 {
  text-align: center;
  margin-top: 80px;
  font-family: "Agency FB";
  font-size: 28px;
}
</style>
