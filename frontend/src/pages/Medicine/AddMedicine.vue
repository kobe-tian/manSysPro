<template>
  <div class="body">
    <h2>添加药品</h2>
    <div>
      <div class="bg">
        <div class="b1">名称：<input :value="this.$route.query.name" type="text" readonly></div><br>
        <div class="b2">请输入您要取的数量：<input type="text" v-model="number" name="number"></div>
      </div>
      <div class="btn">
        <p class="btn1 btn-default"><input type="button" value="确认" @click="tianyao"></p>
        <p class="btn1 btn-default"><input type="button" value="返回上一级" name="" style="margin-top:30px" @click="back">
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
      number: 0
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
    tianyao () {
      this.$api.tianyao({
        number: this.number
      }).then(res => {
        console.log(res)
        alert('添加成功！')
      })
    },
    back () {
      this.$router.go(-1)
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
h2 {
  margin-top: 4%;
}

input {
  width: 120px;
  font-size: 22px;
  border-radius: 5px;
}

.body {
  height: calc(100vh);
  padding: 1px;
  background: url("../../assets/img/1234.png") no-repeat center center fixed;
  background-size: 100%;
  font-size: 28px;
}

.bg {
  text-align: left;
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
