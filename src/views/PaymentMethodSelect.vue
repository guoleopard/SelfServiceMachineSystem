<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Loading from '../components/Loading.vue'
import StepIndicator from '../components/StepIndicator.vue'

const emit = defineEmits(['navigate'])

const countdown = ref(90)
const loading = ref(false)
let timer = null

const paymentMethods = [
  { id: 1, name: '医保卡', icon: '💳', description: '使用医保卡进行缴费' },
  { id: 2, name: '身份证', icon: '🆔', description: '使用身份证进行缴费' },
  { id: 3, name: '电子医保凭证', icon: '📱', description: '使用电子医保凭证进行缴费' }
]

function selectMethod(method) {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('navigate', 'payment-list')
  }, 500)
}

function goBack() {
  emit('navigate', 'home')
}

onMounted(() => {
  timer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(timer)
      emit('navigate', 'home')
    }
  }, 1000)
})

onUnmounted(() => {
  if (timer) {
    clearInterval(timer)
  }
})
</script>

<template>
  <div class="payment-method-container">
    <Loading v-if="loading" text="正在加载..." />
    <div class="header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <div class="title">选择缴费方式</div>
      <div class="countdown">{{ countdown }}s</div>
    </div>
    
    <StepIndicator :currentStep="1" />
    
    <div class="main-content">
      <div class="method-grid">
        <div
          v-for="method in paymentMethods"
          :key="method.id"
          class="method-card"
          @click="selectMethod(method)"
        >
          <div class="method-icon">{{ method.icon }}</div>
          <div class="method-name">{{ method.name }}</div>
          <div class="method-desc">{{ method.description }}</div>
        </div>
      </div>
    </div>
    
    <div class="footer">
      <p>请选择您的缴费方式</p>
    </div>
  </div>
</template>

<style scoped>
.payment-method-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

.header {
  height: 80px;
  background-color: #2c3e50;
  color: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 30px;
}

.back-btn {
  background: none;
  border: 1px solid white;
  color: white;
  padding: 8px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.back-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.title {
  font-size: 24px;
  font-weight: bold;
}

.countdown {
  font-size: 20px;
  background-color: #e74c3c;
  padding: 5px 15px;
  border-radius: 5px;
}

.main-content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
}

.method-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  max-width: 900px;
}

.method-card {
  background-color: white;
  border-radius: 15px;
  padding: 50px 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.method-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
  background-color: #3498db;
  color: white;
}

.method-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.method-name {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.method-desc {
  font-size: 14px;
  color: #666;
  text-align: center;
}

.method-card:hover .method-desc {
  color: rgba(255, 255, 255, 0.8);
}

.footer {
  height: 60px;
  background-color: #2c3e50;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
