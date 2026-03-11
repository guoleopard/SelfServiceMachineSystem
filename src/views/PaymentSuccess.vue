<script setup>
import { ref, onMounted } from 'vue'
import CountdownTimer from '../components/CountdownTimer.vue'
import StepProgress from '../components/StepProgress.vue'
import LoadingSpinner from '../components/LoadingSpinner.vue'

const props = defineProps({
  paymentResult: {
    type: Object,
    default: () => ({
      amount: 169.40,
      method: '微信支付'
    })
  }
})

const emit = defineEmits(['navigate'])

const loading = ref(false)
const paymentData = ref(props.paymentResult)
const countdownToHome = ref(5)
let timer = null

onMounted(() => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    startCountdown()
  }, 800)
})

function startCountdown() {
  timer = setInterval(() => {
    countdownToHome.value--
    if (countdownToHome.value <= 0) {
      clearInterval(timer)
      goHome()
    }
  }, 1000)
}

function goHome() {
  clearInterval(timer)
  emit('navigate', 'home')
}

function printReceipt() {
  alert('正在打印缴费凭证...')
}

function handleTimeout() {
  goHome()
}
</script>

<template>
  <div class="success-container">
    <CountdownTimer @timeout="handleTimeout" />
    <LoadingSpinner :visible="loading" text="加载中..." />
    
    <StepProgress :current-step="5" />
    
    <div class="main-content">
      <div class="success-card">
        <div class="success-icon">
          <div class="checkmark">
            <svg viewBox="0 0 52 52">
              <circle class="checkmark-circle" cx="26" cy="26" r="25" fill="none"/>
              <path class="checkmark-check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/>
            </svg>
          </div>
        </div>
        
        <h1 class="success-title">缴费成功</h1>
        <p class="success-subtitle">您的费用已成功支付</p>
        
        <div class="info-section">
          <div class="info-row">
            <span class="label">支付金额：</span>
            <span class="value highlight">¥ {{ paymentData.amount.toFixed(2) }}</span>
          </div>
          <div class="info-row">
            <span class="label">支付方式：</span>
            <span class="value">{{ paymentData.method }}</span>
          </div>
          <div class="info-row">
            <span class="label">支付时间：</span>
            <span class="value">{{ new Date().toLocaleString('zh-CN') }}</span>
          </div>
        </div>

        <div class="order-info">
          <p class="order-title">订单信息</p>
          <div class="order-item">
            <span>患者：张三</span>
            <span>就诊卡号：1234567890</span>
          </div>
          <div class="order-item">
            <span>科室：内科门诊</span>
            <span>医生：王医生</span>
          </div>
        </div>

        <div class="tips">
          <p>💡 温馨提示：</p>
          <ul>
            <li>请携带好您的随身物品</li>
            <li>如需发票，请前往收费窗口打印</li>
            <li>药品请到药房窗口领取</li>
          </ul>
        </div>

        <div class="button-group">
          <button class="btn secondary" @click="printReceipt">
            🖨️ 打印凭证
          </button>
          <button class="btn primary" @click="goHome">
            🏠 返回首页 ({{ countdownToHome }}s)
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.success-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.success-card {
  background: white;
  border-radius: 25px;
  padding: 50px;
  max-width: 500px;
  width: 100%;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
}

.success-icon {
  margin-bottom: 30px;
}

.checkmark {
  width: 100px;
  height: 100px;
  margin: 0 auto;
}

.checkmark-circle {
  stroke: #4CAF50;
  stroke-width: 2;
  stroke-dasharray: 166;
  stroke-dashoffset: 166;
  stroke-linecap: round;
  animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
}

.checkmark-check {
  stroke: #4CAF50;
  stroke-width: 3;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 48;
  stroke-dashoffset: 48;
  animation: stroke 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.4s forwards;
}

@keyframes stroke {
  100% {
    stroke-dashoffset: 0;
  }
}

.success-title {
  font-size: 32px;
  color: #333;
  margin: 0 0 10px 0;
}

.success-subtitle {
  color: #666;
  font-size: 16px;
  margin: 0 0 30px 0;
}

.info-section {
  background: #f8f9fa;
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 20px;
}

.info-row {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid #eee;
}

.info-row:last-child {
  border-bottom: none;
}

.info-row .label {
  color: #666;
}

.info-row .value {
  font-weight: 600;
  color: #333;
}

.info-row .value.highlight {
  color: #e74c3c;
  font-size: 20px;
}

.order-info {
  background: #e8f5e9;
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 20px;
  text-align: left;
}

.order-title {
  color: #2e7d32;
  font-weight: 600;
  margin: 0 0 15px 0;
}

.order-item {
  display: flex;
  justify-content: space-between;
  padding: 5px 0;
  color: #333;
  font-size: 14px;
}

.tips {
  background: #fff3e0;
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 30px;
  text-align: left;
}

.tips p {
  color: #f57c00;
  font-weight: 600;
  margin: 0 0 10px 0;
}

.tips ul {
  margin: 0;
  padding-left: 20px;
}

.tips li {
  color: #666;
  padding: 3px 0;
  font-size: 14px;
}

.button-group {
  display: flex;
  gap: 15px;
  justify-content: center;
}

.btn {
  padding: 15px 30px;
  border: none;
  border-radius: 30px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn.primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn.secondary {
  background: #f5f5f5;
  color: #333;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}
</style>
