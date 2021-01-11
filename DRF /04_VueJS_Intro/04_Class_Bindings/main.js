var app = new Vue({

  el: '.app',
  data:{
    flag:true,
    styleSquare:{
      backgroundColor:"green",
      borderColor:"yellow",
    }
  },
  methods:{
    changeColor(){
      this.flag = !this.flag;
    }
  }
})
