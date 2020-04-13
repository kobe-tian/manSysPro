<template>
  <div>
    <h2>添加药品</h2>
    <div>
      <div class="bg">
        <div class="b1">名称：<input value=" medicine_ " type="text" readonly></div><br>
        <div class="b2">请输入您要取的数量：<input type="text" value=" num " name="number"></div>
      </div>
      <div class="btn">
        <p class="btn1 btn-default"><input type="submit" value="确认" onclick="alert('添加药品成功！')"
            formaction="/add_medicine/" formmethod="post"></p>
        <p class="btn1 btn-default"><input type="submit" value="返回上一级" name="" formaction="/back1/" formmethod="get">
        </p>
      </div>
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
h2 {
  padding-left: 60%;
  margin-top: 4%;
}

input {
  width: 120px;
  font-size: 22px;
  border-radius: 5px;
}

body {
  background: url("../../assets/img/1234.png") no-repeat center center fixed;
  background-size: 100%;
  font-size: 28px;
}

.bg {
  width: 500px;
  height: 300px;
  margin-top: 5%;
  margin-left: 50%;
  background-color: rgba(142, 229, 238, 0.5);
}

.btn input {
  /*设置两个按钮的宽高、边距及边框样式*/
  width: 130px;
  height: 50px;
  background: #87ceff;
  border-radius: 20px;
  font-size: 18px;
}

.btn {
  margin-left: 83%;
}

.b1,
.b2 {
  margin-left: 15%;
  padding-top: 10%;
}
</style>
