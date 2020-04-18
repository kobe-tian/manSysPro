<template>
  <div class="body">
    <h2>出院登记</h2>
    <div class="hello">
      <form class="t">
        请选择科室名称:
        <select name="patient_dept" class="d1" @change="changeSelect">
          <option v-for="(item,key) in dept" :key="key" :value="item.id">{{item.name}}</option>
        </select>
        <input type="button" value="查询" class="btn btn-default" @click="search">
      </form>
      <table>
        <tr>
          <th>房&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</th>
          <th>病&nbsp;房&nbsp;状&nbsp;况</th>
        </tr>
        <tr v-for="(item,key) in tableList" :key="key">
          <td>{{item.id}}</td>
          <td>{{item.name}}</td>
        </tr>
      </table>
      <form class="t">
        请输入需要出院的病人的房号:<input type="text" name="out_id" class="d2" v-model="typeRoom">
        <input type="button" value="确认" class="btn btn-default" @click="roomConfirm">
      </form>
    </div>
    <form class="f">
      <input type="button" value="返回上一级" class="btn1 btn-default" @click="go('DoctorSelect')">
    </form>
  </div>
</template>

<script>
export default {
  props: {

  },
  data () {
    return {
      keyword1: '初始化',
      typeRoom: '请输入',
      dept: [
        {
          name: '请稍等',
          id: 1
        },
      ],
      tableList: []
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
      this.$api.keshimingcheng().then(res => {
        console.log('res >> ', res)
        this.dept = res.data.depts
        this.keyword1 = res.data.depts[0].id
      })
    },
    search () {
      this.$api.keshimingchengSearch({
        patient_dept: this.keyword1
      }).then(res => {
        console.log('res >> ', res)
        this.tableList = res.data.dept_room_infos
      })
      console.log('查询' + this.keyword1)
    },
    changeSelect (select) {
      let value = select.srcElement.value
      this.keyword1 = select.srcElement.value
      console.log('select >>> ', select.srcElement.value)
    },
    roomConfirm () {
      this.$api.roomConfirm({
        out_id: this.typeRoom
      }).then(res => {
        console.log('res >>> ', res)
      })
      console.log('确认点击')
    },
    go (url) {
      this.$router.push(url)
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.body {
  padding: 1px;
  height: calc(100vh);
  background: url("../../assets/img/out3.png");
  background-size: auto 100%;
}
h2 {
  text-align: center;
  font-size: 32px;
  margin-top: 30px;
  font-weight: bold;
}
.f {
  display: flex;
  margin-left: 100px;
}
.d1 {
  width: 100px;
  height: 40px;
  background-color: #8ee5ee;
  border-radius: 5px;
  margin-top: 18px;
}
.d2 {
  width: 100px;
  height: 35px;
  background-color: #8ee5ee;
  border-radius: 5px;
  margin-top: 18px;
}
.btn {
  width: 60px;
  height: 40px;
  background-color: #8ee5ee;
  border-radius: 5px;
}
.btn1 {
  width: 100px;
  height: 40px;
  background-color: #8ee5ee;
  border-radius: 5px;
  margin-left: 40px;
  margin-bottom: 120px;
}
.hello {
  width: 540px;
  height: 540px;
  margin-top: 30px;
  margin-left: 880px;
  font-family: "Roboto", "Lucida Grande", Verdana, Arial, sans-serif;
  font-size: 18px;
  background-color: rgba(3, 4, 5, 0.1);
}
.t {
  margin-left: 30px;
  margin-top: 40px;
}
table {
  margin-left: 130px;
  margin-top: 70px;
}
table th {
  background-color: rgba(7, 4, 5, 0.2);
  border-width: 1px;
  padding: 8px;
  border-style: solid;
  border-color: #999999;
  color: white;
}
table td {
  background-color: rgba(0, 0, 0, 0.2);
  border-width: 1px;
  padding: 8px;
  border-style: solid;
  border-color: #999999;
  color: white;
}
</style>
