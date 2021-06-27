<template>
  <img :src="url" />
</template>

<script>
export default {
  props: ["url"],
};
</script>

<style scoped>
img {
  width: auto;
  height: 100%;
}
</style>