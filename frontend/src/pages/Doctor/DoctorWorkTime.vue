<template>
  <div class="body">
    <form>
      <h2>值&nbsp;班&nbsp;查&nbsp;询</h2>
      <div class="di">
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
      </div>
      <div class="tabler">
        <div class="tab">
          <el-table :data="tableData" border style="width: 500px">
            <el-table-column prop="date" label="科室">
            </el-table-column>
            <el-table-column prop="name" label="医生姓名">
            </el-table-column>
            <el-table-column prop="address" label="医生编号">
            </el-table-column>
            <el-table-column prop="address" label="工作时间">
            </el-table-column>
          </el-table>
        </div>
        <div class="tab">
          <el-table :data="tableData" border style="width: 500px">
            <el-table-column prop="date" label="科室">
            </el-table-column>
            <el-table-column prop="name" label="医生姓名">
            </el-table-column>
            <el-table-column prop="address" label="医生编号">
            </el-table-column>
            <el-table-column prop="address" label="工作时间">
            </el-table-column>
          </el-table>
        </div>
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
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
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
  background: url("../../assets/img/work.png") no-repeat center center fixed;
  background-size: 100%;
  font-size: 18px;
  height: calc(100vh);
}

.tabler {
  display: flex;
  justify-content: space-evenly;
}

.tab {
  width: 500px;
}

h2 {
  padding-top: 50px;
  padding-bottom: 30px;
  font-size: 30px;
  font-weight: bold;
}

span {
  width: 75px;
  padding-bottom: 5px;
}

.di {
  display: flex;
  justify-content: center;
}

.b1 {
  width: 400px;
  height: 100px;
  padding: 5px;
}

.b2 {
  width: 500px;
  height: 100px;
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
