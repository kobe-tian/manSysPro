<template>
  <div>
    <h2>科&nbsp;室&nbsp;信&nbsp;息</h2>
    <div>
      <table>
        <tr>
          <th><span>编&nbsp;&nbsp;&nbsp;号</span></th>
          <th><span>姓&nbsp;&nbsp;&nbsp;名</span></th>
          <th><span>性&nbsp;&nbsp;&nbsp;别</span></th>
          <th><span>年&nbsp;&nbsp;&nbsp;龄</span></th>
          <th><span>电&nbsp;&nbsp;&nbsp;话</span></th>
          <th><span>职&nbsp;&nbsp;&nbsp;位</span></th>
          <th><span>科&nbsp;&nbsp;&nbsp;室</span></th>
          <!-- <td colspan="6"></td> -->
        </tr>
        <tr v-for="(item,index) in doctor_infos" :key="index">
          <th>{{item.doctor_id}}</th>
          <th>{{item.doctor_name}}</th>
          <th>{{item.doctor_sex}}</th>
          <th>{{item.doctor_age}}</th>
          <th>{{item.doctor_telep}}</th>
          <th>{{item.doctor_position}}</th>
          <th>{{item.dept_name}}</th>
        </tr>
      </table>
      <form class="f">
        <input type="button" class="a2 btn-info" value="返回上一级" @click="back">
        <input type="button" class="a1 btn-info" value="查看科室工作表"  @click="checkKeShiWork">
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
      doctor_infos: [
        {
          dept_name: "神经外科",
          doctor_age: "2",
          doctor_id: "abc123456",
          doctor_name: "abc123456",
          doctor_position: "adwdadwadwawd",
          doctor_sex: "男",
          doctor_telep: "17316289569"
        }
      ]
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
      console.log('hello')
      this.$api.checkKeShi({
        doctor_dept: this.$route.query.id
      }).then(res => {
        console.log(res)
        this.doctor_infos = res.data.doctor_infos
      })
    },
    back(){
      this.$router.go(-1)
    },
    checkKeShiWork(){
      this.$router.push('/UsersWork')
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
body {
  background: url("../../assets/img/display.png") no-repeat center center fixed;
  background-size: 100%;
}

div {
  width: 900px;
  height: 400px;
  margin-left: 240px;
  margin-top: 10px;
  border-radius: 10px;
}

.f {
  width: 760px;
  height: 150px;
  margin-top: 80px;
  margin-left: 90px;
}

span {
  width: 100px;
  height: 20px;
  display: inline-block;
  /*将行内元素转换为行内块元素*/
}

table {
  border-radius: 5px;
  text-align: center;
  margin-top: 50px;
  margin-left: 100px;
  border-collapse: collapse;
  width: 10px;
}

table th {
  background-color: cornflowerblue;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: black;
  color: black;
  width: 2px;
  text-align: center;
}

table td {
  background-color: #f5fafa;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: black;
  color: black;
  width: 2px;
  text-align: center;
}

.a1 {
  width: 120px;
  height: 40px;
  margin-left: 500px;
  background-color: cornflowerblue;
  border-radius: 10px;
  font-family: "Adobe 宋体 Std L";
  font-size: 16px;
}

.a2 {
  width: 120px;
  height: 40px;
  margin-left: 10px;
  margin-top: 20px;
  background-color: cornflowerblue;
  border-radius: 10px;
  font-family: "Adobe 宋体 Std L";
  font-size: 16px;
}

h2 {
  margin-left: 650px;
  margin-top: 80px;
  font-family: "Agency FB";
  font-size: 28px;
}
</style>
