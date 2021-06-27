<template>
  <nav>
    <router-link :to="{ name: 'Home' }">Home</router-link>
    <router-link :to="{ name: 'Profile' }">Profile</router-link>
  </nav>
</template>

<script>
export default {};
</script>

<style>
nav {
  height: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 1rem 0;
}

nav a {
  text-decoration: none;
  margin: 0 2rem;
  font-size: 1rem;
}
</style>