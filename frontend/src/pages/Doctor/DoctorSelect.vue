<template>
  <div>
    <form>
      <div>
        <input type="submit" class="btn-info" value="入院登记" formaction="/patient_manage/"
          formmethod="post"><br><br><br><br>
        <input type="submit" class="btn-info b " value="出院登记" formaction="/out_hospital/" formmethod="get">
      </div><br><br><br><br><br><br><br><br><br><br>
      <input type="submit" class="btn-success a" value="返回上一级" formaction="/return1/" formmethod="get">
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
div {
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

body {
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
