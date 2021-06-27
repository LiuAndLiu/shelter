<template>
  <div>
    <List />
  </div>
</template>

<script>
// @ is an alias to /src
import List from "@/components/home/List.vue";

export default {
  name: "Home",
  components: { List },
};
</script>

<style scoped>
div {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  width: 100%;
}
</style>