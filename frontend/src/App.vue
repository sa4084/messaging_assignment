<template>
  <div id="app">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong style="color: white">Inbox</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <!-- <template v-if="$store.state.isAuthenticated">
        <span class="button is-primary is-info padding-email"><span id="user_email"></span></span>
      </template> -->
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">

        <div class="navbar-end">
          <!-- <router-link to="/log-in" class="navbar-item">Login</router-link> -->
          <!-- <router-link to="/profile" class="navbar-item">Profile</router-link> -->
          <div class="navbar-item">
            <div class="buttons">
              <!-- <router-link to="/compose" class="button is-light">Compose</router-link>
              <router-link to="/compose" class="button is-light">Compose</router-link> -->
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/compose" class="button is-light">Compose</router-link>
              </template>
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/sent" class="button is-light">Sent</router-link>
              </template>
              <!-- <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
              </template> -->
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-primary is-info padding-email">{{$store.state.email}}</router-link>
                <!-- <span class="button is-primary is-info padding-email"><span id="user_email"></span></span> -->
              </template>

              <template v-else>
                <router-link to="/sign-up" class="button is-light">Sign up</router-link>
              </template>

            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view />
      <!-- <HomePage msg="HELLO sent from app.vue"/> -->
    </section>

  </div>
</template>

<script>
import axios from "axios";

export default {
  // name: "App",
  // components: {
  //   HomePage,
  // },
  mounted() {
    // document.getElementById("user_email").innerHTML = $store.state.email;
    // let email = localStorage.getItem('email')
  },
  data() {
    return {
      showMobileMenu: false,
      // email: localStorage.getItem('email')
    }
  },
  beforeCreate() {
    this.$store.commit('initializeMessenger') // Called mutations in store
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";

// #app {
//   font-family: Avenir, Helvetica, Arial, sans-serif;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
//   text-align: center;
//   color: #2c3e50;
// }

// nav {
//   // padding: 30px;

//   a {
//     font-weight: bold;
//     color: #2c3e50;

//     &.router-link-exact-active {
//       color: #42b983;
//     }
//   }
// }
.padding-email {
  vertical-align: middle;
  text-align: center;
  margin: auto;
  color: black;
}
</style>

