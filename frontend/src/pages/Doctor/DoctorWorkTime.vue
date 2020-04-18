<template>
  <div class="body">
    <form>
      <h2>值&nbsp;班&nbsp;查&nbsp;询</h2>
      <div class="di">
        <div class="b1">
          <span>请选择科室名称</span>
          <select name="work_dept" class="x1" @change="changeSelect1">
            <option v-for="(item,index) in depts" :key="index" :value="item.id"> {{item.name}} </option>
          </select>
          <input type="button" value="查询" class="btn2" @click="searchName">
        </div>
        <div class="b2">
          <span>请选择医生编号</span>
          <select name="doctor_id" class="x1" @change="changeSelect2">
            <option v-for="(item,index) in doctor_results" :key="index" :value="item.id"> {{item.doctor_id}} </option>
          </select>
          <input type="button" value="查询" class="btn2" @click="searchNum">
        </div>
      </div>
      <div class="tabler">
        <div class="tab">
          <el-table :data="tableData1" border style="width: 500px">
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
        <div class="tab">
          <el-table :data="tableData2" border style="width: 500px">
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
      <input type="button" value="返回上一级" class="btn1" @click="go('/DoctorChoose')">
    </form>
  </div>
</template>

<script>
export default {
  props: {

  },
  data () {
    return {
      depts: [],
      doctor_results: [],
      keywords1: '',
      keywords2: '',
      tableData1: [
      ],
      tableData2: [
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
      this.$api.initDWT().then(res => {
        console.log(res)
        this.depts = res.data.depts;
        this.doctor_results = res.data.doctor_results

        this.keywords1 = res.data.depts[0].id
        this.keywords2 = res.data.doctor_results[0].id
      })
    },
    searchName () {
      this.$api.searchName({
        work_dept: this.keywords1
      }).then(res => {
        console.log(res)
        res.data.work_time_results.forEach(element => {
          this.tableData1.push({
            dept_name: element.dept_name,
            doctor_id: element.doctor_id,
            work_doctor_name: element.work_doctor_name,
            work_time: element.work_time
          })
        });
      })
    },
    searchNum () {
      this.$api.searchNum({
        doctor_id: this.keywords2
      }).then(res => {
        console.log(res)
        res.data.work_time.forEach(element => {
          this.tableData2.push({
            dept_name: element.dept_name,
            doctor_id: element.doctor_id,
            work_doctor_name: element.work_doctor_name,
            work_time: element.work_time
          })
        })
      })
    },
    go (url) {
      this.$router.push(url)
    },
    changeSelect1 (select) {
      let value = select.srcElement.value
      console.log('select >>> ', select.srcElement.value)
    },
    changeSelect2 (select) {
      let value = select.srcElement.value
      console.log('select >>> ', select.srcElement.value)
    },
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
