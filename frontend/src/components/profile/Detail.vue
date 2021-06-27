<template>
  <div class="information">
    <p>Name: {{ dog.name }}</p>
    <p>Age: {{ dog.age }}</p>
    <p>Weight: {{ dog.weight }}kg</p>
    <p>Height: {{ dog.height }}cm</p>
    <p>Description: {{ dog.description }}</p>
  </div>
</template>

<script>
export default {
  props: ["dog"],
};
</script>

<style scoped>
div.information {
  height: 100%;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  text-align: left;
}

div.information p {
  font-size: 2rem;
  width: 100%;
}
</style>