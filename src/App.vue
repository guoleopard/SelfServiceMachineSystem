<script setup>
import Home from './views/Home.vue'
import Appointment from './views/Appointment.vue'
import PaymentMethodSelect from './views/PaymentMethodSelect.vue'
import PaymentList from './views/PaymentList.vue'
import PaymentDetail from './views/PaymentDetail.vue'
import PayMethodSelect from './views/PayMethodSelect.vue'
import PaymentComplete from './views/PaymentComplete.vue'
import { ref } from 'vue'

const currentView = ref('home')
const paymentData = ref(null)

function navigateTo(view, data = null) {
  currentView.value = view
  paymentData.value = data
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
    <div v-else-if="currentView === 'payment-select'">
      <PaymentMethodSelect @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'payment-list'">
      <PaymentList @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'payment-detail'">
      <PaymentDetail @navigate="navigateTo" :paymentData="paymentData" />
    </div>
    <div v-else-if="currentView === 'pay-method-select'">
      <PayMethodSelect @navigate="navigateTo" :paymentData="paymentData" />
    </div>
    <div v-else-if="currentView === 'payment-complete'">
      <PaymentComplete @navigate="navigateTo" :paymentData="paymentData" />
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
