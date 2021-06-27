<template>
  <div v-if="dogs.length" class="list">
    <div v-for="dog in dogs" :key="dog.id" class="thumbnails">
      <Thumbnail :dog="dog" />
    </div>
  </div>
  <div v-else>
    <h1>{{ dogs.length }}</h1>
    <h1>Nothing to show</h1>
  </div>
</template>

<script>
import Thumbnail from "@/components/home/Thumbnail.vue";

export default {
  components: { Thumbnail },
  data() {
    return {
      dogs: [],
    };
  },
  mounted() {
    fetch("http://localhost:3000/dogs")
      .then((res) => res.json())
      .then((data) => (this.dogs = data));
  },
};
</script>

<style scoped>
div.list {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
}

div.thumbnails {
  background-color: white;
  height: 12rem;
  width: 9rem;
  margin: 0.5rem 1.5rem;
}
</style>