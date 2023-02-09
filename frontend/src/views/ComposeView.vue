<template>
  <div class="about">
    <HelloWorld/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/ComposeTask.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
