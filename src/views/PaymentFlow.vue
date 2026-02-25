<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const emit = defineEmits(['navigate'])

// 当前步骤
const currentStep = ref(1)

// 选择的操作方式
const selectedMethod = ref(null)

// 选择的缴费项目
const selectedItems = ref([])

// 选择的支付方式
const selectedPaymentMethod = ref(null)

// 患者信息
const patientInfo = ref({
  name: '张三',
  cardNo: '11010119900101****',
  gender: '男',
  age: 34
})

// 倒计时
const countdown = ref(90)
let countdownTimer = null

// 操作方式选项
const identityMethods = [
  { id: 'medical-card', name: '医保卡', icon: '💳', desc: '请插入医保卡' },
  { id: 'id-card', name: '身份证', icon: '🆔', desc: '请刷身份证' },
  { id: 'e-medical', name: '电子医保凭证', icon: '📱', desc: '请出示电子医保凭证' }
]

// 模拟缴费项目数据
const paymentItems = ref([
  {
    id: 1,
    type: '挂号费',
    department: '内科',
    doctor: '张医生',
    date: '2024-01-15',
    amount: 15.00,
    insurance: 10.00,
    selfPay: 5.00,
    status: '待缴费'
  },
  {
    id: 2,
    type: '检查费',
    department: '检验科',
    itemName: '血常规检查',
    date: '2024-01-15',
    amount: 85.00,
    insurance: 60.00,
    selfPay: 25.00,
    status: '待缴费'
  },
  {
    id: 3,
    type: '药品费',
    department: '药房',
    itemName: '阿莫西林胶囊 x2盒',
    date: '2024-01-15',
    amount: 45.50,
    insurance: 30.00,
    selfPay: 15.50,
    status: '待缴费'
  },
  {
    id: 4,
    type: '治疗费',
    department: '理疗科',
    itemName: '针灸治疗',
    date: '2024-01-14',
    amount: 120.00,
    insurance: 80.00,
    selfPay: 40.00,
    status: '待缴费'
  }
])

// 支付方式
const paymentMethods = [
  { id: 'wechat', name: '微信支付', icon: '💚', color: '#07c160' },
  { id: 'alipay', name: '支付宝', icon: '💙', color: '#1677ff' }
]

// 计算选中项目的总金额
const totalAmount = ref(0)
const totalInsurance = ref(0)
const totalSelfPay = ref(0)

function updateTotal() {
  totalAmount.value = selectedItems.value.reduce((sum, item) => sum + item.amount, 0)
  totalInsurance.value = selectedItems.value.reduce((sum, item) => sum + item.insurance, 0)
  totalSelfPay.value = selectedItems.value.reduce((sum, item) => sum + item.selfPay, 0)
}

// 选择身份验证方式
function selectIdentityMethod(method) {
  selectedMethod.value = method
  // 模拟读取卡片信息
  setTimeout(() => {
    currentStep.value = 2
    resetCountdown()
  }, 1500)
}

// 选择缴费项目
function toggleItem(item) {
  const index = selectedItems.value.findIndex(i => i.id === item.id)
  if (index > -1) {
    selectedItems.value.splice(index, 1)
  } else {
    selectedItems.value.push(item)
  }
  updateTotal()
}

function isSelected(item) {
  return selectedItems.value.some(i => i.id === item.id)
}

// 确认选择并进入详情
function confirmSelection() {
  if (selectedItems.value.length === 0) {
    alert('请至少选择一个缴费项目')
    return
  }
  currentStep.value = 3
  resetCountdown()
}

// 选择支付方式
function selectPaymentMethod(method) {
  selectedPaymentMethod.value = method
  currentStep.value = 4
  resetCountdown()
}

// 支付交易信息
const transactionInfo = ref({
  orderNo: '',
  payTime: '',
  payMethod: ''
})

// 生成交易单号
function generateOrderNo() {
  const date = new Date()
  const dateStr = date.getFullYear().toString() +
    String(date.getMonth() + 1).padStart(2, '0') +
    String(date.getDate()).padStart(2, '0')
  const randomStr = Math.floor(Math.random() * 1000000).toString().padStart(6, '0')
  return `PY${dateStr}${randomStr}`
}

// 格式化时间
function formatDateTime(date) {
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')
  const hours = String(date.getHours()).padStart(2, '0')
  const minutes = String(date.getMinutes()).padStart(2, '0')
  const seconds = String(date.getSeconds()).padStart(2, '0')
  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
}

// 模拟支付成功
function completePayment() {
  // 生成交易信息
  transactionInfo.value = {
    orderNo: generateOrderNo(),
    payTime: formatDateTime(new Date()),
    payMethod: selectedPaymentMethod.value?.name || ''
  }
  // 模拟支付处理
  setTimeout(() => {
    currentStep.value = 6
    resetCountdown()
  }, 1000)
}

// 打印凭证
function printVoucher() {
  alert('正在打印缴费凭证...\n请从下方取票口取走您的凭证')
}

// 查看缴费明细
function showDetails() {
  alert('缴费明细功能：\n' + selectedItems.value.map(item => 
    `${item.type}: ¥${item.amount.toFixed(2)}`
  ).join('\n'))
}

// 返回首页
function goHome() {
  clearInterval(countdownTimer)
  emit('navigate', 'home')
}

// 返回上一步
function goBack() {
  if (currentStep.value > 1) {
    currentStep.value--
    resetCountdown()
  } else {
    goHome()
  }
}

// 倒计时功能
function startCountdown() {
  clearInterval(countdownTimer)
  countdownTimer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(countdownTimer)
      goHome()
    }
  }, 1000)
}

function resetCountdown() {
  countdown.value = 90
  startCountdown()
}

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60)
  const secs = seconds % 60
  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
}

onMounted(() => {
  startCountdown()
})

onUnmounted(() => {
  clearInterval(countdownTimer)
})
</script>

<template>
  <div class="payment-flow-container">
    <!-- 顶部导航 -->
    <div class="payment-header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <div class="title">自助缴费</div>
      <div class="countdown">
        <span class="countdown-label">剩余时间</span>
        <span class="countdown-time" :class="{ warning: countdown <= 30 }">{{ formatTime(countdown) }}</span>
      </div>
    </div>

    <!-- 步骤指示器 -->
    <div class="step-indicator">
      <div :class="['step', { active: currentStep >= 1, completed: currentStep > 1 }]">
        <div class="step-number">1</div>
        <div class="step-name">身份验证</div>
      </div>
      <div class="step-line" :class="{ active: currentStep >= 2 }"></div>
      <div :class="['step', { active: currentStep >= 2, completed: currentStep > 2 }]">
        <div class="step-number">2</div>
        <div class="step-name">选择项目</div>
      </div>
      <div class="step-line" :class="{ active: currentStep >= 3 }"></div>
      <div :class="['step', { active: currentStep >= 3, completed: currentStep > 3 }]">
        <div class="step-number">3</div>
        <div class="step-name">确认详情</div>
      </div>
      <div class="step-line" :class="{ active: currentStep >= 4 }"></div>
      <div :class="['step', { active: currentStep >= 4, completed: currentStep > 4 }]">
        <div class="step-number">4</div>
        <div class="step-name">扫码支付</div>
      </div>
      <div class="step-line" :class="{ active: currentStep >= 5 }"></div>
      <div :class="['step', { active: currentStep >= 5 }]">
        <div class="step-number">5</div>
        <div class="step-name">缴费完成</div>
      </div>
    </div>

    <!-- 内容区域 -->
    <div class="payment-content">
      <!-- 步骤1: 选择操作方式 -->
      <div v-if="currentStep === 1" class="step-content">
        <h2 class="step-title">请选择身份验证方式</h2>
        <div class="identity-methods">
          <div
            v-for="method in identityMethods"
            :key="method.id"
            class="method-card"
            @click="selectIdentityMethod(method)"
          >
            <div class="method-icon">{{ method.icon }}</div>
            <div class="method-name">{{ method.name }}</div>
            <div class="method-desc">{{ method.desc }}</div>
          </div>
        </div>
        <div v-if="selectedMethod" class="reading-status">
          <div class="loading-spinner"></div>
          <p>正在读取{{ selectedMethod.name }}信息...</p>
        </div>
      </div>

      <!-- 步骤2: 缴费项目列表 -->
      <div v-if="currentStep === 2" class="step-content">
        <div class="patient-info-bar">
          <span>患者：{{ patientInfo.name }}</span>
          <span>卡号：{{ patientInfo.cardNo }}</span>
          <span>{{ patientInfo.gender }} {{ patientInfo.age }}岁</span>
        </div>
        <h2 class="step-title">请选择需要缴费的项目</h2>
        <div class="payment-list">
          <div
            v-for="item in paymentItems"
            :key="item.id"
            :class="['payment-item', { selected: isSelected(item) }]"
            @click="toggleItem(item)"
          >
            <div class="item-checkbox">
              <span v-if="isSelected(item)" class="check-icon">✓</span>
            </div>
            <div class="item-info">
              <div class="item-header">
                <span class="item-type">{{ item.type }}</span>
                <span class="item-status">{{ item.status }}</span>
              </div>
              <div class="item-detail">
                <span v-if="item.department">{{ item.department }}</span>
                <span v-if="item.doctor">{{ item.doctor }}</span>
                <span v-if="item.itemName">{{ item.itemName }}</span>
              </div>
              <div class="item-date">{{ item.date }}</div>
            </div>
            <div class="item-amounts">
              <div class="total-amount">¥{{ item.amount.toFixed(2) }}</div>
              <div class="insurance-amount">医保: ¥{{ item.insurance.toFixed(2) }}</div>
              <div class="selfpay-amount">自费: ¥{{ item.selfPay.toFixed(2) }}</div>
            </div>
          </div>
        </div>
        <div class="selection-summary" v-if="selectedItems.length > 0">
          <div class="summary-row">
            <span>已选 {{ selectedItems.length }} 项</span>
            <span class="summary-amount">自费合计: ¥{{ totalSelfPay.toFixed(2) }}</span>
          </div>
        </div>
        <button class="confirm-btn" :disabled="selectedItems.length === 0" @click="confirmSelection">
          确认选择
        </button>
      </div>

      <!-- 步骤3: 缴费详情 -->
      <div v-if="currentStep === 3" class="step-content">
        <div class="patient-info-bar">
          <span>患者：{{ patientInfo.name }}</span>
          <span>卡号：{{ patientInfo.cardNo }}</span>
        </div>
        <h2 class="step-title">缴费详情确认</h2>
        <div class="detail-list">
          <div v-for="item in selectedItems" :key="item.id" class="detail-item">
            <div class="detail-left">
              <div class="detail-type">{{ item.type }}</div>
              <div class="detail-info">{{ item.department }} {{ item.doctor || item.itemName }}</div>
            </div>
            <div class="detail-right">
              <div class="detail-total">¥{{ item.amount.toFixed(2) }}</div>
              <div class="detail-breakdown">
                <span>医保¥{{ item.insurance.toFixed(2) }}</span>
                <span>自费¥{{ item.selfPay.toFixed(2) }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="detail-summary">
          <div class="summary-line">
            <span>费用总额</span>
            <span>¥{{ totalAmount.toFixed(2) }}</span>
          </div>
          <div class="summary-line">
            <span>医保支付</span>
            <span class="insurance">-¥{{ totalInsurance.toFixed(2) }}</span>
          </div>
          <div class="summary-line total">
            <span>自费金额</span>
            <span class="selfpay">¥{{ totalSelfPay.toFixed(2) }}</span>
          </div>
        </div>
        <button class="confirm-btn" @click="currentStep = 4">
          去支付
        </button>
      </div>

      <!-- 步骤4: 选择支付方式 -->
      <div v-if="currentStep === 4" class="step-content">
        <h2 class="step-title">请选择自费部分支付方式</h2>
        <div class="payment-amount-display">
          <div class="amount-label">需支付金额</div>
          <div class="amount-value">¥{{ totalSelfPay.toFixed(2) }}</div>
        </div>
        <div class="payment-methods">
          <div
            v-for="method in paymentMethods"
            :key="method.id"
            class="payment-method-card"
            @click="selectPaymentMethod(method)"
          >
            <div class="payment-method-icon" :style="{ backgroundColor: method.color }">
              {{ method.icon }}
            </div>
            <div class="payment-method-name">{{ method.name }}</div>
          </div>
        </div>
      </div>

      <!-- 步骤5: 扫码支付 -->
      <div v-if="currentStep === 5" class="step-content">
        <div class="qr-payment">
          <h2 class="step-title">请使用{{ selectedPaymentMethod?.name }}扫码</h2>
          <div class="payment-amount-display">
            <div class="amount-label">支付金额</div>
            <div class="amount-value">¥{{ totalSelfPay.toFixed(2) }}</div>
          </div>
          <div class="qr-code">
            <div class="qr-placeholder">
              <div class="qr-pattern"></div>
              <p>模拟二维码</p>
            </div>
          </div>
          <p class="qr-hint">请打开{{ selectedPaymentMethod?.name }}扫描二维码完成支付</p>
          <button class="confirm-btn" @click="completePayment">
            模拟支付成功
          </button>
        </div>
      </div>

      <!-- 步骤6: 缴费完成 -->
      <div v-if="currentStep === 6" class="step-content">
        <div class="success-page">
          <!-- 成功动画区域 -->
          <div class="success-animation">
            <div class="success-circle">
              <div class="success-check">✓</div>
            </div>
          </div>
          <h2 class="success-title">缴费成功！</h2>
          <p class="success-subtitle">您的缴费已完成，请妥善保管凭证</p>

          <!-- 交易信息卡片 -->
          <div class="transaction-card">
            <div class="card-header">
              <span class="card-title">交易凭证</span>
              <span class="card-status">支付成功</span>
            </div>
            <div class="card-body">
              <div class="info-row">
                <span class="info-label">交易单号</span>
                <span class="info-value order-no">{{ transactionInfo.orderNo }}</span>
              </div>
              <div class="info-row">
                <span class="info-label">支付时间</span>
                <span class="info-value">{{ transactionInfo.payTime }}</span>
              </div>
              <div class="info-row">
                <span class="info-label">支付方式</span>
                <span class="info-value">{{ transactionInfo.payMethod }}</span>
              </div>
              <div class="info-row">
                <span class="info-label">患者姓名</span>
                <span class="info-value">{{ patientInfo.name }}</span>
              </div>
              <div class="info-row">
                <span class="info-label">就诊卡号</span>
                <span class="info-value">{{ patientInfo.cardNo }}</span>
              </div>
            </div>
          </div>

          <!-- 费用明细卡片 -->
          <div class="fee-summary-card">
            <div class="fee-header">费用明细</div>
            <div class="fee-body">
              <div class="fee-row">
                <span class="fee-name">缴费项目</span>
                <span class="fee-value">{{ selectedItems.length }} 项</span>
              </div>
              <div class="fee-items-preview">
                <div v-for="item in selectedItems.slice(0, 3)" :key="item.id" class="preview-item">
                  <span>{{ item.type }}</span>
                  <span>¥{{ item.amount.toFixed(2) }}</span>
                </div>
                <div v-if="selectedItems.length > 3" class="preview-more">
                  还有 {{ selectedItems.length - 3 }} 项...
                </div>
              </div>
              <div class="fee-divider"></div>
              <div class="fee-row">
                <span class="fee-name">费用总额</span>
                <span class="fee-value">¥{{ totalAmount.toFixed(2) }}</span>
              </div>
              <div class="fee-row highlight">
                <span class="fee-name">医保支付</span>
                <span class="fee-value insurance">-¥{{ totalInsurance.toFixed(2) }}</span>
              </div>
              <div class="fee-row total">
                <span class="fee-name">自费金额</span>
                <span class="fee-value selfpay">¥{{ totalSelfPay.toFixed(2) }}</span>
              </div>
            </div>
          </div>

          <!-- 提示信息 -->
          <div class="notice-section">
            <div class="notice-title">📋 温馨提示</div>
            <div class="notice-list">
              <div class="notice-item">
                <span class="notice-dot">1</span>
                <span>请凭缴费凭证到相应科室就诊或取药</span>
              </div>
              <div class="notice-item">
                <span class="notice-dot">2</span>
                <span>如需发票请前往收费窗口打印</span>
              </div>
              <div class="notice-item">
                <span class="notice-dot">3</span>
                <span>请妥善保管您的交易凭证</span>
              </div>
            </div>
          </div>

          <!-- 操作按钮组 -->
          <div class="action-buttons">
            <button class="action-btn secondary" @click="printVoucher">
              <span class="btn-icon">🖨️</span>
              <span>打印凭证</span>
            </button>
            <button class="action-btn secondary" @click="showDetails">
              <span class="btn-icon">📋</span>
              <span>查看明细</span>
            </button>
            <button class="action-btn primary" @click="goHome">
              <span class="btn-icon">✓</span>
              <span>完成并返回首页</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.payment-flow-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

.payment-header {
  height: 80px;
  background-color: #2c3e50;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 30px;
}

.back-btn {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
}

.back-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.title {
  font-size: 24px;
  font-weight: bold;
}

.countdown {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.countdown-label {
  font-size: 12px;
  opacity: 0.8;
}

.countdown-time {
  font-size: 20px;
  font-weight: bold;
  font-family: monospace;
}

.countdown-time.warning {
  color: #e74c3c;
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0.5; }
}

/* 步骤指示器 */
.step-indicator {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 30px;
  background-color: white;
  border-bottom: 1px solid #e0e0e0;
}

.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  opacity: 0.5;
}

.step.active {
  opacity: 1;
}

.step.completed .step-number {
  background-color: #27ae60;
}

.step-number {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #3498db;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  margin-bottom: 8px;
}

.step-name {
  font-size: 14px;
  color: #333;
}

.step-line {
  width: 60px;
  height: 2px;
  background-color: #e0e0e0;
  margin: 0 10px;
  margin-bottom: 25px;
}

.step-line.active {
  background-color: #3498db;
}

/* 内容区域 */
.payment-content {
  flex: 1;
  padding: 30px;
  overflow-y: auto;
}

.step-content {
  max-width: 800px;
  margin: 0 auto;
}

.step-title {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
  font-size: 22px;
}

/* 身份验证方式 */
.identity-methods {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  margin-bottom: 30px;
}

.method-card {
  background-color: white;
  border-radius: 15px;
  padding: 40px 20px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border: 2px solid transparent;
}

.method-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
  border-color: #3498db;
}

.method-icon {
  font-size: 48px;
  margin-bottom: 15px;
}

.method-name {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
}

.method-desc {
  font-size: 14px;
  color: #666;
}

.reading-status {
  text-align: center;
  padding: 30px;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #e0e0e0;
  border-top-color: #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 15px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* 患者信息栏 */
.patient-info-bar {
  background-color: #e8f4f8;
  padding: 15px 20px;
  border-radius: 10px;
  margin-bottom: 20px;
  display: flex;
  gap: 30px;
  justify-content: center;
  font-size: 14px;
  color: #2c3e50;
}

/* 缴费列表 */
.payment-list {
  background-color: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.payment-item {
  display: flex;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid #f0f0f0;
  cursor: pointer;
  transition: background-color 0.2s;
}

.payment-item:last-child {
  border-bottom: none;
}

.payment-item:hover {
  background-color: #f8f9fa;
}

.payment-item.selected {
  background-color: #e8f5e9;
}

.item-checkbox {
  width: 24px;
  height: 24px;
  border: 2px solid #ccc;
  border-radius: 4px;
  margin-right: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}

.payment-item.selected .item-checkbox {
  background-color: #27ae60;
  border-color: #27ae60;
}

.check-icon {
  color: white;
  font-weight: bold;
}

.item-info {
  flex: 1;
}

.item-header {
  display: flex;
  gap: 10px;
  margin-bottom: 8px;
}

.item-type {
  font-weight: bold;
  color: #333;
  font-size: 16px;
}

.item-status {
  background-color: #e74c3c;
  color: white;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.item-detail {
  color: #666;
  font-size: 14px;
  margin-bottom: 5px;
}

.item-detail span {
  margin-right: 10px;
}

.item-date {
  color: #999;
  font-size: 13px;
}

.item-amounts {
  text-align: right;
}

.total-amount {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.insurance-amount {
  font-size: 13px;
  color: #27ae60;
}

.selfpay-amount {
  font-size: 13px;
  color: #e74c3c;
}

.selection-summary {
  background-color: white;
  padding: 15px 20px;
  border-radius: 10px;
  margin-bottom: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.summary-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 16px;
}

.summary-amount {
  font-size: 20px;
  font-weight: bold;
  color: #e74c3c;
}

/* 详情页 */
.detail-list {
  background-color: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  border-bottom: 1px solid #f0f0f0;
}

.detail-item:last-child {
  border-bottom: none;
}

.detail-type {
  font-weight: bold;
  color: #333;
  margin-bottom: 5px;
}

.detail-info {
  color: #666;
  font-size: 14px;
}

.detail-total {
  font-size: 16px;
  font-weight: bold;
  color: #333;
  text-align: right;
}

.detail-breakdown {
  font-size: 12px;
  color: #666;
  text-align: right;
  margin-top: 5px;
}

.detail-breakdown span {
  margin-left: 10px;
}

.detail-summary {
  background-color: white;
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.summary-line {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px dashed #e0e0e0;
  font-size: 16px;
}

.summary-line:last-child {
  border-bottom: none;
}

.summary-line.total {
  font-size: 20px;
  font-weight: bold;
  padding-top: 15px;
  margin-top: 10px;
  border-top: 2px solid #333;
}

.summary-line .insurance {
  color: #27ae60;
}

.summary-line .selfpay {
  color: #e74c3c;
  font-size: 24px;
}

/* 支付方式选择 */
.payment-amount-display {
  text-align: center;
  margin-bottom: 30px;
}

.amount-label {
  font-size: 16px;
  color: #666;
  margin-bottom: 10px;
}

.amount-value {
  font-size: 48px;
  font-weight: bold;
  color: #e74c3c;
}

.payment-methods {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  max-width: 400px;
  margin: 0 auto;
}

.payment-method-card {
  background-color: white;
  border-radius: 15px;
  padding: 40px 20px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border: 2px solid transparent;
}

.payment-method-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
  border-color: #3498db;
}

.payment-method-icon {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 40px;
  margin: 0 auto 15px;
  color: white;
}

.payment-method-name {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

/* 扫码支付 */
.qr-payment {
  text-align: center;
}

.qr-code {
  margin: 30px 0;
}

.qr-placeholder {
  width: 250px;
  height: 250px;
  background-color: white;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.qr-pattern {
  width: 180px;
  height: 180px;
  background-image: 
    repeating-linear-gradient(0deg, #333 0px, #333 10px, transparent 10px, transparent 20px),
    repeating-linear-gradient(90deg, #333 0px, #333 10px, transparent 10px, transparent 20px);
  background-size: 20px 20px;
  opacity: 0.3;
}

.qr-hint {
  color: #666;
  margin-bottom: 20px;
}

/* 成功页面 */
.success-page {
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
  padding-bottom: 30px;
}

/* 成功动画 */
.success-animation {
  margin-bottom: 20px;
}

.success-circle {
  width: 100px;
  height: 100px;
  background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  box-shadow: 0 4px 20px rgba(39, 174, 96, 0.4);
  animation: scaleIn 0.5s ease-out;
}

@keyframes scaleIn {
  0% {
    transform: scale(0);
    opacity: 0;
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.success-check {
  font-size: 50px;
  color: white;
  font-weight: bold;
}

.success-title {
  color: #27ae60;
  font-size: 28px;
  margin-bottom: 10px;
}

.success-subtitle {
  color: #666;
  font-size: 16px;
  margin-bottom: 30px;
}

/* 交易信息卡片 */
.transaction-card {
  background-color: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  text-align: left;
}

.card-header {
  background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
  color: white;
  padding: 15px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-title {
  font-size: 18px;
  font-weight: bold;
}

.card-status {
  background-color: rgba(255, 255, 255, 0.2);
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 14px;
}

.card-body {
  padding: 20px;
}

.info-row {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  border-bottom: 1px dashed #e0e0e0;
}

.info-row:last-child {
  border-bottom: none;
}

.info-label {
  color: #666;
  font-size: 15px;
}

.info-value {
  color: #333;
  font-size: 15px;
  font-weight: 500;
}

.info-value.order-no {
  font-family: monospace;
  background-color: #f0f0f0;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 14px;
}

/* 费用明细卡片 */
.fee-summary-card {
  background-color: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  text-align: left;
}

.fee-header {
  background-color: #f8f9fa;
  padding: 15px 20px;
  font-size: 16px;
  font-weight: bold;
  color: #333;
  border-bottom: 1px solid #e0e0e0;
}

.fee-body {
  padding: 20px;
}

.fee-row {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  font-size: 15px;
}

.fee-row.highlight {
  color: #27ae60;
}

.fee-row.total {
  font-size: 18px;
  font-weight: bold;
  padding-top: 15px;
  margin-top: 10px;
  border-top: 2px solid #333;
}

.fee-name {
  color: #666;
}

.fee-value {
  color: #333;
  font-weight: 500;
}

.fee-value.insurance {
  color: #27ae60;
}

.fee-value.selfpay {
  color: #e74c3c;
  font-size: 20px;
}

.fee-items-preview {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 12px 15px;
  margin: 10px 0;
}

.preview-item {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  font-size: 14px;
  color: #666;
}

.preview-more {
  text-align: center;
  color: #999;
  font-size: 13px;
  padding-top: 8px;
  border-top: 1px dashed #ddd;
  margin-top: 5px;
}

.fee-divider {
  height: 1px;
  background-color: #e0e0e0;
  margin: 15px 0;
}

/* 提示信息 */
.notice-section {
  background-color: #fff9e6;
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 25px;
  text-align: left;
  border: 1px solid #ffe082;
}

.notice-title {
  font-size: 16px;
  font-weight: bold;
  color: #f57c00;
  margin-bottom: 15px;
}

.notice-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.notice-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 14px;
  color: #666;
}

.notice-dot {
  width: 20px;
  height: 20px;
  background-color: #f57c00;
  color: white;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 12px;
  flex-shrink: 0;
}

/* 操作按钮组 */
.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 15px 30px;
  border-radius: 10px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  width: 100%;
}

.action-btn.primary {
  background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
  color: white;
  box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
}

.action-btn.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
}

.action-btn.secondary {
  background-color: white;
  color: #333;
  border: 2px solid #e0e0e0;
}

.action-btn.secondary:hover {
  border-color: #3498db;
  color: #3498db;
  background-color: #f0f8ff;
}

.btn-icon {
  font-size: 18px;
}

/* 按钮 */
.confirm-btn {
  width: 100%;
  max-width: 300px;
  padding: 15px 30px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 18px;
  cursor: pointer;
  display: block;
  margin: 0 auto;
  transition: background-color 0.3s;
}

.confirm-btn:hover {
  background-color: #2980b9;
}

.confirm-btn:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}
</style>