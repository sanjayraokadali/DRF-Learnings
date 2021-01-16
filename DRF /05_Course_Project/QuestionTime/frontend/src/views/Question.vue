<template>

  <div class="single-question mt-2">

    <div class="container">
      <h1>Question : {{ question.content }}</h1>
      <h2>Posted By: {{ question.author }}</h2>

    </div>

  </div>

</template>


<script>
import { apiService } from "@/common/api.service.js"
  export default {
    name: "Question",
    props: {
      slug: {
        type: String,
        required: true,
      }
    },
    data() {
      return {
        question: {}
      }
    },
    methods: {
      get_single_question(){

        let endpoint = '/api/questions/${this.slug}/';
        apiService(endpoint)
          .then(data => {
            this.question = data;
          })

      }
    },
    created() {
      this.get_single_question()
    }
}

</script>


<style>

</style>
