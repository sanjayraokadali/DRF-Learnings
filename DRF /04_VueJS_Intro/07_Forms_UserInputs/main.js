var app = new Vue({

  el: '.app',
  data: {
    text:"",
    checker : false,
    city:"",
    comment: null,
    comments: [],
  },
  methods: {
    onSubmit() {

      if (this.comment != null ){
        var data = this.comment;
        this.comments.push(data);
        this.comment = null;

      }
      else{
        alert("Cannot post an empty Comment!");
      }
    },

  }
})
