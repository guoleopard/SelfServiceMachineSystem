<script setup>
import { ref } from 'vue';
import HomePage from './components/HomePage.vue';
import AppointmentRegistration from './components/AppointmentRegistration.vue';

const currentPage = ref('home');

const navigateTo = (page) => {
  currentPage.value = page;
};
</script>

<template>
  <div id="app">
    <HomePage v-if="currentPage === 'home'" @navigate="navigateTo" />
    <AppointmentRegistration v-if="currentPage === 'appointment'" @back="navigateTo('home')" />
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow: hidden;
}

#app {
  width: 100vw;
  height: 100vh;
}
</style>
