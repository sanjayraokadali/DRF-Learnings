<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <Header
      :counter="index"
      :quant = "questions"

    />
    <b-container class="bv-example-row">
      <b-row sm="6" offset="3" >
        <b-col><QuestionBox
            v-if="questions.length"
            :currentQuestion="questions[index]"
            :next="next"
            :index="index"
          />

        </b-col>
      </b-row>
    </b-container>

  </div>
</template>

<script>
import Header from './components/Header.vue'
import QuestionBox from './components/QuestionBox.vue'

export default {
  name: 'App',
  components: {
    Header,
    QuestionBox
  },
  data() {
    return {
      questions: [],
      index: 0,
    }

  },
  methods: {
    next(){
      if(this.index < this.questions.length-1){
        this.index++
      }

    }
  },
  mounted () {
    fetch("https://opentdb.com/api.php?amount=5&category=19&difficulty=easy&type=multiple", {
      method: 'get'
    })
    .then((response) => {
      return response.json();
    })
    .then((jsonData) => {
      this.questions = jsonData.results;
    })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
