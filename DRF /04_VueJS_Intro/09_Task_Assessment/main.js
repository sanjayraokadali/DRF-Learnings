var app = new Vue({

  el: '.app',
  data: {
    tasks: [],
    task: null,
    task_count: 0
  },
  methods: {
    addTask(){
      if(this.task !=  null && this.task != ' ')
      {
        this.tasks.push(this.task);
        this.task_count += 1;
        this.task = null;
      }
      else
      {
        alert('Cannot Add Empty Task!')
      }
    },
    removeTask(){
      this.tasks.pop(this.task);
      this.task_count -= 1;
    }
  }
})
