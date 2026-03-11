<script setup>
import { ref, onMounted } from 'vue'
import CountdownTimer from '../components/CountdownTimer.vue'
import StepProgress from '../components/StepProgress.vue'
import LoadingSpinner from '../components/LoadingSpinner.vue'

const props = defineProps({
  paymentData: {
    type: Object,
    default: () => ({
      selfPayAmount: 169.40
    })
  }
})

const emit = defineEmits(['navigate'])

const loading = ref(false)

const selfPayAmount = ref(parseFloat(props.paymentData?.selfPayAmount) || 169.40)
const showQrCode = ref(false)
const selectedMethod = ref(null)
const qrCodeTimer = ref(null)

const payMethods = [
  { id: 1, name: '微信支付', icon: '💚', color: '#07c160' },
  { id: 2, name: '支付宝', icon: '💙', color: '#1677ff' }
]

function selectMethod(method) {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    selectedMethod.value = method
    showQrCode.value = true
    
    qrCodeTimer.value = setTimeout(() => {
      emit('navigate', 'payment-success', {
        amount: selfPayAmount.value,
        method: method.name
      })
    }, 3000)
  }, 500)
}

function cancelPay() {
  showQrCode.value = false
  selectedMethod.value = null
  if (qrCodeTimer.value) {
    clearTimeout(qrCodeTimer.value)
  }
}

function goBack() {
  cancelPay()
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('navigate', 'payment-detail')
  }, 500)
}

function goHome() {
  cancelPay()
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('navigate', 'home')
  }, 500)
}

onMounted(() => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
  }, 800)
})

function handleTimeout() {
  cancelPay()
  goHome()
}
</script>

<template>
  <div class="pay-method-container">
    <CountdownTimer @timeout="handleTimeout" />
    <LoadingSpinner :visible="loading" text="加载中..." />
    
    <div class="header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <h1>选择支付方式</h1>
      <button class="home-btn" @click="goHome">🏠 首页</button>
    </div>
    
    <StepProgress :current-step="4" />

    <div class="main-content">
      <div class="amount-card">
        <p class="label">待支付金额</p>
        <p class="amount">¥ {{ selfPayAmount.toFixed(2) }}</p>
      </div>

      <div v-if="!showQrCode" class="methods-container">
        <p class="tip">请选择支付方式</p>
        <div class="methods-grid">
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
      </div>

      <div v-else class="qrcode-container">
        <div class="qrcode-box">
          <div class="qrcode-header">
            <span class="method-icon">{{ selectedMethod.icon }}</span>
            <span>{{ selectedMethod.name }}扫码支付</span>
          </div>
          <div class="qrcode">
            <div class="fake-qrcode">
              <div class="qrcode-pattern"></div>
              <div class="qrcode-pattern"></div>
              <div class="qrcode-pattern"></div>
              <div class="qrcode-pattern center"></div>
            </div>
          </div>
          <p class="qrcode-tip">请使用{{ selectedMethod.name }}扫描二维码</p>
          <p class="qrcode-amount">支付金额：¥ {{ selfPayAmount.toFixed(2) }}</p>
          <p class="countdown-tip">模拟支付中，3秒后自动完成...</p>
          <button class="cancel-btn" @click="cancelPay">取消支付</button>
        </div>
      </div>
    </div>

    <div class="footer">
      <p>请在90秒内完成支付，超时将自动返回首页</p>
    </div>
  </div>
</template>

<style scoped>
.pay-method-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f7fa;
}

.header {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  position: relative;
}

.back-btn, .home-btn {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 25px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s;
}

.back-btn:hover, .home-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.header h1 {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  color: white;
  font-size: 24px;
  font-weight: 600;
  margin: 0;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.amount-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  padding: 30px 60px;
  text-align: center;
  color: white;
  margin-bottom: 40px;
  box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
}

.amount-card .label {
  font-size: 16px;
  margin: 0 0 10px 0;
  opacity: 0.9;
}

.amount-card .amount {
  font-size: 48px;
  font-weight: bold;
  margin: 0;
}

.methods-container {
  width: 100%;
  max-width: 600px;
}

.methods-container .tip {
  text-align: center;
  color: #666;
  font-size: 18px;
  margin-bottom: 30px;
}

.methods-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
}

.method-card {
  background: white;
  border: 3px solid #ddd;
  border-radius: 20px;
  padding: 40px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
}

.method-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.method-icon {
  font-size: 64px;
  margin-bottom: 15px;
}

.method-name {
  font-size: 20px;
  font-weight: 600;
  color: #333;
}

.qrcode-container {
  width: 100%;
  max-width: 400px;
}

.qrcode-box {
  background: white;
  border-radius: 20px;
  padding: 40px;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
}

.qrcode-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  font-size: 20px;
  font-weight: 600;
  color: #333;
  margin-bottom: 30px;
}

.qrcode-header .method-icon {
  font-size: 32px;
  margin: 0;
}

.qrcode {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.fake-qrcode {
  width: 200px;
  height: 200px;
  background: white;
  border: 1px solid #ddd;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-template-rows: repeat(7, 1fr);
  gap: 2px;
  padding: 10px;
}

.qrcode-pattern {
  background: #333;
  border-radius: 2px;
}

.qrcode-pattern:nth-child(1) { grid-area: 1 / 1 / 3 / 3; }
.qrcode-pattern:nth-child(2) { grid-area: 1 / 6 / 3 / 8; }
.qrcode-pattern:nth-child(3) { grid-area: 6 / 1 / 8 / 3; }
.qrcode-pattern.center { 
  grid-area: 3 / 3 / 6 / 6; 
  background: linear-gradient(45deg, #333 25%, transparent 25%),
              linear-gradient(-45deg, #333 25%, transparent 25%),
              linear-gradient(45deg, transparent 75%, #333 75%),
              linear-gradient(-45deg, transparent 75%, #333 75%);
  background-size: 10px 10px;
}

.qrcode-tip {
  color: #666;
  font-size: 14px;
  margin: 10px 0;
}

.qrcode-amount {
  color: #e74c3c;
  font-size: 24px;
  font-weight: bold;
  margin: 15px 0;
}

.countdown-tip {
  color: #999;
  font-size: 12px;
  margin: 10px 0;
}

.cancel-btn {
  background: #f5f5f5;
  border: none;
  color: #666;
  padding: 10px 30px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  margin-top: 15px;
  transition: all 0.3s;
}

.cancel-btn:hover {
  background: #e0e0e0;
}

.footer {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
}

.footer p {
  color: #999;
  font-size: 14px;
  margin: 0;
}
</style>
