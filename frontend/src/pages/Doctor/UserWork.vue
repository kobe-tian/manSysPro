<template>
  <div class="body">
    <div id="header">
      <div class="pan">
        请输入需要修改的时间：<input type="text" name="alter_value">
      </div>
      <div>
        请输入修改之后的时间：<input type="text" name="alter_value_to">&nbsp;&nbsp;
        <input type="submit" class="btn1 btn-info" value="修改" formaction="/alter_work_time/" formmethod="get"
          onclick="alert('修改成功')">
      </div>
    </div>
    <div class="tabler">
      <div>
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
    <div class="but">
      <el-button>
        返回上一级
      </el-button>
    </div>
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
  height: calc(100vh);
  padding: 1px;
  background: url(/static/img/QQ图片20190327153120.0b2d185.jpg) no-repeat center
    center fixed;
  background-size: 100%;
}

.but {
  margin: 200px 100px;
  display: flex;
}

#header {
  height: 120px;
  margin-top: 50px;
  padding-top: 10px;

  .pan {
    margin-bottom: 30px;
    margin-right: 59px;
  }
}

.tabler {
  display: flex;
  justify-content: center;
  margin-top: 100px;
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
