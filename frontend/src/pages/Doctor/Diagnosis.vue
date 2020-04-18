<template>
  <div class="body">
    <div class="div1 hello">
      <form>
        <h5>目前已有{{data.length}}人挂号</h5>
        <div class="b">
          <span>请选择该病人的问诊号：</span>
          <select class="a" :v-model="num" @change="changeSelect">
            <option v-for="(item,key) in data.patient_all_id" :key="key"> {{item.id}}</option>
          </select>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <input class="input1 btn-success" type="button" value="确认">
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
            <td>{{data.patient_all_id[tableNum].name}}</td>
            <td>{{data.patient_all_id[tableNum].sex}}</td>
            <td>{{data.patient_all_id[tableNum].age}}</td>
            <td>{{data.patient_all_id[tableNum].telp}}</td>
            <td>{{data.patient_all_id[tableNum].dept}}</td>
          </tr>
        </table>
        <br><br><br>
      </form>
    </div>
    <div class="div2 hello">
      <div class="tee">诊断结果：<input class="xian" type="text" v-model="diagnosis_result"></div>
      <br><br>
      <div class="tee">病房号：<input class="xian" type="text" name="room_id">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <input type="button" class="btn-success " value="分配病房" @click="fenpei"></div>
      <br><br>
      <div class="tee">药品1：<select name="medicine1">
          <option></option>
          <option>medicine.medicine_name</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;剂量：<select class="select1" name="num1">
          <option></option>
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
        药品2：<select name="medicine2">
          <option></option>
          <option value="medicine.medicine_name">medicine.medicine_name</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;剂量：<select name="num2" class="select1">
          <option></option>
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
        药品3：<select name="medicine3">
          <option></option>
          <option value="medicine.medicine_name">medicine.medicine_name</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;剂量：<select name="num3" class="select1">
          <option></option>
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
      医嘱：<input class="yizhu" type="text" name="doctor_suggestions"><br><br>
      <div class="tee">
        问诊时间：<input class="xian" type="text" name="diagnosis_time">
      </div><br><br>
      <div class="tee">医生签名：<input class="xian2" type="text" name="doctor_name">
      </div><br>
    </div>
    <div class="inp">
      <input class="i1 btn-success" type="submit" value="返回上一级" formaction="/return2/" formmethod="get">
      <input class="i2 btn-success" type="submit" value="打印病历单" onclick="alert('打印成功！')"
        formaction="/insert_deal_method/" formmethod="post">
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
      diagnosis_result: '',
      tableNum: 0,
      num: 1,
      data: {
        length: 0,
        patient_all_id: [1]
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
      this.$api.ruyuandengji().then(res => {
        console.log('res >>> ', res)
        const { data } = res
        console.log('data >>> ', data)
        this.data = data
      })
    },
    changeSelect (select) {
      let value = select.srcElement.value
      this.num = select.srcElement.value
      console.log('select >>> ', select.srcElement.value)
      this.tableChange(value)
    },
    tableChange (value) {
      this.tableNum = value - 1
      console.log('tableNum >>> ', this.tableNum)
    },
    fenpei () {
      // console.log('开始分配病房')
      this.$router.push('/SearchEmptyRoom')
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
  background: url('../../assets/img/diagnosis3.png') no-repeat center center
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
