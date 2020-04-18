<template>
  <div class="body">
    <div class="hello">
      <form method="post">
        <span>按医生姓名查找：</span>
        <input class="kuang1" type="text" name="patient_name" value="" maxlength="100" />
        <input class="kuang2 btn-default" type="submit" value="查询" formaction="/search_by_patient_name/"><br><br>
        <span>按医生科室查找：</span>
        <select class="select01" name="patient_dept">
          <option value="dept.id">dept.dept_name</option>
        </select>
        <input class="kuang2 btn-default" type="submit" value="查询" name="" formaction="/search_by_patient_dept/"
          formmethod="post">
        <input class="kuang3 btn-default" type="submit" value="返回上一级" name="" formaction="/search_by_patient_dept/"
          formmethod="get">
      </form>
    </div>
    <p>给我一份信任，还您一身健康</p>
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
  background-color: mediumorchid;
  background: url("../../assets/img/search_choose.jpg") no-repeat center center
    fixed;
  background-size: 100%;
}

.hello {
  margin: 250px auto;
  width: 550px;
  height: 300px;
  background-color: white;
  border-radius: 15px;
}

.kuang1 {
  width: 200px;
  height: 27px;
  border-radius: 10px;
  margin-top: 40px;
  background-color: #8ee5ee;
}

.kuang2 {
  width: 70px;
  height: 27px;
  border-radius: 10px;
  background-color: #8ee5ee;
  margin-top: 40px;
}

p {
  color: dodgerblue;
  font-size: 42px;
  font-family: "Adobe 楷体 Std R";
  text-align: center;
  margin-top: 60px;
}

.select01 {
  width: 200px;
  height: 27px;
  text-align: center;
  background-color: #8ee5ee;
  border-radius: 10px;
}

.kuang3 {
  width: 100px;
  height: 30px;
  margin-left: 320px;
  margin-top: 100px;
  border-radius: 10px;
  border-radius: 10px;
  background-color: #8ee5ee;
}

span {
  font-size: 18px;
  font-family: "Source Sans Pro", sans-serif;
  margin-left: 35px;
}
</style>
