<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>|
      <router-link to="/about">About</router-link>|
      <router-link :to="{name: 'login', params: {next: '/'}}">Login</router-link>|
      <router-link to="/createAccount">Create Account</router-link>|
      <router-link to="/account">Account Overview</router-link>|
      <router-link to="/manageProducts">Inventory</router-link>|
      <router-link to="/shop">Shop Online</router-link>
      <SideBar />
    </div>
    <router-view />

  </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';
export default {
    components: {
    SideBar
  }
};

</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 50px;
}

#nav a {
  font-weight: bold;
  color: #525252;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
