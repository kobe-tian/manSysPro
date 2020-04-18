<template>
  <div class="body">
    <div id="header">
      <h2>诊断表</h2>
    </div><br>
    <table>
      <tr>
        <th>门诊号</th>
        <td>{{ id }}</td>
      </tr>
      <tr>
        <th>姓名</th>
        <td>{{ patient_name }}</td>
      </tr>
      <tr>
        <th>房号</th>
        <td>{{ room_id }}</td>
      </tr>
      <tr>
        <th>诊断结果</th>
        <td>{{ diagnosis_result }}</td>
      </tr>
      <tr>
        <th>用药详情</th>
        <td>{{ medicine_detail }}</td>
      </tr>
      <tr>
        <th>医嘱</th>
        <td>{{ doctor_suggestions }}</td>
      </tr>
    </table>
    <div id="tb">
      <table>
        <tr>
          <th>医生签名：</th>
          <td>{{ deal_doctor_name }}</td>
        </tr>
        <tr>
          <th>时间：</th>
          <td>{{ diagnosis_time }}</td>
        </tr>
      </table>
    </div>
    <div id="foot">
      <div class="form">
        <el-button>
          继续查询
        </el-button>
        <el-button>
          返回主界面
        </el-button>
      </div>
    </div>
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
.body {
  height: calc(100vh);
  padding: 1px;
  background: url("../../assets/img/4.jpg") no-repeat center fixed;
  background-size: 100%;
}

#header {
  text-align: center;
  height: 50px;
}

h2 {
  font-family: 华文行楷;
  font-size: 40px;
  margin-top: 100px;
}

table {
  border-collapse: collapse;
  margin: 0 auto;
  font-size: 20px;
  color: #333333;
  text-align: center;

  th {
    width: 100px;
  }
}

table td {
  color: #666;
  width: 400px;
  height: 50px;
  border-bottom: 1px solid gray;
  font-family: 华文行楷;
  font-size: 20px;
}

table th {
  font-family: 华文行楷;
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

.btn {
  height: 30px;
  width: 100px;
  font-size: 15px;
  margin-left: 1000px;
  font-family: 华文行楷;
}

#tb {
  margin-left: 550px;
  margin-top: 30px;
  font-size: 18px;
}

#foot {
  margin-top: 50px;
}
</style>
