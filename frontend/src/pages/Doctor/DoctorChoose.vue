<template>
  <div class="body">
    <form>
      <div class="d">
        <input class="btn-success" value="患者管理" @click="patientManage"><br><br><br>
        <input class="btn-success" value="值班查询" @click="queryDuty"><br><br><br>
        <input class="btn-danger" value="退出" @click="quit">
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
    patientManage () {
      this.$router.push('/DoctorSelect')
    },
    queryDuty () {
      this.$router.push('/')
    },
    quit () {
      this.$router.push('/')
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.body {
  background: url('../../assets/img/select.jpg');
  background-size: auto 100%;
  height: calc(100vh);
  padding: 1px;
}

form {
  margin-top: 160px;
}
.d {
  width: 500px;
  .btn-danger {
    background: red;
    border-color: unset;
  }
  input {
    text-align: center;
    color: #fff;
    background-color: #5cb85c;
    border-color: #4cae4c;
    cursor: pointer;
    height: 60px;
    width: 160px;
    opacity: 0.7;
    filter: alpha(opacity=70);
    border-radius: 30px;
    font-size: 20px;
    &:hover {
      color: #fff;
      background-color: #449d44;
      border-color: #398439;
    }
  }
}
</style>
