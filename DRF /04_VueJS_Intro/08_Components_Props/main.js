Vue.component("comment",{

  props: {
    comment:{
      type:Object,
      required:true
    }
  },
  template:
  `
    <div>
      <p> {{ comment.username }} </p>
      <p> {{ comment.content }} </p>
      <hr>
    </div>
  `
})


var app  = new Vue({

  el: '.app',
  data: {
    comments: [
        { username:"Alice",content:"First Comment" },
        { username:"Bob",content:"Second Comment" },
        { username:"Casey",content:"Third Comment" },
        { username:"Den",content:"Fourth Comment" },
        { username:"Eli",content:"Fifth Comment" },
    ]
  }
})

Vue.component("trip",{

  props:{
    trip:{
      type:Object,
      required:true
    }
  },
  template:
  `
    <div>
      <ul>
        <li>{{ trip.location  }}</li>
        <li>{{ trip.days  }}</li>
        <li>{{ trip.rate  }}</li>
        <hr>
      </ul>
    </div>

  `

})


var trip  = new Vue({

  el: '.trip',
  data: {

    trips: [
        {
           location: "Goa",
           days:"5 Days",
           rate: 22000,
        },
        {
           location: "Delhi",
           days:"7 Days",
           rate: 20000,
        },
        {
           location: "Mumbai",
           days:"10 Days",
           rate: 30000,
        },
        {
           location: "Manali",
           days:"7 Days",
           rate: 25000,
        },
        {
           location: "Sikkim",
           days:"6 Days",
           rate: 30000,
        },

    ]

  }

})
