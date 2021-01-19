
<template>

  <div class="container">
    <h2>QuestionBox</h2>
    <b-jumbotron header="BootstrapVue">
      <template #header></template>

    <template #lead>
      {{ currentQuestion.question }}
    </template>

    <hr class="my-4">

    <b-list-group class="container"  v-for="(answer,i) in answerList" :key="i">
      <b-list-group-item id="i" @click="alertMessage(answer)" :class="[ selectedAnswer === answer ? 'correct' : 'incorrect']" href="#" >{{ answer }}</b-list-group-item>
    </b-list-group>

    <br><br>

    <b-button style="opacity: 0.8;" variant="success" href="#">Submit</b-button><br><br>
    <b-button style="opacity: 0.7;" variant="danger" @click="next" >Next</b-button>
    </b-jumbotron>
  </div>

</template>


<script>

  export default{
    props:{
      currentQuestion: Object,
      next: Function,
      index: Number,
    },
    data(){
      return {
        selectedAnswer: null,
      }},
    computed:{
      answerList(){
        let answers = [...this.currentQuestion.incorrect_answers]
        answers.push(this.currentQuestion.correct_answer)
        return answers
      }
    },
    methods:{
      alertMessage(answer){

        if( answer == this.currentQuestion.correct_answer ){
          this.selectedAnswer = answer
          alert("Correct Answer")
        }else{
          alert("Wrong Answer")
        }

      }
    }
  }
</script>

<style scoped>
  .list-group{
    opacity: 0.7;
  }

  .list-group-item:hover{
    background-color: lightgray;
  }

  .correct {
    background-color: lightgreen;
    color: black;
  }

  .incorrect {
    background-color: red;
    color: white;
  }

</style>
