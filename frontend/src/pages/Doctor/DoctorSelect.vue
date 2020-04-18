<template>
  <div class="body">
    <div>
      <form style="float: left;">
        <div class="hello">
          <input type="submit" class="btn-info" value="入院登记" formaction="/patient_manage/"
            formmethod="post"><br><br><br><br>
          <input type="submit" class="btn-info b " value="出院登记" formaction="/out_hospital/" formmethod="get">
        </div><br><br><br><br><br><br><br><br><br><br>
        <input type="submit" class="bfd btn-success a" value="返回上一级" formaction="/return1/" formmethod="get">
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
.bfd {
  background: green;
  color: white;
}
.hello {
  margin-top: 160px;
  margin-left: 350px;
}
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
  height: calc(100vh);
  padding: 1px;
  background: url("../../assets/img/out.png") no-repeat center center fixed;
  background-size: 100%;
}
.a {
  padding: 1px 25px;
}
.b {
  padding: 1px 35px;
}
</style>
