var app = new Vue({
  el: '.app',
  data: {
    first_name: "Sanjay",
    last_name: "Kadali",
  },
  computed: {
    ComputedNumber(){
      return Math.random();
    },
    getFullName(){
      return this.first_name + ' ' + this.last_name;
    },
    getReversedName(){
      first = this.first_name.split("").reverse().join("");
      last = this.last_name.split('').reverse().join('');

      return first + ' ' + last;
    }
  },
  methods: {
    FunctionedNumber(){
      return Math.random();
    }
  }
})
