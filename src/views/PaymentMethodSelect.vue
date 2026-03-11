<script setup>
import { ref, onMounted } from 'vue'
import CountdownTimer from '../components/CountdownTimer.vue'
import StepProgress from '../components/StepProgress.vue'
import LoadingSpinner from '../components/LoadingSpinner.vue'

const emit = defineEmits(['navigate'])

const loading = ref(false)

const paymentMethods = [
  { id: 1, name: '医保卡', icon: '💳', description: '请插入医保卡' },
  { id: 2, name: '身份证', icon: '🆔', description: '请放置身份证' },
  { id: 3, name: '电子医保凭证', icon: '📱', description: '请扫码电子医保凭证' }
]

function selectMethod(method) {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('navigate', 'payment-list')
  }, 1000)
}

function goHome() {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('navigate', 'home')
  }, 500)
}

function handleTimeout() {
  goHome()
}

onMounted(() => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
  }, 800)
})
</script>

<template>
  <div class="payment-method-container">
    <CountdownTimer @timeout="handleTimeout" />
    <LoadingSpinner :visible="loading" text="加载中..." />
    
    <div class="header">
      <button class="back-btn" @click="goHome">← 返回</button>
      <h1>请选择操作方式</h1>
    </div>
    
    <StepProgress :current-step="1" />

    <div class="main-content">
      <div class="methods-grid">
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
      <p>请选择您的身份验证方式</p>
    </div>
  </div>
</template>

<style scoped>
.payment-method-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.header {
  height: 100px;
  display: flex;
  align-items: center;
  padding: 0 40px;
  background: rgba(255, 255, 255, 0.1);
  position: relative;
}

.back-btn {
  position: absolute;
  left: 40px;
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 25px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s;
}

.back-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.header h1 {
  width: 100%;
  text-align: center;
  color: white;
  font-size: 28px;
  font-weight: 600;
}

.main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.methods-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  max-width: 900px;
}

.method-card {
  background: white;
  border-radius: 20px;
  padding: 50px 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.method-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.method-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.method-name {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.method-desc {
  font-size: 14px;
  color: #666;
  text-align: center;
}

.footer {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.1);
}

.footer p {
  color: white;
  font-size: 16px;
}
</style>
