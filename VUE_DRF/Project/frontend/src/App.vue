<template>
  <div id="app">

    <form @submit.prevent="addStudent">

      <input type="text" v-model="student.name"  placeholder="Enter your name">
      <input type="text" v-model="student.branch_name"  placeholder="Enter your branch">
      <input type="text" v-model="student.section" placeholder="Enter your section">

      <input type="submit" name="" value="Add">

    </form>

      <table>
        <th>Student</th>
        <th>Branch</th>
        <th>Section</th>
        <tr v-for="student in students" :key="student.id" >
          <td>{{ student.name }}</td>
          <td>{{ student.branch_name }}</td>
          <td>{{ student.section }}</td>
          <button type="button" class="btn btn-outline-light" name="button">X</button>
        </tr>

      </table>



  </div>
</template>

<script>


export default {
  name: 'App',
  data () {


    return {
      student:{
        'name':'',
        'branch_name':'',
        'section':''
      },
      students: []
    }

  },
  methods: {


    async addStudent(){

      let response = await fetch("http://127.0.0.1:8000/api/students/", {

        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      this.students.push(await response.json());

    },
    created() {
      let endpoint = fetch("http://127.0.0.1:8000/api/students/");
      this.students = endpoint.json();
    },

  }



}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin-top: 60px;
}
</style>
