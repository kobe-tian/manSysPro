<template>
  <div class="body">
    <h2>病&nbsp;人&nbsp;信&nbsp;息</h2><br>
    <div class="hello">
      <table>
        <tr>
          <th>医生编号</th>
          <th>姓名</th>
          <th>性别</th>
          <th>年龄</th>
          <th>电话</th>
          <th>职位</th>
          <th>科室</th>
        </tr>
        <tr>
          <td>hello</td>
          <td>hello</td>
          <td>hello</td>
          <td>hello</td>
          <td>hello</td>
          <td>hello</td>
          <td>hello</td>
        </tr>
      </table>
      <form class="f form">
        <input type="submit" value="返回上一级" class="a2 btn-info" formaction="/search_p/">
        <input type="submit" value="查看就诊详情" class="a1 btn-info" formaction="/diagnosis_detail/" formmethod="get">
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
  padding: 1px;
  height: calc(100vh);
  background: url("../../assets/img/display.png") no-repeat center center fixed;
  background-size: 100%;
}

.hello {
  width: 900px;
  height: 400px;
  margin: 80px auto;
  border-radius: 10px;
}

.f {
  width: 700px;
  height: 150px;
  margin-top: 130px;
  margin-left: 100px;
}

.form {
  display: flex;
  justify-content: space-between;
}

span {
  width: 100px;
  display: inline-block;
  /*将行内元素转换为行内块元素*/
}

table {
  border-radius: 5px;
  text-align: center;
  margin: 50px auto;
}
table th {
  background-color: cornflowerblue;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #999999;
  color: black;
  width: 100px;
  text-align: center;
}
table td {
  background-color: cornflowerblue;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #999999;
  color: black;
  width: 2px;
  text-align: center;
}

.a1 {
  width: 120px;
  height: 40px;
  float: right;
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
  font-family: "Adobe \5B8B\4F53 Std L";
  font-size: 16px;
}

h2 {
  text-align: center;
  margin-top: 80px;
  font-family: "Agency FB";
  font-size: 28px;
}
</style>
