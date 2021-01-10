var app = new Vue({
  el: '.app',
  data: {
    message: "This is for learning Events and Methods.",
    link: 'http://www.google.com',
    packets: 0
  },
  methods: {
    onplus(){
      this.packets += 1;
      console.log(this.packets);
      if(this.packets > 10){
        alert("Cannot add more than 10!")
        this.packets = 0;
      }
    },
    onminus(){
      this.packets -= 1;
      console.log(this.packets);
      if(this.packets < 0){
        alert("nothing to remove!");
        this.packets  = 0;
      }
    }

  }
})

var app = new Vue({
  el: '.box',
  data: {
    box: 0,
  },
  methods: {
    addbox(){

      if(this.box % 2 == 0 ){
        console.log("It is Even: " + this.box)
      }
      else{
        console.log("It is Odd: " + this.box)
      }
      this.box += 1;
    }
  }
})

var app = new Vue({
  el: '.overthegreen',
  methods: {
    overthegreen() {
      console.log('Over the green Box!')
    }
  }
})
