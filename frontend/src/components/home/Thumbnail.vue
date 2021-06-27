<template>
  <div class="thumbnail">
    <div @click="handleRedirect" class="image">
      <img :src="dog.url" :alt="dog.name" />
    </div>
    <div class="information">
      <p>Name: {{ dog.name }}</p>
      <p>Age: {{ dog.age }}</p>
      <p>Description: {{ dog.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["dog"],
  methods: {
    handleRedirect() {
      console.log("Redirecting");
    },
  },
};
</script>

<style scoped>
div.thumbnail {
  width: 100%;
  height: 100%;
}

div.image {
  display: flex;
  align-content: center;
  justify-content: center;
  overflow: hidden;
  width: auto;
  height: 65%;
}

div.information {
  height: 35%;
}

div.information p {
  margin: 0 0.15rem;
  height: 30%;
  font-size: 0.8rem;
  text-align: left;
  overflow: hidden;
}

img {
  width: auto;
  height: auto;
}
</style>