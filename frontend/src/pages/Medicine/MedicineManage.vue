<template>
  <div class="body">
    <div id="bg">
      <div CLASS="head">
        <h2>药品管理</h2>
      </div>
      <div class="inf">
        <h3>所有药品信息表</h3>
        <input type="submit" value="添加新药材" class="tian btn-default">
        <table border="1">
          <tr>
            <td>药&nbsp;&nbsp;品&nbsp;&nbsp;名&nbsp;&nbsp;称</td>
            <td>药&nbsp;品&nbsp;数&nbsp;量</td>
          </tr>
          <tr>
            <td> name </td>
            <td> num </td>
          </tr>
        </table>
      </div>

      <div class="find">

        <p>请输入药品名称：</p><br>
        <form action="/search_medicine/" method="post">
          <input type="text" name="medicine_name" value=" medicine " formmethod="post"
            style="font-size: 18px ;width: 150px">
          <input type="submit" value="查找" class="btn0 btn-default">
        </form>
        <div class="hjk">
          <input type="submit" value="取药" class="btn1 btn-default" formaction="/add_medicine/" formmethod="get"
            id="btnt">
          <input type="submit" value="添加" class="btn1 btn-default" formaction="/add_medicine/" formmethod="get"
            id="btnt">
        </div>
        <table border="1" class="b">
          <tr>
            <td> result_key </td>
            <td> result_key </td>
          </tr>
          <tr>
            <td> result_value </td>
            <td> result_value </td>
          </tr>
        </table>
      </div>
    </div>
    <input type="submit" value="返回上一级" class="btn2 btn-default" />
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
.hjk {
  margin-top: 30px;
  width: 323px;
}
h2 {
  font-size: 32px;
  text-align: center;
  font-weight: bold;
}
h3 {
  font-size: 20px;
  text-align: center;
  font-weight: bold;
}
.body {
  height: calc(100vh);
  padding: 1px;
  background: url("../../assets/img/1234.png") no-repeat center center fixed;
  background-size: 100%;
  font-size: 18px;
}

.find {
  width: 350px;
  height: 350px;
  margin-left: 42%;
  margin-top: 7%;
  float: left;

  background-color: rgba(142, 229, 238, 0.2);
}

.find p {
  margin-top: 40px;
  margin-left: 20%;
}

.find form {
  margin-left: 20%;
}

.btn input {
  /*设置两个按钮的宽高、边距及边框样式*/
  width: 50px;
  height: 24px;
  margin-right: 50px;
  background: #87ceff;
  border-radius: 20px;
}

.btn0 {
  font-size: 16px;
  margin-right: 50px;
  background: #87ceff;
  border-radius: 20px;
}

#btnt {
  width: 80px;
  font-size: 16px;
  background: #87ceff;
  border-radius: 20px;
  margin-left: 50px;
}

.b {
  margin-top: 40px;
  margin-left: 25%;
}

.inf {
  position: relative;
  margin-top: 2%;
  margin-right: 12%;
  width: 200px;
  height: 400px;
  float: right;
}

.guodong {
  width: 250px;
  height: 350px;
  overflow: auto;
}

.btn2 {
  width: 120px;
  height: 50px;
  background: #87ceff;
  border-radius: 20px;
  position: absolute;
  left: 100px;
  top: 570px;
  font-size: 18px;
}

.tian {
  position: absolute;
  top: -8px;
  right: -86px;
  width: 100px;
  height: 35px;
  background: #87ceff;
  border-radius: 20px;
  font-size: 16px;
}

.head {
  position: relative;
  text-align: center;
  margin-top: 50px;
}

#bg {
  width: 100%;
  height: 300px;
  position: static;
}

table {
  border-collapse: collapse;
  margin: 20px auto;
  text-align: center;
  overflow: auto;
}

table td,
table th {
  border: 1px solid #cad9ea;
  color: black;
  height: 30px;
  line-height: 46px;
  padding: 0 10px;
}

table thead th {
  background-color: #cce8eb;
  width: 100px;
}

table tr:nth-child(odd) {
  background: #63b8ff;
}

table tr:nth-child(even) {
  background: #87ceff;
}
</style>
