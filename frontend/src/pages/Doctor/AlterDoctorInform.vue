<template>
  <div>
    <form>
      <h2>医生信息修改</h2>
      <div id="bg">
        编号：<input type="text" value="doctor_id" readonly><br>
        姓名：<input type="text" value="doctor_name" readonly><br>
        性别：<input type="text" value="doctor_sex" readonly><br>
        科室：<input type="text" value="doctor_dept.dept_name" readonly><br>
        年龄：<input type="text" value="doctor_age" name="age"><br>
        电话：<input type="text" value="doctor_telep" name="telep"><br>
        职位：<input type="text" value="doctor_position" name="position"><br>
      </div>
      <p class="btn">
        <p class="btn1"><input type="submit" value="确认修改" formaction="/back3/" formmethod="post"
            onclick="alert('修改成功')">
        </p>
        <p class="btn1 "> <input type="submit" value="返回上一级" formaction="/back3/" formmethod="get"></p>
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
body {
  background: url("../../assets/img/download.jpg") no-repeat center center fixed;
  background-size: 100%;
}

#bg {
  margin-left: 23%;
  margin-top: 8%;
}

form {
  background-color: rgba(100, 149, 237, 0.7);
  height: 520px;
  width: 550px;
  margin-left: 30%;
  margin-top: 5%;
  border-radius: 15px;
}

input {
  margin-top: 2%;
  font-size: 16px;
  height: 22px;
}

h2 {
  margin-left: 35%;
  margin-top: 5%;
  padding-top: 5%;
}

p {
  height: 22px;
  margin-top: 12px;
  font-size: 18px;
}

p span {
  width: 120px;
  display: inline-block;
  /*将行内元素转换为行内块元素*/
}

.btn input {
  /*设置两个按钮的宽高、边距及边框样式*/
  width: 110px;
  height: 30px;
  margin-right: 100px;
  background: #f0f8ff;
  border-radius: 20px;
}

.btn {
  margin-left: 65%;
  margin-top: 5%;
}

.btn1 {
  padding-top: 10px;
}

input {
  background-color: #8ee5ee;
  border-radius: 5px;
}
</style>
