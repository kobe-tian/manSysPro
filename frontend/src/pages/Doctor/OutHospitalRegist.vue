<template>
  <div class="body">
    <h2>出院登记</h2>
    <div class="hello">
      <form class="t">
        请选择科室名称:
        <select name="patient_dept" class="d1">
          <option value="dept.id">dept.dept_name</option>
        </select>
        <input type="submit" value="查询" formaction="/search_room/" formmethod="post" class="btn btn-default">
      </form>
      <table>
        <tr>
          <th>房&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</th>
          <th>病&nbsp;房&nbsp;状&nbsp;况</th>
        </tr>
        <tr>
          <td>1</td>
          <td>空</td>
        </tr>
      </table>
      <form class="t">
        请输入需要出院的病人的房号:<input type="text" name="out_id" class="d2">
        <input type="submit" value="确认" formaction="/out_hospital/" formmethod="post" class="btn btn-default">
      </form>
    </div>
    <form class="f">
      <input type="submit" value="返回上一级" formaction="/return4/" formmethod="get" class="btn1 btn-default">
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
.body {
  padding: 1px;
  height: calc(100vh);
  background: url("../../assets/img/out3.png");
  background-size: auto 100%;
}
h2 {
  text-align: center;
  font-size: 32px;
  margin-top: 30px;
  font-weight: bold;
}
.f {
  display: flex;
  margin-left: 100px;
}
.d1 {
  width: 100px;
  height: 40px;
  background-color: #8ee5ee;
  border-radius: 5px;
  margin-top: 18px;
}
.d2 {
  width: 100px;
  height: 35px;
  background-color: #8ee5ee;
  border-radius: 5px;
  margin-top: 18px;
}
.btn {
  width: 60px;
  height: 40px;
  background-color: #8ee5ee;
  border-radius: 5px;
}
.btn1 {
  width: 100px;
  height: 40px;
  background-color: #8ee5ee;
  border-radius: 5px;
  margin-left: 40px;
  margin-bottom: 120px;
}
.hello {
  width: 540px;
  height: 540px;
  margin-top: 30px;
  margin-left: 880px;
  font-family: "Roboto", "Lucida Grande", Verdana, Arial, sans-serif;
  font-size: 18px;
  background-color: rgba(3, 4, 5, 0.1);
}
.t {
  margin-left: 30px;
  margin-top: 40px;
}
table {
  margin-left: 130px;
  margin-top: 70px;
}
table th {
  background-color: rgba(7, 4, 5, 0.2);
  border-width: 1px;
  padding: 8px;
  border-style: solid;
  border-color: #999999;
  color: white;
}
table td {
  background-color: rgba(0, 0, 0, 0.2);
  border-width: 1px;
  padding: 8px;
  border-style: solid;
  border-color: #999999;
  color: white;
}
</style>
