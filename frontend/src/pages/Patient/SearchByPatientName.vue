<template>
  <div class="body">
    <h2>病&nbsp;人&nbsp;信&nbsp;息</h2><br>
    <div class="hello">
      <table>
        <tr>
          <th v-for="(item,index) in result_keys" :key="index">{{item}}</th>
        </tr>
        <tr>
          <th v-for="(item,index) in result_values" :key="index">{{item}}</th>
        </tr>
      </table>
      <form class="f form">
        <input type="button" value="返回上一级" class="a2 btn-info" @click="back">
        <input type="button" value="查看就诊详情" class="a1 btn-info" @click="seeDetails">
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
      this.$api.searchByPName({
        patient_name: this.$route.query.name
      }).then(res => {
        console.log(res)
        if (res.data.result_keys) {
          this.result_keys = res.data.result_keys
          this.result_values = res.data.result_values
        } else {
          alert('没有改病人信息！')
          this.$router.push('/SearchPatientChoose')
        }
      })
    },
    back () {
      this.$router.push('/SearchPatientChoose')
    },
    seeDetails () {
      // this.$router.push(`/DiagnosisDetail?name=${this.$route.query.name}`)
      this.$router.push(`/DiagnosisDetail`)
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
  margin: 80px auto;
  border-radius: 10px;
}

.f {
  width: 700px;
  height: 150px;
  margin-top: 130px;
  margin-left: 100px;
}

.form {
  display: flex;
  justify-content: space-between;
}

span {
  width: 100px;
  display: inline-block;
  /*将行内元素转换为行内块元素*/
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
  background-color: cornflowerblue;
  border-radius: 10px;
  font-family: "Adobe 宋体 Std L";
  font-size: 16px;
}

.a2 {
  width: 120px;
  height: 40px;
  background-color: cornflowerblue;
  border-radius: 10px;
  font-family: "Adobe \5B8B\4F53 Std L";
  font-size: 16px;
}

h2 {
  text-align: center;
  margin-top: 80px;
  font-family: "Agency FB";
  font-size: 28px;
}
</style>
