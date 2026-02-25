<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

const emit = defineEmits(['navigate'])

const currentStep = ref(1)
const countdown = ref(90)
let countdownTimer = null

const selectedMethod = ref(null)
const patientInfo = ref(null)
const selectedPaymentItem = ref(null)
const selectedPayMethod = ref(null)

const methods = [
  { id: 1, name: '医保卡', icon: '💳', desc: '请将医保卡插入读卡器' },
  { id: 2, name: '身份证', icon: '🪪', desc: '请将身份证放置在读卡区域' },
  { id: 3, name: '电子医保凭证', icon: '📱', desc: '请打开电子医保凭证扫码' }
]

const mockPatientInfo = {
  name: '张三',
  idCard: '330102199001011234',
  medicalCardNo: 'MED20240001'
}

const mockPaymentList = [
  {
    id: 1,
    department: '内科',
    doctor: '李医生',
    date: '2024-01-15',
    items: [
      { name: '挂号费', amount: 10 },
      { name: '诊查费', amount: 20 }
    ],
    totalAmount: 30,
    insuranceAmount: 20,
    selfPayAmount: 10,
    status: '待缴费'
  },
  {
    id: 2,
    department: '检验科',
    doctor: '王医生',
    date: '2024-01-15',
    items: [
      { name: '血常规', amount: 35 },
      { name: '肝功能检查', amount: 80 },
      { name: '肾功能检查', amount: 60 }
    ],
    totalAmount: 175,
    insuranceAmount: 100,
    selfPayAmount: 75,
    status: '待缴费'
  },
  {
    id: 3,
    department: '放射科',
    doctor: '赵医生',
    date: '2024-01-14',
    items: [
      { name: '胸部X光', amount: 80 },
      { name: 'CT检查', amount: 300 }
    ],
    totalAmount: 380,
    insuranceAmount: 200,
    selfPayAmount: 180,
    status: '待缴费'
  }
]

const paymentList = ref([])

const payMethods = [
  { id: 1, name: '微信支付', icon: '💚', color: '#07C160' },
  { id: 2, name: '支付宝', icon: '💙', color: '#1677FF' }
]

const qrCodeUrl = ref('')
const isPaymentSuccess = ref(false)
let paymentCheckTimer = null

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

function resetCountdown() {
  startCountdown()
}

function selectMethod(method) {
  selectedMethod.value = method
  setTimeout(() => {
    patientInfo.value = mockPatientInfo
    paymentList.value = mockPaymentList
    currentStep.value = 2
    resetCountdown()
  }, 1500)
}

function selectPaymentItem(item) {
  selectedPaymentItem.value = item
  currentStep.value = 3
  resetCountdown()
}

function selectPayMethod(method) {
  selectedPayMethod.value = method
  qrCodeUrl.value = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=pay_${Date.now()}_${method.id}`
  currentStep.value = 4
  resetCountdown()
  startPaymentCheck()
}

function startPaymentCheck() {
  isPaymentSuccess.value = false
  paymentCheckTimer = setTimeout(() => {
    isPaymentSuccess.value = true
    currentStep.value = 5
    resetCountdown()
  }, 5000)
}

function stopPaymentCheck() {
  if (paymentCheckTimer) {
    clearTimeout(paymentCheckTimer)
    paymentCheckTimer = null
  }
}

function goBack() {
  stopPaymentCheck()
  if (currentStep.value > 1) {
    currentStep.value--
    resetCountdown()
  } else {
    goHome()
  }
}

function goHome() {
  stopCountdown()
  stopPaymentCheck()
  emit('navigate', 'home')
}

watch(currentStep, () => {
  resetCountdown()
})

onMounted(() => {
  startCountdown()
})

onUnmounted(() => {
  stopCountdown()
  stopPaymentCheck()
})
</script>

<template>
  <div class="payment-container">
    <div class="payment-header">
      <button class="back-btn" @click="goBack">←</button>
      <div class="title">自助缴费</div>
      <div class="countdown">
        <span class="countdown-label">剩余时间</span>
        <span class="countdown-value">{{ countdown }}s</span>
      </div>
    </div>

    <div class="step-indicator">
      <div :class="['step', { active: currentStep >= 1 }]">1. 选择方式</div>
      <div :class="['step', { active: currentStep >= 2 }]">2. 缴费列表</div>
      <div :class="['step', { active: currentStep >= 3 }]">3. 缴费详情</div>
      <div :class="['step', { active: currentStep >= 4 }]">4. 支付方式</div>
      <div :class="['step', { active: currentStep >= 5 }]">5. 完成缴费</div>
    </div>

    <div class="payment-content">
      <div v-if="currentStep === 1" class="step-content">
        <h2>请选择操作方式</h2>
        <div class="method-list">
          <div
            v-for="method in methods"
            :key="method.id"
            :class="['method-item', { selected: selectedMethod?.id === method.id }]"
            @click="selectMethod(method)"
          >
            <div class="method-icon">{{ method.icon }}</div>
            <div class="method-name">{{ method.name }}</div>
            <div class="method-desc">{{ method.desc }}</div>
          </div>
        </div>
      </div>

      <div v-if="currentStep === 2" class="step-content">
        <div class="patient-info-card">
          <div class="patient-name">患者：{{ patientInfo?.name }}</div>
          <div class="patient-detail">身份证号：{{ patientInfo?.idCard }}</div>
          <div class="patient-detail">医保卡号：{{ patientInfo?.medicalCardNo }}</div>
        </div>
        <h2>待缴费项目</h2>
        <div class="payment-list">
          <div
            v-for="item in paymentList"
            :key="item.id"
            class="payment-item"
            @click="selectPaymentItem(item)"
          >
            <div class="payment-item-header">
              <span class="department">{{ item.department }}</span>
              <span class="status">{{ item.status }}</span>
            </div>
            <div class="payment-item-body">
              <div class="info-row">
                <span class="label">医生：</span>
                <span class="value">{{ item.doctor }}</span>
              </div>
              <div class="info-row">
                <span class="label">日期：</span>
                <span class="value">{{ item.date }}</span>
              </div>
              <div class="info-row">
                <span class="label">项目：</span>
                <span class="value">{{ item.items.map(i => i.name).join('、') }}</span>
              </div>
            </div>
            <div class="payment-item-footer">
              <div class="amount-info">
                <span class="total">合计：¥{{ item.totalAmount.toFixed(2) }}</span>
                <span class="self-pay">自费：¥{{ item.selfPayAmount.toFixed(2) }}</span>
              </div>
            </div>
          </div>
        </div>
        <div v-if="paymentList.length === 0" class="empty-list">
          <div class="empty-icon">📭</div>
          <p>暂无待缴费项目</p>
        </div>
      </div>

      <div v-if="currentStep === 3" class="step-content">
        <h2>缴费详情</h2>
        <div class="detail-card">
          <div class="detail-header">
            <span class="department">{{ selectedPaymentItem?.department }}</span>
            <span class="doctor">{{ selectedPaymentItem?.doctor }}</span>
          </div>
          <div class="detail-body">
            <div class="detail-section">
              <div class="section-title">诊疗项目</div>
              <div class="item-list">
                <div v-for="(item, index) in selectedPaymentItem?.items" :key="index" class="item-row">
                  <span class="item-name">{{ item.name }}</span>
                  <span class="item-amount">¥{{ item.amount.toFixed(2) }}</span>
                </div>
              </div>
            </div>
            <div class="detail-section">
              <div class="amount-row">
                <span class="amount-label">费用总额</span>
                <span class="amount-value">¥{{ selectedPaymentItem?.totalAmount.toFixed(2) }}</span>
              </div>
              <div class="amount-row insurance">
                <span class="amount-label">医保报销</span>
                <span class="amount-value">-¥{{ selectedPaymentItem?.insuranceAmount.toFixed(2) }}</span>
              </div>
              <div class="amount-row self-pay">
                <span class="amount-label">自费金额</span>
                <span class="amount-value">¥{{ selectedPaymentItem?.selfPayAmount.toFixed(2) }}</span>
              </div>
            </div>
          </div>
          <div class="detail-footer">
            <button class="pay-btn" @click="currentStep = 4; resetCountdown()">
              立即缴费 ¥{{ selectedPaymentItem?.selfPayAmount.toFixed(2) }}
            </button>
          </div>
        </div>
      </div>

      <div v-if="currentStep === 4" class="step-content">
        <h2>选择支付方式</h2>
        <div class="pay-method-list">
          <div
            v-for="method in payMethods"
            :key="method.id"
            :class="['pay-method-item', { selected: selectedPayMethod?.id === method.id }]"
            :style="{ borderColor: selectedPayMethod?.id === method.id ? method.color : '' }"
            @click="selectPayMethod(method)"
          >
            <div class="pay-method-icon">{{ method.icon }}</div>
            <div class="pay-method-name">{{ method.name }}</div>
          </div>
        </div>
        <div v-if="selectedPayMethod" class="qrcode-section">
          <div class="qrcode-title">请使用{{ selectedPayMethod.name }}扫码支付</div>
          <div class="qrcode-container">
            <img :src="qrCodeUrl" alt="支付二维码" class="qrcode-img" />
          </div>
          <div class="qrcode-amount">
            支付金额：<span class="amount">¥{{ selectedPaymentItem?.selfPayAmount.toFixed(2) }}</span>
          </div>
          <div class="payment-waiting">
            <div class="loading-spinner"></div>
            <span>等待支付中...</span>
          </div>
        </div>
      </div>

      <div v-if="currentStep === 5" class="step-content">
        <div class="success-container">
          <div class="success-icon">✅</div>
          <h2>缴费成功</h2>
          <div class="success-info">
            <div class="info-row">
              <span class="label">缴费金额：</span>
              <span class="value">¥{{ selectedPaymentItem?.selfPayAmount.toFixed(2) }}</span>
            </div>
            <div class="info-row">
              <span class="label">支付方式：</span>
              <span class="value">{{ selectedPayMethod?.name }}</span>
            </div>
            <div class="info-row">
              <span class="label">交易时间：</span>
              <span class="value">{{ new Date().toLocaleString() }}</span>
            </div>
          </div>
          <div class="success-tips">
            <p>请妥善保管您的缴费凭证</p>
            <p>如有疑问请咨询导诊台</p>
          </div>
          <button class="home-btn" @click="goHome">返回首页</button>
        </div>
      </div>
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
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 8px 16px;
  border-radius: 20px;
}

.countdown-label {
  font-size: 14px;
}

.countdown-value {
  font-size: 18px;
  font-weight: bold;
  color: #e74c3c;
}

.step-indicator {
  height: 60px;
  background-color: #ecf0f1;
  display: flex;
  align-items: center;
  padding: 0 20px;
  gap: 10px;
  overflow-x: auto;
}

.step {
  flex: 1;
  text-align: center;
  padding: 10px;
  border-radius: 5px;
  background-color: #bdc3c7;
  color: white;
  font-size: 14px;
  white-space: nowrap;
  min-width: 100px;
}

.step.active {
  background-color: #27ae60;
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

.method-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.method-item {
  background-color: #ecf0f1;
  border-radius: 15px;
  padding: 30px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border: 3px solid transparent;
}

.method-item:hover {
  transform: translateY(-5px);
  background-color: #3498db;
  color: white;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

.method-item.selected {
  border-color: #27ae60;
  background-color: #27ae60;
  color: white;
}

.method-icon {
  font-size: 48px;
  margin-bottom: 15px;
}

.method-name {
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 8px;
}

.method-desc {
  font-size: 14px;
  color: #7f8c8d;
}

.method-item:hover .method-desc,
.method-item.selected .method-desc {
  color: rgba(255, 255, 255, 0.8);
}

.patient-info-card {
  background-color: #e8f5e9;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
  border-left: 4px solid #27ae60;
}

.patient-name {
  font-size: 20px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 10px;
}

.patient-detail {
  font-size: 14px;
  color: #7f8c8d;
  margin: 5px 0;
}

.payment-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.payment-item {
  background-color: #ecf0f1;
  border-radius: 12px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.payment-item:hover {
  transform: translateY(-3px);
  background-color: #3498db;
  color: white;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.payment-item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 1px solid #bdc3c7;
}

.payment-item:hover .payment-item-header {
  border-bottom-color: rgba(255, 255, 255, 0.3);
}

.department {
  font-size: 18px;
  font-weight: 600;
}

.status {
  background-color: #e74c3c;
  color: white;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
}

.payment-item-body .info-row {
  display: flex;
  margin: 8px 0;
  font-size: 14px;
}

.payment-item-body .label {
  color: #7f8c8d;
  width: 60px;
}

.payment-item:hover .payment-item-body .label {
  color: rgba(255, 255, 255, 0.7);
}

.payment-item-footer {
  margin-top: 15px;
  padding-top: 10px;
  border-top: 1px solid #bdc3c7;
}

.payment-item:hover .payment-item-footer {
  border-top-color: rgba(255, 255, 255, 0.3);
}

.amount-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.total {
  font-size: 16px;
  font-weight: 600;
}

.self-pay {
  font-size: 18px;
  font-weight: bold;
  color: #e74c3c;
}

.payment-item:hover .self-pay {
  color: #ffeb3b;
}

.empty-list {
  text-align: center;
  padding: 60px 20px;
}

.empty-icon {
  font-size: 60px;
  margin-bottom: 20px;
}

.empty-list p {
  font-size: 18px;
  color: #7f8c8d;
}

.detail-card {
  background-color: #ecf0f1;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.detail-header {
  background-color: #3498db;
  color: white;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.detail-header .department {
  font-size: 20px;
  font-weight: 600;
}

.detail-header .doctor {
  font-size: 16px;
}

.detail-body {
  padding: 20px;
}

.detail-section {
  margin-bottom: 20px;
}

.section-title {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 2px solid #3498db;
}

.item-list {
  background-color: white;
  border-radius: 10px;
  padding: 15px;
}

.item-row {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px dashed #ecf0f1;
}

.item-row:last-child {
  border-bottom: none;
}

.item-name {
  color: #2c3e50;
}

.item-amount {
  font-weight: 600;
  color: #2c3e50;
}

.amount-row {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  border-bottom: 1px solid #ecf0f1;
}

.amount-row:last-child {
  border-bottom: none;
}

.amount-label {
  color: #7f8c8d;
}

.amount-value {
  font-weight: 600;
}

.amount-row.insurance .amount-value {
  color: #27ae60;
}

.amount-row.self-pay {
  background-color: #fff3e0;
  margin: 10px -20px -20px -20px;
  padding: 15px 20px;
}

.amount-row.self-pay .amount-label {
  color: #e74c3c;
  font-weight: 600;
}

.amount-row.self-pay .amount-value {
  color: #e74c3c;
  font-size: 20px;
}

.detail-footer {
  padding: 20px;
  background-color: white;
}

.pay-btn {
  width: 100%;
  padding: 18px;
  background-color: #27ae60;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 20px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.pay-btn:hover {
  background-color: #219a52;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(39, 174, 96, 0.3);
}

.pay-method-list {
  display: flex;
  gap: 20px;
  margin-bottom: 30px;
}

.pay-method-item {
  flex: 1;
  background-color: #ecf0f1;
  border-radius: 15px;
  padding: 30px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 3px solid transparent;
}

.pay-method-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.pay-method-item.selected {
  background-color: #f0f9ff;
}

.pay-method-icon {
  font-size: 40px;
  margin-bottom: 10px;
}

.pay-method-name {
  font-size: 18px;
  font-weight: 600;
}

.qrcode-section {
  text-align: center;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 15px;
}

.qrcode-title {
  font-size: 18px;
  color: #2c3e50;
  margin-bottom: 20px;
}

.qrcode-container {
  display: inline-block;
  padding: 15px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.qrcode-img {
  width: 200px;
  height: 200px;
}

.qrcode-amount {
  margin-top: 20px;
  font-size: 18px;
  color: #2c3e50;
}

.qrcode-amount .amount {
  font-size: 24px;
  font-weight: bold;
  color: #e74c3c;
}

.payment-waiting {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
  color: #7f8c8d;
}

.loading-spinner {
  width: 20px;
  height: 20px;
  border: 3px solid #ecf0f1;
  border-top-color: #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.success-container {
  text-align: center;
  padding: 40px 20px;
}

.success-icon {
  font-size: 80px;
  margin-bottom: 20px;
}

.success-container h2 {
  font-size: 32px;
  color: #27ae60;
  margin-bottom: 30px;
}

.success-info {
  background-color: #ecf0f1;
  border-radius: 15px;
  padding: 25px;
  margin-bottom: 30px;
  text-align: left;
}

.success-info .info-row {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px dashed #bdc3c7;
}

.success-info .info-row:last-child {
  border-bottom: none;
}

.success-info .label {
  color: #7f8c8d;
}

.success-info .value {
  font-weight: 600;
  color: #2c3e50;
}

.success-tips {
  margin-bottom: 30px;
}

.success-tips p {
  color: #7f8c8d;
  margin: 8px 0;
}

.home-btn {
  padding: 15px 60px;
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
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}
</style>
