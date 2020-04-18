<template>
  <div class="body">
    <h2>添加药品</h2>
    <div>
      <div class="bg">
        <div class="b1">请输入药品名称:<input type="text" name="m_name" v-model="name"></div><br>
        <div class="b2">请输入添加数量:<input type="text" name="m_num" v-model="number"></div>
      </div>
      <div class="btn">
        <p class="btn1 "><input type="submit" value="确认添加" class="btn-default" @click="add"></p>
        <p class="btn1 "><input type="submit" value="返回上一级" class="btn-default" style="margin-top:30px" @click="back">
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
      name: '',
      number: ''
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
    add () {
      this.$api.addNewM({
        m_name: this.name,
        m_num: this.number
      }).then(res => {
        console.log(res)
        alert('添加成功')
      })
    },
    back(){
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
