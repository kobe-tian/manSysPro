<template>
  <div class="body">
    <div class="div1 hello">
      <form>
        <h5>目前已有{{length}}人挂号</h5>
        <div class="b">
          <span>请选择该病人的问诊号：</span>
          <select class="a" :v-model="num" @change="changeSelect">
            <option v-for="(item,key) in patient_all_id" :key="key"> {{item.id}}</option>
          </select>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <input class="input1 btn-success" type="button" value="确认" @click="queren">
        </div>
        <br><br>
        <table border="2">
          <tr>
            <th>姓&nbsp;&nbsp;&nbsp;名</th>
            <th>性&nbsp;&nbsp;&nbsp;别</th>
            <th>年&nbsp;&nbsp;&nbsp;龄</th>
            <th>电&nbsp;&nbsp;&nbsp;话</th>
            <th>科&nbsp;&nbsp;&nbsp;室</th>
          </tr>
          <tr>
            <td>{{patient_info.patient_name}}</td>
            <td>{{patient_info.patient_sex}}</td>
            <td>{{patient_info.patient_age}}</td>
            <td>{{patient_info.patient_telep}}</td>
            <td>{{patient_info.dept_name}}</td>
          </tr>
        </table>
        <br><br><br>
      </form>
    </div>
    <div class="div2 hello">
      <div class="tee">诊断结果：<input class="xian" type="text" v-model="form.diagnosis_result"></div>
      <br><br>
      <div class="tee">病房号：<input class="xian" type="text" v-model="form.room_id">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <input type="button" class="btn-success " value="分配病房" @click="fenpei"></div>
      <br><br>
      <div class="tee">
        药品1：
        <select name="medicine1" @change="changeSelect1">
          <option v-for="(item,key) in medicines" :key="key" :value="item">{{item}}
          </option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        剂量：<select class="select1" name="num1" @change="changeSelect11">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
        </select></div>
      <br><br>
      <div class="tee">
        药品2：
        <select name="medicine2" @change="changeSelect2">
          <option v-for="(item,key) in medicines" :key="key" :value="item">{{item}}</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        剂量：<select name="num2" class="select1" @change="changeSelect22">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
        </select></div>
      <br><br>
      <div class="tee">
        药品3：
        <select name="medicine3" @change="changeSelect3">
          <option v-for="(item,key) in medicines" :key="key" :value="item">{{item}}</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;剂量：<select name="num3" class="select1"
          @change="changeSelect33">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
        </select>
      </div>
    </div>
    <div class="div3 hello">
      医嘱：<input class="yizhu" type="text" name="doctor_suggestions" v-model="form.doctor_suggestions"><br><br>
      <div class="tee">
        问诊时间：<input class="xian" type="text" name="diagnosis_time" v-model="form.diagnosis_time">
      </div><br><br>
      <div class="tee">医生签名：<input class="xian2" type="text" name="doctor_name" v-model="form.doctor_name">
      </div><br>
    </div>
    <div class="inp">
      <input class="i1 btn-success" type="button" value="返回上一级" @click="back">
      <input class="i2 btn-success" type="button" value="打印病历单" @click="dayingbld(form)">
    </div>
    <br>
  </div>
</template>

<script>
export default {
  props: {

  },
  data () {
    return {
      patient_info: {},
      flag: 1,
      length: 0,
      medicines: [],
      patient_all_id: [1],
      tableNum: 0,
      num: 1,
      form: {
        patient_id: 1,
        diagnosis_result: '',
        room_id: '',
        doctor_suggestions: '',
        diagnosis_time: '',
        doctor_name: '',
        medicine1: '',
        medicine2: '',
        medicine3: '',
        num1: '',
        num2: '',
        num3: ''
      },
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
      this.$api.ruyuandengji().then(res => {
        if (res.status === 200) {
          const { data: { flag, length, medicines, patient_all_id, status } } = res
          this.flag = flag
          this.length = length
          this.medicines = medicines
          this.patient_all_id = patient_all_id
          this.status = status


          this.form = {
            patient_id: patient_all_id[0].id,
            diagnosis_result: '请输入',
            room_id: 1,
            doctor_suggestions: '请输入',
            diagnosis_time: '请输入',
            doctor_name: '请签名',
            medicine1: '123',
            medicine2: '123',
            medicine3: '123',
            num1: '1',
            num2: '1',
            num3: '1'
          }
        }
        console.log('res >>> ', res)
      })
    },
    changeSelect (select) {
      let value = select.srcElement.value
      this.num = select.srcElement.value
      this.form.patient_id = select.srcElement.value
      console.log('select >>> ', select.srcElement.value)
      this.tableChange(value)
    },
    changeSelect1 (select) {
      let value = select.srcElement.value
      this.medicine1 = value
      console.log('select >>> ', select.srcElement.value)
    },
    changeSelect2 (select) {
      let value = select.srcElement.value
      this.medicine2 = value
      console.log('select >>> ', select.srcElement.value)
    },
    changeSelect3 (select) {
      let value = select.srcElement.value
      this.medicine3 = value
      console.log('select >>> ', select.srcElement.value)
    },
    changeSelect11 (select) {
      let value = select.srcElement.value
      this.num1 = value
      console.log('select >>> ', select.srcElement.value)
    },
    changeSelect22 (select) {
      let value = select.srcElement.value
      this.num2 = value
      console.log('select >>> ', select.srcElement.value)
    },
    changeSelect33 (select) {
      let value = select.srcElement.value
      this.num3 = value
      console.log('select >>> ', select.srcElement.value)
    },
    tableChange (value) {
      this.tableNum = value - 1
      console.log('tableNum >>> ', this.tableNum)
    },
    fenpei () {
      this.$router.push('/SearchEmptyRoom')
    },
    dayingbld (form) {
      console.log('form >>> ', form)
      this.$api.dayinbinglidan(form).then(res => {
        console.log('res >>> ', res)
        if (res.status === 200) {
          alert('打印成功！')
        }
      })
    },
    back () {
      this.$router.push('/DoctorSelect')
    },
    queren () {
      this.$api.display({
        patient_id: this.num
      }).then(res => {
        console.log(res)
        this.patient_info = res.data.patient_info
      })
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.tee {
  display: flex;
}
.btn-success {
  background: #3fb33f;
  color: white;
}
.b {
  display: flex;
  margin-top: 20px;
  span {
    padding-top: 5px;
  }
}
table {
  border: 1px solid black;
  tr {
    border: 1px solid black;
    th {
      border: 1px solid black;
      width: 30px;
    }

    td {
      border: 1px solid black;
      width: 30px;
    }
  }
}
.a {
  width: 70px;
}
.xian {
  border-style: solid;
  border-top: 5px;
  border-left: 0px;
  border-right: 0px;
  width: 170px;
  height: 22px;
  text-align: center;
}
.xian2 {
  border-style: solid;
  border-top: 5px;
  border-left: 0px;
  border-right: 0px;
  height: 22px;
  width: 170px;
  font-family: 华文行楷;
  font-size: 20px;
  text-align: center;
}
.hello {
  background-color: white;
  border-style: solid;
  height: 535px;
  width: 525px;
  margin-left: 380px;
  opacity: 0.7;
  filter: alpha(opacity=0.5);
  border: 2px solid black;
}
.div1 {
  height: 160px;
  padding-top: 20px;
  padding-left: 40px;
  margin-left: 300px;
  width: 525px;
}
.div2 {
  height: 250px;
  padding-top: 45px;
  padding-left: 40px;
  width: 525px;
  margin-left: 300px;
}
.div3 {
  padding-top: 15px;
  padding-left: 40px;
  padding-right: 5px;
  width: 520px;
  height: 230px;
  margin-left: 300px;
}
.yizhu {
  height: 80px;
  width: 450px;
  font-family: 华文行楷;
  font-size: 25px;
}
h5 {
  text-align: left;
}
.i1 {
  float: left;
  width: 100px;
  height: 40px;
  background-color: cornflowerblue;
  border-radius: 5px;
  border-style: none;
}
.i2 {
  float: right;
  width: 100px;
  height: 40px;
  background-color: cornflowerblue;
  border-radius: 5px;
  border-style: none;
}
.inp {
  width: 1000px;
  margin-left: 50px;
}
.input3 {
  height: 36px;
  width: 100px;
  background-color: #8ee5ee;
}
.body {
  height: calc(100vh);
  padding: 1px;
  background: url("../../assets/img/diagnosis3.png") no-repeat center center
    fixed;
  background-size: 100%;
}
.input1 {
  height: 25px;
  width: 50px;
}
select {
  background-color: #8ee5ee;
}
.select1 {
  width: 60px;
  background-color: #8ee5ee;
}
.p1 {
  text-align: left;
}
</style>
