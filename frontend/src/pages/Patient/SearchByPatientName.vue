<template>
  <div>
    <h2>病&nbsp;人&nbsp;信&nbsp;息</h2><br>
    <div>
      <table>
        <tr>
          <td><span>{{ result_key }}</span></td>
        </tr>
        <tr>
          <td><span>{{ result_value }}</span></td>
        </tr>
      </table>
      <form class="f">
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
body {
  background: url('../../assets/img/display.png') no-repeat center center fixed;
  background-size: 100%;
}

div {
  width: 900px;
  height: 400px;
  margin-left: 280px;
  margin-top: 10px;
  border-radius: 10px;
}

.f {
  width: 700px;
  height: 150px;
  margin-top: 130px;
  margin-left: 100px;
}

span {
  width: 100px;
  display: inline-block;
  /*将行内元素转换为行内块元素*/
}

table {
  border-radius: 5px;
  text-align: center;
  margin-top: 50px;
  margin-left: 140px;
}

table th {
  background-color: #f5fafa;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #63b8ff;
  color: black;
}

table td {
  background-color: cornflowerblue;
  border-width: 1px;
  padding: 3px;
  border-style: solid;
  border-color: #999999;
  color: black;
}

.a1 {
  width: 120px;
  height: 40px;
  float: right;
  background-color: cornflowerblue;
  border-radius: 10px;
  font-family: 'Adobe 宋体 Std L';
  font-size: 16px;
}

.a2 {
  width: 120px;
  height: 40px;
  margin-left: 40px;
  margin-top: 20px;
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
