<template>
  <div>
    <form>
      <div class="d">
        <input type="submit" class="btn-success" value="患者管理" formaction="/patient_manage/"
          formmethod="get"><br><br><br>
        <input type="submit" class="btn-success" value="值班查询" formaction="/work_time_search/"
          formmethod="get"><br><br><br>
        <input type="submit" class="btn-danger" value="退出" formaction="/exit/" formmethod="post">
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
div {
  margin-top: 160px;
  margin-left: 180px;
}
input {
  height: 60px;
  width: 160px;
  background-color: gainsboro;
  opacity: 0.7;
  filter: alpha(opacity=70);
  border-radius: 30px;
  font-size: 20px;
}
body {
  background: url("../../assets/img/select.jpg");
  background-size: 100%;
}
.d {
  margin-left: 5px;
}
</style>
