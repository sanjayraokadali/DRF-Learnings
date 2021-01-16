<template>
  <div class="home">
    <div class="container">
      <h2>View Questions!</h2>
        <hr>
      <div v-for="question in questions" :key="question.pk">

          <p>Posted By: {{ question.author }}</p>
          <p>
              Question :
          <router-link
            :to="{ name : 'Question', params: { slug : question.slug } }"
          >
           {{ question.content }}
          </router-link>
          </p>
          <p>Answers : {{ question.answers_count }}</p>
          <hr>
      </div>
  </div>
</div>
</template>

<script>
import { apiService } from "@/common/api.service.js"

export default {
  name: "Home",
  data(){
    return {
      questions : []
    }
  },
  methods: {
    getQuestion() {
      let endpoint = '/api/questions';
      apiService(endpoint)
        .then(data => {
          this.questions.push(...data.results);
        })
    }
  },
  created() {
    this.getQuestion()
    console.log(this.questions)
  }
};

</script>
