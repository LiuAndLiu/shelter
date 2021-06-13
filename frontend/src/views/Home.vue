<template>
  <div class="home">
    <HelloWorld v-bind:msg="message"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/home/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data() {
    return {
      message: "Hi there Vue."
    }
  }
}
</script>
