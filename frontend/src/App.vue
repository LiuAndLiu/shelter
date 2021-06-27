<template>
  <header>
    <Header />
  </header>
  <NavBar />
  <main>
    <router-view />
  </main>

  <footer>
    <Footer />
  </footer>
</template>

<script>
import NavBar from "@/components/foundation/NavBar.vue";
import Header from "@/components/foundation/Header.vue";
import Footer from "@/components/foundation/Footer.vue";

export default {
  components: { NavBar, Header, Footer },
};
</script>

<style>
* {
  border: 1px black solid;
}

html {
  font-size: 18px;
}

body {
  background-color: aliceblue;
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 80%;
  margin: 0 auto;
  height: auto;
}

header {
  height: 6rem;
}

main {
  height: 95vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

footer {
  height: 6rem;
}
</style>
