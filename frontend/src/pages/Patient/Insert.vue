<template>
  <div class="body">
    <div class="div1">
      <form>
        <h2>挂号单</h2>
        姓&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;名:<input class="input1" name="patient_name"
          v-model="form.patient_name"><br><br>

        年&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;龄:<input class="input1" name="patient_age"
          v-model="form.patient_age"> <br><br>

        身份证号:<input class="input1" name="patient_idcard" v-model="form.patient_idcard"><br><br>

        联系电话:<input class="input1" name="patient_telep" v-model="form.patient_telep"><br><br>
        性&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;别:
        <select class="select01" name="patient_sex" @change="changeSelect1">
          <option value="女">女</option>
          <option value="男">男</option>
        </select><br><br>
        科&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;室:
        <select class="select01" name="patient_dept" @change="changeSelect2">
          <option v-for="(item,index) in depts" :value="item.id" :key="index">{{item.name}}</option>
        </select><br><br>
        <input class="input02 " type="button" value="打印挂号单" @click="print">
        <input class="input02" type="button" value="返回上一级">
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
      depts: [],
      form: {
        patient_name: '',
        patient_sex: '',
        patient_age: '',
        patient_telep: '',
        patient_idcard: '',
        patient_dept: ''
      }
    }
  },
  computed: {

  },
  created () {
    this.init()
  },
  mounted () {

  },
  watch: {

  },
  methods: {
    init () {
      this.$api.guahao().then(res => {
        console.log(res)
        this.depts = res.data.depts
        this.form.patient_sex = '女'
        this.form.patient_dept = res.data.depts[0].id
      })
    },
    print () {
      this.$api.addPatient(this.form).then(res => {
        console.log(res)
        alert('打印成功！')
        this.$router.push(`/PrintPatient?id=${res.data.id}`)
      })
      // console.log(this.form)
    },
    changeSelect1 (select) {
      let value = select.srcElement.value
      this.form.patient_age = value
      console.log('select >>> ', select.srcElement.value)
    },
    changeSelect2 (select) {
      let value = select.srcElement.value
      this.form.patient_dept = value
      console.log('select >>> ', select.srcElement.value)
    },
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.body {
  padding: 1px;
  height: calc(100vh);
  background: url("../../assets/img/_500703205.jpg") no-repeat center center
    fixed;
  background-size: 100%;
}

.div1 {
  height: 460px;
  width: 350px;
  margin-left: 900px;
  margin-top: 100px;
  margin-bottom: 100px;
  background-color: gainsboro;
  opacity: 0.7;
  filter: alpha(opacity=70);
  padding-top: 10px;
  border-radius: 30px;
}

.input1 {
  width: 200px;
  height: 30px;
  border-style: solid;
  border-top: 0px;
  border-left: 0px;
  border-right: 0px;
  background-color: gainsboro;
  opacity: 0.7;
  filter: alpha(opacity=70);
}

.input02 {
  border-radius: 30px;
  height: 30px;
  width: 80px;
  border-color: black;
  margin-left: 200px;
}

.select01 {
  border-radius: 30px;
  border-color: dimgray;
  height: 28px;
  width: 110px;
  border-width: 2px;
}

h2 {
  text-align: center;
  font-size: 32px;
  font-weight: bold;
}
</style>
