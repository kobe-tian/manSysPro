<template>
  <div>
    <div class="b">
      <table border="2">
        <tr>
          <th>编&nbsp;&nbsp;&nbsp;号</th>
          <th align="center">姓&nbsp;&nbsp;&nbsp;名</th>
          <th>性&nbsp;&nbsp;&nbsp;别</th>
          <th>年&nbsp;&nbsp;&nbsp;龄</th>
          <th>电&nbsp;&nbsp;&nbsp;话</th>
          <th>职&nbsp;&nbsp;&nbsp;位</th>
          <th>科&nbsp;&nbsp;&nbsp;室</th>
          <td colspan="6"></td>
          <!--定义表头单元格应该横跨的列数-->
        </tr>
        <tr>
        <tr>
          <!--循环user_results中的数据输出 -->
          <td> Doctor_result.doctor_id </td>
          <td> Doctor_result.doctor_name </td>
          <td>Doctor_result.doctor_sex</td>
          <td>Doctor_result.doctor_age</td>
          <td>Doctor_result.doctor_telep</td>
          <td>Doctor_result.doctor_position</td>
          <td>Doctor_result.doctor_dept.dept_name</td>
        </tr>
      </table>
      <form action="/display/" method="post">
        <input type="text" name="test">
        <input type="submit" value="继续显示">
      </form>
    </div>
    <p>
      <div class="c">
        <table border="2">
          <tr>
            <th>姓&nbsp;&nbsp;&nbsp;名</th>
            <th>科&nbsp;&nbsp;&nbsp;长</th>
            <th>电&nbsp;&nbsp;&nbsp;话</th>
            <th>楼&nbsp;&nbsp;&nbsp;层</th>
            <td colspan="6"></td>
            <!--定义表头单元格应该横跨的列数-->
          </tr>
          <tr>
          <tr>
            <!--循环user_results中的数据输出 -->
            <td> Dept_result.dept_name </td>
            <td>Dept_result.dept_manager</td>
            <td>Doctor_result.dept_manager_telep</td>
            <td>Doctor_result.dept_floor</td>
          </tr>
        </table>
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
.b {
  width: 600px;
  height: 800px;
  background: red;
  position: absolute;
  left: 0;
}
.c {
  width: 600px;
  height: 800px;
  background: blue;
  float: right;
}
</style>
