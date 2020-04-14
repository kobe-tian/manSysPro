<template>
  <div class="body">
    <div class="div1">
      <el-button type="primary" size="medium" @click="ruyuandengji">入院登记</el-button>
      <el-button type="primary" size="medium" @click="chuyuandengji">出院登记</el-button>
    </div>
    <div class="div2">
      <el-button type='success' size="medium" @click="back">返回上一级</el-button>
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
    ruyuandengji () {
      this.$router.push('/Diagnosis')
    },
    chuyuandengji () {

    },
    back () {

    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
input {
  border-radius: 30px;
  height: 60px;
  width: 160px;
  background-color: #63b8ff;
  opacity: 0.7;
  filter: alpha(opacity=70);
  font-size: 20px;
}

.body {
  position: relative;
  height: calc(100vh);
  padding: 1px;
  background: url(/static/img/out.1a85a8a.png) no-repeat center center fixed;
  background-size: auto 100%;

  .div1 {
    position: absolute;
    left: 300px;
    top: 170px;
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }

  .div2 {
    position: absolute;
    bottom: 50px;
    left: 20px;
  }
}

.a {
  padding: 1px 25px;
}

.b {
  padding: 1px 35px;
}
</style>
