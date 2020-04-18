<template>
  <div class="body">
    <h2>科&nbsp;室&nbsp;病&nbsp;人&nbsp;信&nbsp;息</h2>
    <div class="hello">
      <table>
        <tr>
          <th><span>门诊&nbsp;&nbsp;号</span></th>
          <th><span>姓&nbsp;&nbsp;&nbsp;名</span></th>
          <th><span>性&nbsp;&nbsp;&nbsp;别</span></th>
          <th><span>年&nbsp;&nbsp;&nbsp;龄</span></th>
          <th><span>电&nbsp;&nbsp;&nbsp;话</span></th>
          <th><span>科&nbsp;&nbsp;&nbsp;室</span></th>
          <!--定义表头单元格应该横跨的列数-->
        </tr>
        <tr v-for="(item,index) in patient_infos" :key="index">
          <!--循环user_results中的数据输出 -->
          <td>{{item.id}}</td>
          <td>{{item.patient_name}}</td>
          <td>{{item.patient_sex}}</td>
          <td>{{item.patient_age}}</td>
          <td>{{item.patient_telep}}</td>
          <td>{{item.dept_name}}</td>
          <!--定义表头单元格应该横跨的列数-->
        </tr>
      </table>
      <form method="post" class="f">
        <input type="button" class="a2 btn-info" value="继续查找" @click="continuer">
        <input type="button" class="a1 btn-info" value="返回首页" @click="back">
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
      patient_infos: []
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
      this.$api.searchDept({
        patient_dept: this.$route.query.id
      }).then(res => {
        console.log(res)
        if (res.data.patient_infos) {
          this.patient_infos = res.data.patient_infos
        } else {
          alert('该部门没有人员信息！')
          this.$router.push('/SearchPatientChoose')
        }
      })
    },
    continuer () {
      this.$router.push('/SearchPatientChoose')
    },
    back () {
      this.$router.push('/Choose')
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
  margin: 20px auto;
  border-radius: 10px;
}

.f {
  width: 100%;
  height: 150px;
  margin-top: 100px;
  display: flex;
  justify-content: space-around;
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
  margin-top: 60px;
  margin-left: 150px;
  width: 10px;
}

table th {
  background-color: cornflowerblue;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #999999;
  color: black;
  width: 1px;
  text-align: center;
}

table td {
  background-color: #f5fafa;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #999999;
  color: black;
  width: 1px;
  text-align: center;
}

.a1 {
  width: 120px;
  height: 40px;
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
