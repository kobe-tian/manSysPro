<template>
  <div>
    <form>
      <h2>添加新药材</h2>
      <div>名称：<input type="text" required></div><br>
      <div>数量：<input type="text" required></div>
      <div class="btn">
        <p class="btn1"><input type="submit" value="确认添加"></p>
        <p class="btn1"><input type="submit" value="返回上级"></p>
      </div>
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
  // background: url("../../assets/img/yanpin.jpg") no-repeat center center fixed;
  background-size: 100%;
}

form {
  width: 400px;
  height: 400px;
  margin: 200px auto;
}

.btn input {
  /*设置两个按钮的宽高、边距及边框样式*/
  width: 100px;
  height: 24px;
  margin-right: 100px;
  background: #f0f8ff;
  border-radius: 20px;
}

h2 {
  padding-left: 70px;
}

.btn {
  margin-left: 75%;
}

.btn1 {
  padding-top: 8px;
}

div {
  padding-top: 20px;
}
</style>
