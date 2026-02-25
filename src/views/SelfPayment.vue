<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

const emit = defineEmits(['navigate'])

const currentStep = ref(1)
const countdown = ref(90)
const loading = ref(false)
const loadingText = ref('加载中...')
let countdownTimer = null

const authMethods = [
  { id: 1, name: '医保卡', icon: '💊' },
  { id: 2, name: '身份证', icon: '🪪' },
  { id: 3, name: '电子医保凭证', icon: '📱' }
]
const selectedAuthMethod = ref(null)

const mockPaymentItems = [
  { id: 1, name: '门诊挂号费', amount: 25.00, type: '挂号', date: '2024-01-15' },
  { id: 2, name: '血常规检查', amount: 35.50, type: '检查', date: '2024-01-15' },
  { id: 3, name: 'CT扫描', amount: 280.00, type: '检查', date: '2024-01-15' },
  { id: 4, name: '阿莫西林胶囊', amount: 18.50, type: '药品', date: '2024-01-15' },
  { id: 5, name: '维生素C片', amount: 12.00, type: '药品', date: '2024-01-15' },
  { id: 6, name: '诊疗费', amount: 50.00, type: '诊疗', date: '2024-01-15' }
]

const selectedItems = ref([])
const paymentDetail = ref(null)

const paymentMethods = [
  { id: 1, name: '微信支付', icon: '💚' },
  { id: 2, name: '支付宝', icon: '💙' }
]
const selectedPaymentMethod = ref(null)

const patientInfo = ref({
  name: '张三',
  cardNo: '8821456789',
  idCard: '310***********1234'
})

function startCountdown() {
  stopCountdown()
  countdown.value = 90
  countdownTimer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      goHome()
    }
  }, 1000)
}

function stopCountdown() {
  if (countdownTimer) {
    clearInterval(countdownTimer)
    countdownTimer = null
  }
}

watch(currentStep, () => {
  startCountdown()
})

function selectAuthMethod(method) {
  selectedAuthMethod.value = method
  showLoading('正在验证信息...', () => {
    currentStep.value = 2
  })
}

function toggleSelectItem(item) {
  const index = selectedItems.value.findIndex(i => i.id === item.id)
  if (index > -1) {
    selectedItems.value.splice(index, 1)
  } else {
    selectedItems.value.push(item)
  }
}

function isItemSelected(item) {
  return selectedItems.value.some(i => i.id === item.id)
}

function goToDetail() {
  if (selectedItems.value.length === 0) {
    alert('请选择至少一个缴费项目')
    return
  }
  showLoading('正在核算费用...', () => {
    const totalAmount = selectedItems.value.reduce((sum, item) => sum + item.amount, 0)
    paymentDetail.value = {
      items: [...selectedItems.value],
      totalAmount: totalAmount,
      insuranceAmount: totalAmount * 0.7,
      selfAmount: totalAmount * 0.3
    }
    currentStep.value = 3
  })
}

function selectPaymentMethod(method) {
  selectedPaymentMethod.value = method
  showLoading('正在生成支付码...', () => {
    currentStep.value = 4
  })
}

function simulatePayment() {
  loading.value = true
  loadingText.value = '正在支付...'
  setTimeout(() => {
    loading.value = false
    currentStep.value = 5
  }, 2000)
}

function showLoading(text, callback) {
  loading.value = true
  loadingText.value = text
  setTimeout(() => {
    loading.value = false
    if (callback) callback()
  }, 800)
}

function goBackWithLoading() {
  if (currentStep.value > 1) {
    showLoading('返回中...', () => {
      currentStep.value--
    })
  } else {
    goHome()
  }
}

function goHome() {
  stopCountdown()
  emit('navigate', 'home')
}

function goBack() {
  goBackWithLoading()
}

onMounted(() => {
  startCountdown()
})

onUnmounted(() => {
  stopCountdown()
})
</script>

<template>
  <div class="payment-container">
    <div v-if="loading" class="loading-overlay">
      <div class="loading-spinner"></div>
      <div class="loading-text">{{ loadingText }}</div>
    </div>

    <div class="payment-header">
      <button class="back-btn" @click="goBack">←</button>
      <div class="title">自助缴费</div>
      <div class="countdown" :class="{ warning: countdown <= 30 }">
        {{ countdown }}s
      </div>
    </div>

    <div class="step-indicator">
      <div :class="['step', { active: currentStep >= 1 }]">1. 选择认证方式</div>
      <div :class="['step', { active: currentStep >= 2 }]">2. 选择缴费项目</div>
      <div :class="['step', { active: currentStep >= 3 }]">3. 缴费详情</div>
      <div :class="['step', { active: currentStep >= 4 }]">4. 扫码支付</div>
      <div :class="['step', { active: currentStep >= 5 }]">5. 支付完成</div>
    </div>

    <div class="payment-content">
      <Transition name="slide" mode="out-in">
      <div v-if="currentStep === 1" key="step1" class="step-content">
        <h2>请选择认证方式</h2>
        <div class="auth-methods">
          <div
            v-for="method in authMethods"
            :key="method.id"
            class="auth-card"
            @click="selectAuthMethod(method)"
          >
            <div class="auth-icon">{{ method.icon }}</div>
            <div class="auth-name">{{ method.name }}</div>
          </div>
        </div>
      </div>
      </Transition>

      <Transition name="slide" mode="out-in">
      <div v-if="currentStep === 2" key="step2" class="step-content">
        <div class="patient-card">
          <div class="patient-info">
            <span class="label">患者：</span>
            <span class="value">{{ patientInfo.name }}</span>
          </div>
          <div class="patient-info">
            <span class="label">卡号：</span>
            <span class="value">{{ patientInfo.cardNo }}</span>
          </div>
        </div>
        <h2>请选择缴费项目</h2>
        <div class="payment-list">
          <div
            v-for="item in mockPaymentItems"
            :key="item.id"
            :class="['payment-item', { selected: isItemSelected(item) }]"
            @click="toggleSelectItem(item)"
          >
            <div class="item-check">
              <span v-if="isItemSelected(item)">✓</span>
            </div>
            <div class="item-info">
              <div class="item-name">{{ item.name }}</div>
              <div class="item-meta">
                <span class="item-type">{{ item.type }}</span>
                <span class="item-date">{{ item.date }}</span>
              </div>
            </div>
            <div class="item-amount">¥{{ item.amount.toFixed(2) }}</div>
          </div>
        </div>
        <div class="selected-summary" v-if="selectedItems.length > 0">
          <span>已选择 {{ selectedItems.length }} 项</span>
          <span class="summary-amount">合计: ¥{{ selectedItems.reduce((s, i) => s + i.amount, 0).toFixed(2) }}</span>
        </div>
        <button class="next-btn" @click="goToDetail" :disabled="selectedItems.length === 0">
          下一步
        </button>
      </div>
      </Transition>

      <Transition name="slide" mode="out-in">
      <div v-if="currentStep === 3" key="step3" class="step-content">
        <h2>缴费详情</h2>
        <div class="detail-card">
          <div class="detail-list">
            <div v-for="item in paymentDetail.items" :key="item.id" class="detail-item">
              <span>{{ item.name }}</span>
              <span>¥{{ item.amount.toFixed(2) }}</span>
            </div>
          </div>
          <div class="detail-total">
            <div class="total-row">
              <span>总金额</span>
              <span>¥{{ paymentDetail.totalAmount.toFixed(2) }}</span>
            </div>
            <div class="total-row insurance">
              <span>医保统筹</span>
              <span>-¥{{ paymentDetail.insuranceAmount.toFixed(2) }}</span>
            </div>
            <div class="total-row self-payment">
              <span>自付金额</span>
              <span class="highlight">¥{{ paymentDetail.selfAmount.toFixed(2) }}</span>
            </div>
          </div>
        </div>
        <h3 style="text-align: center; margin: 20px 0;">请选择支付方式</h3>
        <div class="payment-methods">
          <div
            v-for="method in paymentMethods"
            :key="method.id"
            class="payment-method-card"
            @click="selectPaymentMethod(method)"
          >
            <span class="method-icon">{{ method.icon }}</span>
            <span class="method-name">{{ method.name }}</span>
          </div>
        </div>
      </div>
      </Transition>

      <Transition name="slide" mode="out-in">
      <div v-if="currentStep === 4" key="step4" class="step-content">
        <div class="qrcode-container">
          <h2>{{ selectedPaymentMethod?.name }}</h2>
          <div class="qrcode-box">
            <div class="fake-qrcode">
              <div class="qrcode-pattern"></div>
              <div class="qrcode-text">请扫描二维码</div>
            </div>
          </div>
          <p class="amount-display">
            支付金额: <span class="amount">¥{{ paymentDetail?.selfAmount.toFixed(2) }}</span>
          </p>
          <p class="payment-tip">请使用{{ selectedPaymentMethod?.name }}扫描上方二维码完成支付</p>
          <button class="simulate-btn" @click="simulatePayment">模拟支付成功</button>
        </div>
      </div>
      </Transition>

      <Transition name="slide" mode="out-in">
      <div v-if="currentStep === 5" key="step5" class="step-content">
        <div class="success-message">
          <div class="success-icon">✅</div>
          <h2>支付成功！</h2>
          <div class="success-detail">
            <p>支付金额: ¥{{ paymentDetail?.selfAmount.toFixed(2) }}</p>
            <p>支付方式: {{ selectedPaymentMethod?.name }}</p>
          </div>
          <div class="receipt-info">
            <p>📄 缴费凭证已自动打印</p>
          </div>
          <button class="home-btn" @click="goHome">返回首页</button>
        </div>
      </div>
      </Transition>
    </div>
  </div>
</template>

<style scoped>
.payment-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
}

.payment-header {
  height: 80px;
  background-color: #2c3e50;
  color: white;
  display: flex;
  align-items: center;
  padding: 0 20px;
  position: relative;
}

.back-btn {
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
  padding: 10px;
}

.title {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  font-size: 24px;
  font-weight: bold;
}

.countdown {
  position: absolute;
  right: 20px;
  font-size: 24px;
  font-weight: bold;
  color: #4CAF50;
}

.countdown.warning {
  color: #f44336;
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.step-indicator {
  height: 60px;
  background-color: #ecf0f1;
  display: flex;
  align-items: center;
  padding: 0 10px;
  gap: 5px;
  overflow-x: auto;
}

.step {
  flex: 1;
  text-align: center;
  padding: 8px 5px;
  border-radius: 5px;
  background-color: #bdc3c7;
  color: white;
  font-size: 12px;
  white-space: nowrap;
  min-width: 100px;
}

.step.active {
  background-color: #3498db;
}

.payment-content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.step-content {
  max-width: 600px;
  margin: 0 auto;
}

.step-content h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #2c3e50;
  font-size: 24px;
}

.auth-methods {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.auth-card {
  background-color: #ecf0f1;
  border-radius: 15px;
  padding: 30px;
  display: flex;
  align-items: center;
  gap: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.auth-card:hover {
  transform: translateY(-3px);
  background-color: #3498db;
  color: white;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

.auth-icon {
  font-size: 48px;
}

.auth-name {
  font-size: 22px;
  font-weight: 600;
}

.patient-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 20px;
  color: white;
}

.patient-info {
  display: flex;
  margin-bottom: 8px;
}

.patient-info:last-child {
  margin-bottom: 0;
}

.patient-info .label {
  opacity: 0.9;
}

.patient-info .value {
  font-weight: 600;
}

.payment-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}

.payment-item {
  background-color: #f8f9fa;
  border-radius: 12px;
  padding: 15px;
  display: flex;
  align-items: center;
  gap: 15px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.payment-item:hover {
  background-color: #e9ecef;
}

.payment-item.selected {
  background-color: #e3f2fd;
  border-color: #3498db;
}

.item-check {
  width: 28px;
  height: 28px;
  border: 2px solid #bdc3c7;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  color: white;
}

.payment-item.selected .item-check {
  background-color: #3498db;
  border-color: #3498db;
}

.item-info {
  flex: 1;
}

.item-name {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 5px;
}

.item-meta {
  display: flex;
  gap: 15px;
  font-size: 14px;
  color: #7f8c8d;
}

.item-amount {
  font-size: 20px;
  font-weight: bold;
  color: #e74c3c;
}

.selected-summary {
  background-color: #3498db;
  color: white;
  padding: 15px 20px;
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 16px;
  margin-bottom: 20px;
}

.summary-amount {
  font-size: 20px;
  font-weight: bold;
}

.next-btn {
  width: 100%;
  padding: 18px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 20px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.next-btn:hover:not(:disabled) {
  background-color: #2980b9;
  transform: translateY(-2px);
}

.next-btn:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.detail-card {
  background-color: #f8f9fa;
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 20px;
}

.detail-list {
  margin-bottom: 20px;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  border-bottom: 1px dashed #ddd;
}

.detail-item:last-child {
  border-bottom: none;
}

.detail-total {
  background-color: white;
  border-radius: 10px;
  padding: 15px;
}

.total-row {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  font-size: 16px;
}

.total-row.insurance {
  color: #4CAF50;
}

.total-row.self-payment {
  border-top: 2px solid #eee;
  margin-top: 10px;
  padding-top: 15px;
  font-size: 18px;
}

.total-row .highlight {
  color: #e74c3c;
  font-size: 24px;
  font-weight: bold;
}

.payment-methods {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.payment-method-card {
  background-color: #f8f9fa;
  border-radius: 15px;
  padding: 30px 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid transparent;
  min-width: 150px;
}

.payment-method-card:hover {
  transform: translateY(-3px);
  border-color: #3498db;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}

.method-icon {
  font-size: 60px;
}

.method-name {
  font-size: 18px;
  font-weight: 600;
}

.qrcode-container {
  text-align: center;
}

.qrcode-box {
  display: flex;
  justify-content: center;
  margin: 30px 0;
}

.fake-qrcode {
  width: 250px;
  height: 250px;
  background: linear-gradient(45deg, #fff 25%, transparent 25%),
    linear-gradient(-45deg, #fff 25%, transparent 25%),
    linear-gradient(45deg, transparent 75%, #fff 75%),
    linear-gradient(-45deg, transparent 75%, #fff 75%);
  background-size: 20px 20px;
  background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
  background-color: #000;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
}

.qrcode-pattern {
  width: 180px;
  height: 180px;
  background: repeating-conic-gradient(#000 0% 25%, #fff 0% 50%) 50% / 30px 30px;
}

.qrcode-text {
  position: absolute;
  bottom: 20px;
  color: #3498db;
  font-size: 14px;
  font-weight: bold;
  background: white;
  padding: 5px 15px;
  border-radius: 5px;
}

.amount-display {
  font-size: 20px;
  color: #666;
  margin-bottom: 10px;
}

.amount-display .amount {
  color: #e74c3c;
  font-size: 32px;
  font-weight: bold;
}

.payment-tip {
  color: #999;
  font-size: 14px;
  margin-bottom: 30px;
}

.simulate-btn {
  padding: 15px 40px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.simulate-btn:hover {
  background-color: #45a049;
  transform: translateY(-2px);
}

.success-message {
  text-align: center;
  padding: 40px 20px;
}

.success-icon {
  font-size: 80px;
  margin-bottom: 20px;
}

.success-message h2 {
  font-size: 32px;
  color: #4CAF50;
  margin-bottom: 20px;
}

.success-detail {
  background-color: #f8f9fa;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
}

.success-detail p {
  font-size: 18px;
  color: #666;
  margin: 10px 0;
}

.receipt-info {
  background-color: #e3f2fd;
  border-radius: 10px;
  padding: 15px;
  margin-bottom: 30px;
}

.receipt-info p {
  color: #1976d2;
  font-size: 16px;
}

.home-btn {
  padding: 15px 50px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.home-btn:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.4s ease;
}

.slide-enter-from {
  opacity: 0;
  transform: translateX(50px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateX(-50px);
}

.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  transform: translateX(0);
}

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.loading-spinner {
  width: 60px;
  height: 60px;
  border: 5px solid rgba(255, 255, 255, 0.3);
  border-top-color: #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.loading-text {
  margin-top: 20px;
  color: white;
  font-size: 18px;
  font-weight: 500;
}
</style>
