<template>
  <div class="body">
    <div id="header">
      <div class="pan">
        请输入需要修改的时间：<input type="text" name="alter_value" v-model="alter_value">
      </div>
      <div>
        请输入修改之后的时间：<input type="text" name="alter_value_to" v-model="alter_value_to">&nbsp;&nbsp;
        <input type="button" class="btn1 btn-info" value="修改" @click="changeTime">
      </div>
    </div>
    <div class="tabler">
      <div>
        <el-table :data="tableData" border style="width: 500px">
          <el-table-column prop="dept_name" label="科室">
          </el-table-column>
          <el-table-column prop="work_doctor_name" label="医生姓名">
          </el-table-column>
          <el-table-column prop="doctor_id" label="医生编号">
          </el-table-column>
          <el-table-column prop="work_time" label="工作时间">
          </el-table-column>
        </el-table>
      </div>
    </div>
    <div class="but">
      <el-button @click="back">
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
      tableData: [],
      alter_value: '',
      alter_value_to: ''
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
      this.$api.checkDoctorWord().then(res => {
        console.log(res)
        res.data.work_time_results.forEach(element => {
          this.tableData.push(element)
        });
      })
    },
    back () {
      this.$router.go(-1)
    },
    changeTime () {
      this.$api.reviseDOTime({
        alter_value: this.alter_value,
        alter_value_to: this.alter_value_to
      }).then(res => {
        console.log(res)
        if (res.status === 200) {
          let arr = []
          res.data.work_time_results.forEach(item => {
            arr.push(item)
          })
          this.tableData = arr
        } else {
          alert('修改失败')
        }
      })
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
