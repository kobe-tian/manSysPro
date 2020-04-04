<template id="body">
  <div id="login" :style="images">
    <input v-model="message" placeholder='UserName' id="kuang1">
    <p></p>
    <input v-model="message" placeholder="Password" id="kuang2">
  </div>

</template>

<script>
export default {
  name: 'UserLogin'
}
</script>

<style scoped>
#body {
  /*background-image: ;*/
  background-color: mediumorchid;
  background-size: 100%;
}
#login {
  font-family: "Roboto", "Lucida Grande", Verdana, Arial, sans-serif;
  font-size: 60px;
  color:dodgerblue;
  text-align: center;
  margin-top: 80px;
}
#sub1 {
  font-family:'Source Sans Pro', sans-serif;
  width: 120px;
  height: 40px;
  border-radius: 10px;
  margin-left: 40px
}
#sub2 {
  font-family:'Source Sans Pro', sans-serif;
  width: 80px;
  height: 30px;
  border-radius: 10px;
  margin-left: 40px;
  margin-top: 15px;
  float: right;
}
#kuang1 {
  width: 200px;
  height: 27px;
  border-radius: 8px;
  color:midnightblue;
  margin:50px 50px  50px 50px;
}
#kuang2 {
  width: 200px;
  height: 27px;
  border-radius: 8px;
  color:midnightblue;
  margin:10px 50px 50px 50px;
}
#btn {
    display: inline-block;
    padding: 6px 12px;
    margin-bottom: 0;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.42857143;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    -ms-touch-action: manipulation;
    touch-action: manipulation;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-image: none;
    border: 1px solid transparent;
    border-radius: 4px
}
#btn-success{
    color: #fff;
    background-color: #5cb85c;
    border-color: #4cae4c
}
</style>
