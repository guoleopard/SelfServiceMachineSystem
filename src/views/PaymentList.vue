<script setup>
import { ref, reactive, onMounted } from 'vue'
import CountdownTimer from '../components/CountdownTimer.vue'
import StepProgress from '../components/StepProgress.vue'
import LoadingSpinner from '../components/LoadingSpinner.vue'

const emit = defineEmits(['navigate'])

const loading = ref(false)

const patientInfo = reactive({
  name: '张三',
  cardNo: '1234567890',
  department: '内科门诊'
})

const paymentItems = ref([
  {
    id: 1,
    type: '检查费',
    name: '血常规检查',
    date: '2024-01-15',
    amount: 85.00,
    status: '待缴费'
  },
  {
    id: 2,
    type: '药品费',
    name: '感冒药（3盒）',
    date: '2024-01-15',
    amount: 128.50,
    status: '待缴费'
  },
  {
    id: 3,
    type: '治疗费',
    name: '输液治疗',
    date: '2024-01-15',
    amount: 256.00,
    status: '待缴费'
  },
  {
    id: 4,
    type: '检查费',
    name: 'CT扫描',
    date: '2024-01-15',
    amount: 580.00,
    status: '待缴费'
  }
])

const selectedItems = ref([])

function toggleSelect(item) {
  const index = selectedItems.value.findIndex(i => i.id === item.id)
  if (index > -1) {
    selectedItems.value.splice(index, 1)
  } else {
    selectedItems.value.push(item)
  }
}

function isSelected(item) {
  return selectedItems.value.some(i => i.id === item.id)
}

function selectAll() {
  if (selectedItems.value.length === paymentItems.value.length) {
    selectedItems.value = []
  } else {
    selectedItems.value = [...paymentItems.value]
  }
}

function getTotalAmount() {
  return selectedItems.value.reduce((sum, item) => sum + item.amount, 0)
}

function goToDetail() {
  if (selectedItems.value.length === 0) {
    alert('请选择至少一个缴费项目')
    return
  }
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('navigate', 'payment-detail', selectedItems.value)
  }, 1000)
}

function goBack() {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('navigate', 'payment-method')
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
  <div class="payment-list-container">
    <CountdownTimer @timeout="handleTimeout" />
    <LoadingSpinner :visible="loading" text="加载中..." />
    
    <div class="header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <h1>待缴费项目</h1>
      <button class="home-btn" @click="goHome">🏠 首页</button>
    </div>
    
    <StepProgress :current-step="2" />

    <div class="patient-info">
      <div class="info-item">
        <span class="label">患者姓名：</span>
        <span class="value">{{ patientInfo.name }}</span>
      </div>
      <div class="info-item">
        <span class="label">就诊卡号：</span>
        <span class="value">{{ patientInfo.cardNo }}</span>
      </div>
      <div class="info-item">
        <span class="label">就诊科室：</span>
        <span class="value">{{ patientInfo.department }}</span>
      </div>
    </div>

    <div class="main-content">
      <div class="select-all-bar">
        <label class="checkbox-label">
          <input 
            type="checkbox" 
            :checked="selectedItems.length === paymentItems.length && paymentItems.length > 0"
            @change="selectAll"
          >
          <span>全选</span>
        </label>
        <span class="selected-count">已选择 {{ selectedItems.length }} 项</span>
      </div>

      <div class="payment-list">
        <div 
          v-for="item in paymentItems" 
          :key="item.id"
          class="payment-item"
          :class="{ selected: isSelected(item) }"
          @click="toggleSelect(item)"
        >
          <div class="item-checkbox">
            <input type="checkbox" :checked="isSelected(item)" @click.stop>
          </div>
          <div class="item-content">
            <div class="item-header">
              <span class="item-type">{{ item.type }}</span>
              <span class="item-date">{{ item.date }}</span>
            </div>
            <div class="item-name">{{ item.name }}</div>
            <div class="item-footer">
              <span class="item-status" :class="item.status">{{ item.status }}</span>
              <span class="item-amount">¥ {{ item.amount.toFixed(2) }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer">
      <div class="total-info">
        <span>合计：</span>
        <span class="total-amount">¥ {{ getTotalAmount().toFixed(2) }}</span>
      </div>
      <button 
        class="pay-btn" 
        :disabled="selectedItems.length === 0"
        @click="goToDetail"
      >
        去缴费
      </button>
    </div>
  </div>
</template>

<style scoped>
.payment-list-container {
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

.patient-info {
  display: flex;
  gap: 40px;
  padding: 20px 40px;
  background: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.info-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.label {
  color: #666;
  font-size: 14px;
}

.value {
  color: #333;
  font-size: 16px;
  font-weight: 600;
}

.main-content {
  flex: 1;
  padding: 20px 40px;
  overflow-y: auto;
}

.select-all-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background: white;
  border-radius: 10px;
  margin-bottom: 15px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  font-size: 16px;
}

.checkbox-label input[type="checkbox"] {
  width: 20px;
  height: 20px;
  cursor: pointer;
}

.selected-count {
  color: #667eea;
  font-weight: 600;
}

.payment-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.payment-item {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 20px;
  background: white;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border: 2px solid transparent;
}

.payment-item:hover {
  transform: translateX(5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}

.payment-item.selected {
  border-color: #667eea;
  background: #f0f4ff;
}

.item-checkbox input[type="checkbox"] {
  width: 22px;
  height: 22px;
  cursor: pointer;
}

.item-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.item-type {
  background: #667eea;
  color: white;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 12px;
}

.item-date {
  color: #999;
  font-size: 14px;
}

.item-name {
  font-size: 18px;
  font-weight: 600;
  color: #333;
}

.item-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.item-status {
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 12px;
}

.item-status.待缴费 {
  background: #fff3e0;
  color: #f57c00;
}

.item-amount {
  font-size: 20px;
  font-weight: bold;
  color: #e74c3c;
}

.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background: white;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
}

.total-info {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 18px;
}

.total-amount {
  font-size: 28px;
  font-weight: bold;
  color: #e74c3c;
}

.pay-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 15px 50px;
  border-radius: 30px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.pay-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}

.pay-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}
</style>
