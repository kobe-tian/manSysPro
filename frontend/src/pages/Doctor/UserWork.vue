<template>
  <div>
    <table border="0">
      <tr class="th1">
        <th>科&nbsp;&nbsp;室</th>
        <th>医生姓名</th>
        <th>医生编号</th>
        <th>工作时间</th>
      </tr>
      <!--循环user_results中的数据输出 -->
      <tr class="th2">
        <th>work_time_result.work_doctor_dept.dept_name </th>
        <th>work_time_result.work_doctor_name </th>
        <th>work_time_result.work_doctor_id.doctor_id</th>
        <th>work_time_result.work_time</th>
      </tr>
      <form>
        <div id="header">
          请输入需要修改的时间：<input type="text" name="alter_value"><br><br><br>
          请输入修改之后的时间：<input type="text" name="alter_value_to">&nbsp;&nbsp;
          <input type="submit" class="btn1 btn-info" value="修改" formaction="/alter_work_time/" formmethod="get"
            onclick="alert('修改成功')"><br><br>
        </div>
      </form>
    </table><br><br><br><br><br><br><br>
    <form>
      <input type="submit" class="btn btn-default" value="返回上一级" formaction="/back4/" formmethod="get">
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
  background: url("../../assets/img/QQ图片20190327153120.jpg") no-repeat center
    center fixed;
  background-size: 100%;
}

#header {
  height: 120px;
  margin-top: 50px;
  padding-top: 10px;
  padding-left: 550px;
}

table {
  margin-left: 30%;
  margin-top: 5%;
}

table th {
  height: 40px;
  font-size: 20px;
  font-family: 宋体;
  width: 150px;
}

.th1 {
  background-color: #b0e2ff;
}

.th2 {
  background-color: #f0f8ff;
}

input {
  background-color: #b0e2ff;
  height: 22px;
  border-radius: 30px;
}

.btn {
  height: 30px;
  margin-top: 10px;
  font-size: 15px;
  margin-left: 100px;
  width: 120px;
  height: 40px;
}

.btn1 {
  height: 30px;
  font-size: 15px;
}
</style>
