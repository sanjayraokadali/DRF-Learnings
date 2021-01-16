import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Question from "@/views/Question.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "questions/:slug",
    name:"Question",
    component: Question,
    props: true,
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
