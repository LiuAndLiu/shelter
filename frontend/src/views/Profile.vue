<template>
  <div class="profile">
    <div v-if="dog" class="info">
      <div class="image">
        <Image :url="dog.url" />
      </div>
      <div class="details">
        <Detail :dog="dog" />
      </div>
    </div>
    <div class="selection">
      <button>Adopt!</button>
      <button @click="handleBack">Go back</button>
    </div>
  </div>
</template>

<script>
import Image from "@/components/profile/Image.vue";
import Detail from "@/components/profile/Detail.vue";

export default {
  props: ["id"],
  components: {
    Image,
    Detail,
  },
  data() {
    return {
      dog: null,
    };
  },
  mounted() {
    fetch(`http://localhost:3000/dogs/${this.id}`)
      .then((res) => res.json())
      .then((data) => (this.dog = data));
  },
  methods: {
    handleBack() {
      this.$router.push({ name: "Home" });
    },
  },
};
</script>

<style scoped>
div.profile {
  display: flex;
  align-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  width: 100%;
  height: 100%;
}

div.info {
  display: flex;
  align-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  width: 100%;
  height: 80%;
}

div.details {
  margin: auto;
  width: 40%;
  height: 90%;
}

div.image {
  margin: auto;
  width: 50%;
  height: 70%;
}

div.selection {
  width: 100%;
  height: 15%;
  display: flex;
  justify-content: space-around;
  align-content: center;
  align-items: center;
}

div.selection button {
  width: 40%;
  font-size: 2rem;
  height: 50%;
  cursor: pointer;
}
</style>