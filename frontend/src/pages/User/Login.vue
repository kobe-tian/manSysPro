<template>
  <div class="login">
    <h3>
      欢&nbsp;&nbsp;迎&nbsp;&nbsp;登&nbsp;&nbsp;录&nbsp;&nbsp;医&nbsp;&nbsp;院&nbsp;&nbsp;管&nbsp;&nbsp;理&nbsp;&nbsp;平&nbsp;&nbsp;台
    </h3>
    <div class="1">
      <form>
        <input type="text" class="kuang1" placeholder="Username" name="user_name"><br>
        <input type="password" class="kuang2" placeholder="Password" name="password"><br>
        <input type="submit" class="sub1 btn btn-success" value="Manager_login" formmethod="post"
          formaction="/new_login/">
        <input type="submit" class="sub1 btn btn-success" value="Doctor_login" formmethod="post"
          formaction="/doctor_login/">
        <input type="submit" value="regist" class="sub2 btn btn-success">
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

  },
  components: {

  }
}
</script>

<style scoped>
body {
  background-color: mediumorchid;
  background: url("../../assets/img/small.jpg") no-repeat center center fixed;
  background-size: 100%;
}

h3 {
  font-family: "Roboto", "Lucida Grande", Verdana, Arial, sans-serif;
  font-size: 60px;
  color: dodgerblue;
  text-align: center;
  margin-top: 80px;
}

.login {
  background-color: lightskyblue;
  margin-top: 90px;
  margin-left: 560px;
  width: 400px;
  height: 300px;
  border-radius: 20px;
}

.kuang1 {
  width: 200px;
  height: 27px;
  border-radius: 8px;
  color: midnightblue;
  margin: 50px 10px 50px 50px;
}

.kuang2 {
  width: 200px;
  height: 27px;
  border-radius: 8px;
  color: midnightblue;
  margin: 10px 50px 50px 50px;
}

.sub1 {
  font-family: "Source Sans Pro", sans-serif;
  width: 120px;
  height: 40px;
  border-radius: 10px;
  margin-left: 40px;
}

.sub2 {
  font-family: "Source Sans Pro", sans-serif;
  width: 80px;
  height: 30px;
  border-radius: 10px;
  margin-left: 40px;
  margin-top: 15px;
  float: right;
}
</style>
