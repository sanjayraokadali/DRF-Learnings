<template>
    <div class="container">
      <b-nav tabs>
        <b-nav-item disabled> <strong>Fancy Quiz App</strong> </b-nav-item>
        <b-nav-item disabled>Counter: {{ counter+1 }}/{{ quant.length}}</b-nav-item>
      </b-nav>
    </div>

</template>

<script>

  export default {
      props: {
        counter: Number,
        quant : Array,
      }
    }

</script>
