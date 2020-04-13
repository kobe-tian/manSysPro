<template>
  <div>
    <h2>科&nbsp;室&nbsp;病&nbsp;人&nbsp;信&nbsp;息</h2>
    <div>
      <table>
        <tr>
          <th><span>门诊&nbsp;&nbsp;号</span></th>
          <th><span>姓&nbsp;&nbsp;&nbsp;名</span></th>
          <th><span>性&nbsp;&nbsp;&nbsp;别</span></th>
          <th><span>年&nbsp;&nbsp;&nbsp;龄</span></th>
          <th><span>电&nbsp;&nbsp;&nbsp;话</span></th>
          <th><span>科&nbsp;&nbsp;&nbsp;室</span></th>
          <!--定义表头单元格应该横跨的列数-->
        </tr>
        <tr>
          <!--循环user_results中的数据输出 -->
          <td><span> patient_info.id </span></td>
          <td><span> patient_info.patient_name </span></td>
          <td><span> patient_info.patient_sex </span></td>
          <td><span> patient_info.patient_age </span></td>
          <td><span> patient_info.patient_telep </span></td>
          <td><span> patient_info.patient_dept.dept_name</span></td>
          <!--定义表头单元格应该横跨的列数-->
        </tr>
      </table>
      <form method="post" class="f">
        <input type="submit" class="a2 btn-info" value="继续查找" formaction="/search_p/" formmethod="post">
        <input type="submit" class="a1 btn-info" value="返回首页" formaction="/choose1/" formmethod="post">
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
body {
  background: url('../../assets/img/display.png') no-repeat center center fixed;
  background-size: 100%;
}

div {
  width: 900px;
  height: 400px;
  margin-left: 280px;
  margin-top: 20px;
  border-radius: 10px;
}

.f {
  width: 400px;
  height: 150px;
  margin-top: 80px;
  margin-left: 150px;
}

span {
  width: 100px;
  height: 20px;
  display: inline-block;
  /*将行内元素转换为行内块元素*/
}

table {
  border-radius: 5px;
  text-align: center;
  margin-top: 60px;
  margin-left: 150px;
  width: 10px;
}

table th {
  background-color: cornflowerblue;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #999999;
  color: black;
  width: 1px;
  text-align: center;
}

table td {
  background-color: #f5fafa;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #999999;
  color: black;
  width: 1px;
  text-align: center;
}

.a1 {
  width: 120px;
  height: 40px;
  margin-left: 60px;
  margin-top: 70px;
  background-color: cornflowerblue;
  border-radius: 10px;
  font-family: 'Adobe 宋体 Std L';
  font-size: 16px;
}

.a2 {
  position: absolute;
  width: 120px;
  height: 40px;
  left: 900px;
  top: 470px;
  background-color: cornflowerblue;
  border-radius: 10px;
  font-family: 'Adobe 宋体 Std L';
  font-size: 16px;
}

h2 {
  text-align: center;
  margin-top: 80px;
  font-family: 'Agency FB';
  font-size: 28px;
}
</style>
