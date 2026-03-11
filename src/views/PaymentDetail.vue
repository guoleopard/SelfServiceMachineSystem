<script setup>
import { ref, computed, onMounted } from 'vue'
import CountdownTimer from '../components/CountdownTimer.vue'
import StepProgress from '../components/StepProgress.vue'
import LoadingSpinner from '../components/LoadingSpinner.vue'

const props = defineProps({
  paymentItems: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['navigate'])

const loading = ref(false)

const paymentData = ref(props.paymentItems.length > 0 ? props.paymentItems : [
  { id: 1, type: '检查费', name: '血常规检查', amount: 85.00 },
  { id: 2, type: '药品费', name: '感冒药（3盒）', amount: 128.50 }
])

const patientInfo = ref({
  name: '张三',
  cardNo: '1234567890',
  department: '内科门诊',
  doctor: '王医生'
})

const totalAmount = computed(() => {
  return paymentData.value.reduce((sum, item) => sum + item.amount, 0)
})

const insuranceCoverage = computed(() => {
  return (totalAmount.value * 0.6).toFixed(2)
})

const selfPayAmount = computed(() => {
  return totalAmount.value * 0.4
})

function goToPay() {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('navigate', 'pay-method', {
      items: paymentData.value,
      totalAmount: totalAmount.value,
      selfPayAmount: selfPayAmount.value
    })
  }, 1000)
}

function goBack() {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('navigate', 'payment-list')
  }, 500)
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
  <div class="payment-detail-container">
    <CountdownTimer @timeout="handleTimeout" />
    <LoadingSpinner :visible="loading" text="加载中..." />
    
    <div class="header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <h1>缴费详情</h1>
      <button class="home-btn" @click="goHome">🏠 首页</button>
    </div>
    
    <StepProgress :current-step="3" />

    <div class="main-content">
      <div class="patient-card">
        <h3>患者信息</h3>
        <div class="info-grid">
          <div class="info-item">
            <span class="label">姓名：</span>
            <span class="value">{{ patientInfo.name }}</span>
          </div>
          <div class="info-item">
            <span class="label">就诊卡号：</span>
            <span class="value">{{ patientInfo.cardNo }}</span>
          </div>
          <div class="info-item">
            <span class="label">科室：</span>
            <span class="value">{{ patientInfo.department }}</span>
          </div>
          <div class="info-item">
            <span class="label">医生：</span>
            <span class="value">{{ patientInfo.doctor }}</span>
          </div>
        </div>
      </div>

      <div class="items-card">
        <h3>缴费项目明细</h3>
        <table class="items-table">
          <thead>
            <tr>
              <th>项目类型</th>
              <th>项目名称</th>
              <th>金额（元）</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in paymentData" :key="item.id">
              <td>{{ item.type }}</td>
              <td>{{ item.name }}</td>
              <td class="amount">{{ item.amount.toFixed(2) }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="summary-card">
        <h3>费用明细</h3>
        <div class="summary-item">
          <span class="label">总费用：</span>
          <span class="value">¥ {{ totalAmount.toFixed(2) }}</span>
        </div>
        <div class="summary-item highlight">
          <span class="label">医保统筹支付：</span>
          <span class="value insurance">¥ {{ insuranceCoverage }}</span>
        </div>
        <div class="divider"></div>
        <div class="summary-item total">
          <span class="label">个人自费金额：</span>
          <span class="value self-pay">¥ {{ selfPayAmount.toFixed(2) }}</span>
        </div>
      </div>
    </div>

    <div class="footer">
      <button class="confirm-btn" @click="goToPay">
        确认支付自费部分 ¥ {{ selfPayAmount.toFixed(2) }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.payment-detail-container {
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
  padding: 30px 40px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.patient-card, .items-card, .summary-card {
  background: white;
  border-radius: 15px;
  padding: 25px;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
}

.patient-card h3, .items-card h3, .summary-card h3 {
  margin: 0 0 20px 0;
  color: #333;
  font-size: 18px;
  padding-bottom: 10px;
  border-bottom: 2px solid #667eea;
  display: inline-block;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.info-item .label {
  color: #666;
  font-size: 14px;
  min-width: 80px;
}

.info-item .value {
  color: #333;
  font-size: 16px;
  font-weight: 600;
}

.items-table {
  width: 100%;
  border-collapse: collapse;
}

.items-table th, .items-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.items-table th {
  background: #f8f9fa;
  color: #666;
  font-weight: 600;
}

.items-table tr:hover td {
  background: #f8f9fa;
}

.amount {
  font-weight: 600;
  color: #e74c3c;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  font-size: 16px;
}

.summary-item.highlight {
  background: #e8f5e9;
  margin: 10px -25px;
  padding: 15px 25px;
}

.summary-item .label {
  color: #666;
}

.summary-item .value {
  font-weight: 600;
  color: #333;
}

.summary-item .value.insurance {
  color: #2e7d32;
}

.divider {
  height: 1px;
  background: #eee;
  margin: 10px 0;
}

.summary-item.total {
  padding-top: 15px;
  border-top: 2px dashed #ddd;
}

.summary-item.total .label {
  font-size: 18px;
  font-weight: 600;
}

.summary-item.total .value.self-pay {
  font-size: 24px;
  color: #e74c3c;
}

.footer {
  padding: 20px 40px;
  background: white;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: center;
}

.confirm-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 18px 60px;
  border-radius: 35px;
  font-size: 20px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.confirm-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}
</style>
