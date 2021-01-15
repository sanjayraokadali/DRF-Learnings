<template>

    <div class="example">
      <h1>This is an exmaple View!</h1>
      <h4>{{ message }}</h4>

    </div>
</template>

<script>
  export default {
      name: 'example',
      data() {
        return {
          message: "Example mmessage from data() func"
        }
      }
    }

</script>

<style scoped>
  h1{
    color: red;
    opacity: 0.5;
  }
</style>
