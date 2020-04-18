<template>
  <div class="body">
    <div class="hello">
      <form>
        <span>请选择科室名称:</span>
        <select name="patient_dept" class="b1">
          <option v-for="(item,key) in depts" :key="key" :value="item.id" @change="selectChange"> {{item.name}}
          </option>
        </select>
        <input type="button" value="查询" class="b2" @click="searchRoom(searchID)"><br><br>
      </form>
      <table>
        <tr>
          <th>房&nbsp;&nbsp;&nbsp;号</th>
          <th>入住&nbsp;&nbsp;&nbsp;状况</th>
        </tr>
        <tr v-for="(item,key) in dept_room_infos" :key="key">
          <td>{{item.room_id}}</td>
          <td>{{item.room_name}}</td>
        </tr>
      </table><br>
      <form>
        <input type="button" value="返回上一级" class="b3" @click="back">
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
      searchID: null,
      dept_room_infos: [],
      depts: [
        {
          id: 1,
          name: '神经'
        }
      ]
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
      this.$api.fenpeibingfang({
        diagnosis_result: '123'
      }).then(res => {
        console.log('res >>> ', res)
        if (res.status === 200) {
          this.depts = res.data.depts
          this.searchID = res.data.depts[0].id
          console.log('this.depts >>> ', this.depts)
        }
      })
    },
    // 查询空房
    searchRoom (id) {
      this.$api.chaxunkongfang({
        patient_dept: id
      }).then(res => {
        console.log('res >>> ', res)
        if (res.status === 200) {
          const { data } = res
          this.dept_room_infos = data.dept_room_infos
        }
      })
    },
    selectChange (select) {
      this.value = select.srcElement.value
      console.log('select >>> ', select.srcElement.value)
    },
    back () {
      this.$router.push('/Diagnosis')
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.hello {
  height: 340px;
  width: 360px;
  padding: 100px;
  background-color: steelblue;
  border-radius: 30px;
  margin: 100px auto;
}

.body {
  height: calc(100vh);
  padding: 1px;
  background: url("../../assets/img/5154.jpg_wh300.jpg") no-repeat;
  background-size: auto 100%;
}

table {
  border-radius: 5px;
  margin: 0 auto;
}

table th {
  background-color: rgba(7, 4, 5, 0.2);
  border-width: 1px;
  padding: 5px;
  border-style: solid;
  border-color: #999999;
  color: white;
}

table td {
  background-color: rgba(0, 0, 0, 0.2);
  border-width: 1px;
  padding: 5px;
  border-style: solid;
  border-color: #999999;
  color: white;
}

.b1 {
  width: 80px;
  height: 30px;
  background-color: #d3d3d3;
  border-radius: 5px;
  font-family: "微软雅黑 Light";
  font-size: 16px;
}

.b2 {
  width: 50px;
  height: 30px;
  background-color: #d3d3d3;
  border-radius: 5px;
  font-family: "微软雅黑 Light";
  font-size: 16px;
}

.b3 {
  width: 100px;
  height: 30px;
  background-color: #d3d3d3;
  border-radius: 5px;
  margin-left: 180px;
  font-family: "微软雅黑 Light";
  font-size: 16px;
}

span {
  font-family: "Adobe 宋体 Std L";
  font-size: 18px;
  color: white;
}
</style>
