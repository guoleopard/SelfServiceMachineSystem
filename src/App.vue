<script setup>
import Home from './views/Home.vue'
import Appointment from './views/Appointment.vue'
import PaymentMethodSelect from './views/PaymentMethodSelect.vue'
import PaymentList from './views/PaymentList.vue'
import PaymentDetail from './views/PaymentDetail.vue'
import PayMethodSelect from './views/PayMethodSelect.vue'
import PaymentSuccess from './views/PaymentSuccess.vue'
import { ref } from 'vue'

const currentView = ref('home')
const pageData = ref(null)

function navigateTo(view, data = null) {
  console.log('Navigating to:', view, 'with data:', data)
  currentView.value = view
  pageData.value = data
}
</script>

<template>
  <div id="app">
    <!-- Debug info -->
    <div style="position: fixed; top: 10px; left: 10px; background: rgba(0,0,0,0.8); color: white; padding: 10px; z-index: 9999; font-size: 12px;">
      Current View: {{ currentView }}
    </div>
    <div v-if="currentView === 'home'">
      <Home @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'appointment'">
      <Appointment @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'payment-method'">
      <PaymentMethodSelect @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'payment-list'">
      <PaymentList @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'payment-detail'">
      <PaymentDetail :paymentItems="pageData" @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'pay-method'">
      <PayMethodSelect :paymentData="pageData" @navigate="navigateTo" />
    </div>
    <div v-else-if="currentView === 'payment-success'">
      <PaymentSuccess :paymentResult="pageData" @navigate="navigateTo" />
    </div>
    <div v-else>
      <div class="error-page">
        <h1>未知页面: {{ currentView }}</h1>
        <button @click="navigateTo('home')">返回首页</button>
      </div>
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
