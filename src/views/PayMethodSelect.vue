<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Loading from '../components/Loading.vue'
import StepIndicator from '../components/StepIndicator.vue'

const emit = defineEmits(['navigate'])
const props = defineProps({
  paymentData: {
    type: Object,
    default: () => ({})
  }
})

const loading = ref(true)
const countdown = ref(90)
let timer = null

const defaultData = {
  selfAmount: 76.50
}

const paymentData = ref(props.paymentData || defaultData)
const selectedMethod = ref(null)
const showQRCode = ref(false)
const qrCodeTimer = ref(null)

const payMethods = [
  { id: 1, name: '微信支付', icon: '💚', color: '#07c160' },
  { id: 2, name: '支付宝', icon: '💙', color: '#1677ff' }
]

function selectMethod(method) {
  selectedMethod.value = method
  showQRCode.value = true
  
  // 模拟扫码支付，3秒后自动完成
  qrCodeTimer.value = setTimeout(() => {
    emit('navigate', 'payment-complete', paymentData.value)
  }, 3000)
}

function goBack() {
  if (qrCodeTimer.value) {
    clearTimeout(qrCodeTimer.value)
  }
  emit('navigate', 'payment-detail', paymentData.value)
}

function cancelPay() {
  if (qrCodeTimer.value) {
    clearTimeout(qrCodeTimer.value)
  }
  showQRCode.value = false
  selectedMethod.value = null
}

onMounted(() => {
  // 模拟数据加载
  setTimeout(() => {
    loading.value = false
  }, 500)
  
  timer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(timer)
      if (qrCodeTimer.value) {
        clearTimeout(qrCodeTimer.value)
      }
      emit('navigate', 'home')
    }
  }, 1000)
})

onUnmounted(() => {
  if (timer) {
    clearInterval(timer)
  }
  if (qrCodeTimer.value) {
    clearTimeout(qrCodeTimer.value)
  }
})
</script>

<template>
  <div class="pay-method-container">
    <Loading v-if="loading" text="正在加载支付信息..." />
    <div class="header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <div class="title">选择支付方式</div>
      <div class="countdown">{{ countdown }}s</div>
    </div>
    
    <StepIndicator :currentStep="4" />
    
    <div class="main-content">
      <div class="amount-display">
        <p class="label">待支付金额</p>
        <p class="amount">¥{{ paymentData.selfAmount?.toFixed(2) }}</p>
      </div>
      
      <div v-if="!showQRCode" class="method-grid">
        <div
          v-for="method in payMethods"
          :key="method.id"
          class="method-card"
          :style="{ borderColor: method.color }"
          @click="selectMethod(method)"
        >
          <div class="method-icon">{{ method.icon }}</div>
          <div class="method-name">{{ method.name }}</div>
        </div>
      </div>
      
      <div v-else class="qrcode-section">
        <div class="qrcode-box">
          <div class="qrcode-title">请使用{{ selectedMethod?.name }}扫码支付</div>
          <div class="qrcode">
            <div class="qrcode-placeholder">
              <div class="scan-animation"></div>
            </div>
          </div>
          <p class="tip">扫码后请在手机上完成支付</p>
          <button class="cancel-btn" @click="cancelPay">取消支付</button>
        </div>
      </div>
    </div>
    
    <div class="footer">
      <p>请选择支付方式完成缴费</p>
    </div>
  </div>
</template>

<style scoped>
.pay-method-container {
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
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.amount-display {
  text-align: center;
  margin-bottom: 40px;
}

.amount-display .label {
  font-size: 18px;
  color: #666;
  margin-bottom: 10px;
}

.amount-display .amount {
  font-size: 48px;
  font-weight: bold;
  color: #e74c3c;
}

.method-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  max-width: 500px;
}

.method-card {
  background-color: white;
  border: 3px solid #ddd;
  border-radius: 15px;
  padding: 40px 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.method-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

.method-icon {
  font-size: 64px;
  margin-bottom: 15px;
}

.method-name {
  font-size: 20px;
  font-weight: bold;
  color: #333;
}

.qrcode-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.qrcode-box {
  background-color: white;
  border-radius: 15px;
  padding: 40px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  text-align: center;
}

.qrcode-title {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 30px;
}

.qrcode {
  width: 200px;
  height: 200px;
  margin: 0 auto 20px;
  position: relative;
}

.qrcode-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, #333 25%, transparent 25%),
              linear-gradient(-45deg, #333 25%, transparent 25%),
              linear-gradient(45deg, transparent 75%, #333 75%),
              linear-gradient(-45deg, transparent 75%, #333 75%);
  background-size: 20px 20px;
  background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
  border-radius: 10px;
  position: relative;
  overflow: hidden;
}

.scan-animation {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, transparent, #07c160, transparent);
  animation: scan 2s linear infinite;
}

@keyframes scan {
  0% { top: 0; }
  100% { top: 100%; }
}

.tip {
  color: #666;
  font-size: 14px;
  margin-bottom: 20px;
}

.cancel-btn {
  background-color: #95a5a6;
  color: white;
  border: none;
  padding: 10px 30px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.cancel-btn:hover {
  background-color: #7f8c8d;
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
