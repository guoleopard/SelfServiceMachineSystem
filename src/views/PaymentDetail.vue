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

// 默认数据（如果没有传入props）
const defaultData = {
  orderNo: 'PAY202401150001',
  date: '2024-01-15',
  department: '内科门诊',
  doctor: '张医生',
  items: ['血常规检查', '心电图检查'],
  totalAmount: 256.50,
  medicareAmount: 180.00,
  selfAmount: 76.50
}

const paymentData = ref(props.paymentData || defaultData)

function goToPay() {
  emit('navigate', 'pay-method-select', paymentData.value)
}

function goBack() {
  emit('navigate', 'payment-list')
}

onMounted(() => {
  // 模拟数据加载
  setTimeout(() => {
    loading.value = false
  }, 600)
  
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
  <div class="payment-detail-container">
    <Loading v-if="loading" text="正在加载订单详情..." />
    <div class="header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <div class="title">缴费详情</div>
      <div class="countdown">{{ countdown }}s</div>
    </div>
    
    <StepIndicator :currentStep="3" />
    
    <div class="main-content">
      <div class="detail-card">
        <div class="card-header">
          <h3>订单信息</h3>
        </div>
        
        <div class="card-body">
          <div class="info-row">
            <span class="label">订单号:</span>
            <span class="value">{{ paymentData.orderNo }}</span>
          </div>
          
          <div class="info-row">
            <span class="label">就诊日期:</span>
            <span class="value">{{ paymentData.date }}</span>
          </div>
          
          <div class="info-row">
            <span class="label">就诊科室:</span>
            <span class="value">{{ paymentData.department }}</span>
          </div>
          
          <div class="info-row">
            <span class="label">主治医生:</span>
            <span class="value">{{ paymentData.doctor }}</span>
          </div>
          
          <div class="info-row">
            <span class="label">缴费项目:</span>
            <span class="value">{{ paymentData.items?.join('、') }}</span>
          </div>
          
          <div class="divider"></div>
          
          <div class="amount-section">
            <div class="amount-row">
              <span class="label">总金额:</span>
              <span class="value total">¥{{ paymentData.totalAmount?.toFixed(2) }}</span>
            </div>
            
            <div class="amount-row">
              <span class="label">医保统筹支付:</span>
              <span class="value medicare">¥{{ paymentData.medicareAmount?.toFixed(2) }}</span>
            </div>
            
            <div class="amount-row highlight">
              <span class="label">待支付金额(自费):</span>
              <span class="value self">¥{{ paymentData.selfAmount?.toFixed(2) }}</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="action-buttons">
        <button class="btn btn-primary" @click="goToPay">立即缴费</button>
      </div>
    </div>
    
    <div class="footer">
      <p>请确认缴费信息无误后进行支付</p>
    </div>
  </div>
</template>

<style scoped>
.payment-detail-container {
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
  padding: 30px 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.detail-card {
  background-color: white;
  border-radius: 15px;
  width: 100%;
  max-width: 600px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.card-header {
  background-color: #3498db;
  color: white;
  padding: 20px;
}

.card-header h3 {
  margin: 0;
  font-size: 20px;
}

.card-body {
  padding: 30px;
}

.info-row {
  display: flex;
  padding: 12px 0;
  border-bottom: 1px solid #eee;
}

.label {
  width: 120px;
  color: #666;
  flex-shrink: 0;
}

.value {
  flex: 1;
  color: #333;
  font-weight: 500;
}

.divider {
  height: 1px;
  background-color: #ddd;
  margin: 20px 0;
}

.amount-section {
  background-color: #f8f9fa;
  border-radius: 10px;
  padding: 20px;
}

.amount-row {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
}

.amount-row .label {
  width: auto;
}

.amount-row .value {
  font-size: 18px;
}

.total {
  color: #333;
}

.medicare {
  color: #27ae60;
}

.highlight {
  background-color: #fff3cd;
  margin: 10px -20px -10px;
  padding: 15px 20px;
  border-radius: 0 0 10px 10px;
}

.highlight .label {
  font-weight: bold;
}

.highlight .self {
  color: #e74c3c;
  font-size: 24px;
  font-weight: bold;
}

.action-buttons {
  margin-top: 30px;
  width: 100%;
  max-width: 600px;
}

.btn {
  width: 100%;
  padding: 15px;
  font-size: 20px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background-color: #3498db;
  color: white;
}

.btn-primary:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
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
