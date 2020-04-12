<template>
  <div>
    <form>
      <h2>值&nbsp;班&nbsp;查&nbsp;询</h2>
      <div class="b1">
        <span>请选择科室名称</span>
        <select name="work_dept" class="x1">
          <option> work_dept </option>
          <option value="dept.id">dept.dept_name</option>
        </select>
        <input type="submit" value="查询" formaction="/work_time_search/" formmethod="post" class="btn2">
      </div>
      <div class="b2">
        <span>请选择医生编号</span>
        <select name="doctor_id" class="x1">
          <option> doctor_i </option>
          <option value="doctor_result.id">doctor_result.doctor_id</option>
        </select>
        <input type="submit" value="查询" formaction="/return5/" formmethod="post" class="btn2">
      </div>
      <div class="foot_l">
        <table border="2">
          <tr>
            <th>科&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;室</th>
            <th>医&nbsp;生&nbsp;姓&nbsp;名</th>
            <th>医&nbsp;生&nbsp;编&nbsp;号</th>
            <th>工&nbsp;作&nbsp;时&nbsp;间</th>
            <td colspan="2"></td>
          </tr>
          <!--循环user_results中的数据输出 -->
          <tr>
            <td>work_time_result.work_doctor_dept.dept_name </td>
            <td>work_time_result.work_doctor_name </td>
            <td>work_time_result.work_doctor_id.doctor_id</td>
            <td>work_time_result.work_time</td>
            <td colspan="2"></td>
          </tr>
        </table>
      </div>
      <div class="foot_r">
        <table border="2">
          <tr>
            <th>科&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;室</th>
            <th>医&nbsp;生&nbsp;姓&nbsp;名</th>
            <th>医&nbsp;生&nbsp;编&nbsp;号</th>
            <th>工&nbsp;作&nbsp;时&nbsp;间</th>
            <td colspan="2"></td>
          </tr>
          <!--循环user_results中的数据输出 -->
          <tr>
            <td>work_.work_doctor_dept.dept_name </td>
            <td>work_.work_doctor_name </td>
            <td>work_.work_doctor_id.doctor_id</td>
            <td>work_.work_time</td>
            <td colspan="2"></td>
          </tr>
        </table>
      </div>
      <input type="submit" value="返回上一级" class="btn1" formaction="/return5/" formmethod="get">
    </form>
  </div>
</template>

<script>
export default {
  props: {

  },
  data () {
    return {

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

  },
  components: {

  }
}
</script>

<style scoped lang="scss">
body {
  background: url("../../assets/img/work.png") no-repeat center center fixed;
  background-size: 100%;
  font-size: 18px;
}

h2 {
  margin-left: 650px;
  padding-top: 50px;
  padding-bottom: 30px;
}

span {
  width: 75px;
  padding-bottom: 5px;
}

.b1 {
  width: 400px;
  height: 100px;
  margin-left: 19%;
  float: left;
  padding: 5px;
}

.b2 {
  width: 500px;
  height: 100px;
  margin-left: 110px;
  float: left;
}

.btn2 {
  width: 65px;
  height: 30px;
  background: #f0f8ff;
  border-radius: 20px;
}

.foot_l {
  width: 150px;
  height: 100px;
  clear: left;
  float: left;
  margin-left: 19%;
}

.foot_r {
  width: 400px;
  height: 300px;
  float: right;
  margin-right: 22%;
}

.btn1 {
  position: absolute;
  width: 135px;
  height: 45px;
  background: #f0f8ff;
  border-radius: 20px;
  top: 85%;
  font-size: 20px;
  right: 10%;
}

.x1 {
  width: 70px;
  font-size: 16px;
}

table {
  border-collapse: collapse;
  margin: 0 auto;
  text-align: center;
}

table td,
table th {
  border: 1px solid #cad9ea;
  color: #666;
  height: 30px;
}

table thead th {
  background-color: #cce8eb;
  width: 100px;
}

table tr:nth-child(odd) {
  background: #fff;
}

table tr:nth-child(even) {
  background: #f5fafa;
}
</style>
