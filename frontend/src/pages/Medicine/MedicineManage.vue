<template>
  <div class="body">
    <div id="bg">
      <div CLASS="head">
        <h2>药品管理</h2>
      </div>
      <div class="inf">
        <h3>所有药品信息表</h3>
        <input type="button" value="添加新药材" class="tian btn-default" @click="addNewMedicine">
        <table border="1">
          <tr>
            <td>药&nbsp;&nbsp;品&nbsp;&nbsp;名&nbsp;&nbsp;称</td>
            <td>药&nbsp;品&nbsp;数&nbsp;量</td>
          </tr>
          <tr v-for="(item,index) in medicine_inform" :key="index">
            <td> {{item.medicine_name}} </td>
            <td> {{item.medicine_num}} </td>
          </tr>
        </table>
      </div>

      <div class="find">

        <p>请输入药品名称：</p><br>
        <form action="/search_medicine/" method="post">
          <input type="text" name="medicine_name" v-model="keyword" style="font-size: 18px ;width: 150px">
          <input type="button" value="查找" class="btn0 btn-default" @click="searchM">
        </form>
        <div class="hjk">
          <input type="button" value="取药" class="btn1 btn-default" id="btnt" @click="quyao">
          <input type="button" value="添加" class="btn1 btn-default" id="btnt" @click="tianjia">
        </div>
        <table border="1" :class="cals">
          <tr>
            <td> 药品名称 </td>
            <td> 药品数量 </td>
          </tr>
          <tr>
            <td> {{result_values[0]}} </td>
            <td> {{result_values[1]}} </td>
          </tr>
        </table>
      </div>
    </div>
    <input type="button" value="返回上一级" class="btn2 btn-default" @click="back" />
  </div>
</template>

<script>
export default {
  props: {
  },
  data () {
    return {
      result_values: [1, 2],
      medicine_inform: [
        {
          medicine_name: "123",
          medicine_num: 123458167
        }
      ],
      keyword: '',
      medicine: null,
      cals: 'b hidden'
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
    back () {
      this.$router.go(-1)
    },
    go (url) {
      this.$router.push(url)
    },
    addNewMedicine () {
      this.go('/AddType')
    },
    init () {
      this.$api.medicine().then(res => {
        console.log(res)
        this.medicine_inform = res.data.medicine_inform
      })
    },
    searchM () {
      this.$api.searchMedicine({
        medicine_name: this.keyword
      }).then(res => {
        console.log(res)
        this.medicine = res.data.medicine
        console.log(this.medicine)
        this.result_values = res.data.result_values
        console.log('result_values >>> ', this.result_values)
        this.cals = 'b'
      })
    },
    quyao () {
      if (this.medicine !== null) {
        this.go(`/TakeMedicine?name=${this.medicine}`)
      }
      console.log(this.medicine)
    },
    tianjia () {
      if (this.medicine !== null) {
        this.go(`/AddMedicine?name=${this.medicine}`)
      }
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.hidden {
  display: none;
}
.hjk {
  margin-top: 30px;
  width: 323px;
}
h2 {
  font-size: 32px;
  text-align: center;
  font-weight: bold;
}
h3 {
  font-size: 20px;
  text-align: center;
  font-weight: bold;
}
.body {
  height: calc(100vh);
  padding: 1px;
  background: url("../../assets/img/1234.png") no-repeat center center fixed;
  background-size: 100%;
  font-size: 18px;
}

.find {
  width: 350px;
  height: 350px;
  margin-left: 42%;
  margin-top: 7%;
  float: left;

  background-color: rgba(142, 229, 238, 0.2);
}

.find p {
  margin-top: 40px;
  margin-left: 20%;
}

.find form {
  margin-left: 20%;
}

.btn input {
  /*设置两个按钮的宽高、边距及边框样式*/
  width: 50px;
  height: 24px;
  margin-right: 50px;
  background: #87ceff;
  border-radius: 20px;
}

.btn0 {
  font-size: 16px;
  margin-right: 50px;
  background: #87ceff;
  border-radius: 20px;
}

#btnt {
  width: 80px;
  font-size: 16px;
  background: #87ceff;
  border-radius: 20px;
  margin-left: 50px;
}

.b {
  margin-top: 40px;
  margin-left: 25%;
}

.inf {
  position: relative;
  margin-top: 2%;
  margin-right: 12%;
  width: 200px;
  height: 400px;
  float: right;
}

.guodong {
  width: 250px;
  height: 350px;
  overflow: auto;
}

.btn2 {
  width: 120px;
  height: 50px;
  background: #87ceff;
  border-radius: 20px;
  position: absolute;
  left: 100px;
  top: 570px;
  font-size: 18px;
}

.tian {
  position: absolute;
  top: -8px;
  right: -86px;
  width: 100px;
  height: 35px;
  background: #87ceff;
  border-radius: 20px;
  font-size: 16px;
}

.head {
  position: relative;
  text-align: center;
  margin-top: 50px;
}

#bg {
  width: 100%;
  height: 300px;
  position: static;
}

table {
  border-collapse: collapse;
  margin: 20px auto;
  text-align: center;
  overflow: auto;
}

table td,
table th {
  border: 1px solid #cad9ea;
  color: black;
  height: 30px;
  line-height: 46px;
  padding: 0 10px;
}

table thead th {
  background-color: #cce8eb;
  width: 100px;
}

table tr:nth-child(odd) {
  background: #63b8ff;
}

table tr:nth-child(even) {
  background: #87ceff;
}
</style>
