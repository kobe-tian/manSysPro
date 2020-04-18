<template>
  <div class="body">
    <div class="title">工作表</div>
    <div class="div1">
      <table border="0">
        <tr class="th1 ">
          <th>科&nbsp;室</th>
          <th>医生姓名</th>
          <th>医生编号</th>
          <th>工作时间</th>
        </tr>
        <!--循环user_results中的数据输出 -->
        <tr class="th2" v-for="(item,index) in work_time_results" :key="index">
          <th>{{item.dept_name}}</th>
          <th>{{item.work_doctor_name}}</th>
          <th>{{item.doctor_id}}</th>
          <th>{{item.work_time}}</th>
        </tr>
      </table>
    </div>
    <input type="button" class="btn btn-success" value="返回上一级" @click="back">
  </div>
</template>

<script>
export default {
  props: {

  },
  data () {
    return {
      work_time_results: [
        {
          dept_name: "神经外科",
          doctor_id: "abc123456",
          work_doctor_name: "123456",
          work_time: "12345"
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
      this.$api.checkKeShiWorkTable().then(res => {
        console.log(res)
        this.work_time_results = res.data.work_time_results
      })
    },
    back () {
      this.$router.go(-1)
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
  background: url("../../assets/img/QQ图片20190327153120.jpg") no-repeat center;
  background-size: 100% 100%;
  font-size: 20px;
  .title {
    font-size: 32px;
    padding-top: 100px;
  }
}

h2 {
  text-align: center;
  margin-top: 4%;
}

table {
  margin: 100px auto;
  border: 1px solid #63b8ff;
}

table th {
  height: 30px;
  font-size: 18px;
  font-family: 宋体;
  width: 120px;
  border: 1px solid #63b8ff;
}

.btn {
  height: 33px;
  width: 100px;
  font-size: 16px;
  margin-left: 5%;
  margin-top: 3%;
  border-radius: 20%;
  background-color: #4cae4c;
}

.th1 {
  background-color: #8ee5ee;
  text-align: center;
}

.th2 {
  background-color: #f0f8ff;
}
</style>
