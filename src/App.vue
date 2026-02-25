<script setup>
import Home from './views/Home.vue'
import Appointment from './views/Appointment.vue'
import PaymentFlow from './views/PaymentFlow.vue'
import { ref } from 'vue'

const currentView = ref('home')

function navigateTo(view) {
  currentView.value = view
}
</script>

<template>
  <div id="app">
    <div v-if="currentView === 'home'">
      <Home @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'appointment'">
      <Appointment @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'payment-flow'">
      <PaymentFlow @navigate="navigateTo" />
    </div>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Microsoft YaHei', sans-serif;
  background-color: #f5f5f5;
}

#app {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
