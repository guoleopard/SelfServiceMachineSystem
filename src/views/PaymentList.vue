<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import Loading from '../components/Loading.vue'
import StepIndicator from '../components/StepIndicator.vue'

const emit = defineEmits(['navigate'])

const loading = ref(true)

const countdown = ref(90)
let timer = null

// 模拟缴费数据
const paymentItems = ref([
  {
    id: 1,
    orderNo: 'PAY202401150001',
    date: '2024-01-15',
    department: '内科门诊',
    doctor: '张医生',
    items: ['血常规检查', '心电图检查'],
    totalAmount: 256.50,
    medicareAmount: 180.00,
    selfAmount: 76.50,
    status: 'unpaid'
  },
  {
    id: 2,
    orderNo: 'PAY202401150002',
    date: '2024-01-15',
    department: '外科门诊',
    doctor: '李医生',
    items: ['换药费', '消炎药'],
    totalAmount: 189.00,
    medicareAmount: 120.00,
    selfAmount: 69.00,
    status: 'unpaid'
  },
  {
    id: 3,
    orderNo: 'PAY202401140001',
    date: '2024-01-14',
    department: '眼科门诊',
    doctor: '王医生',
    items: ['视力检查', '眼药水'],
    totalAmount: 156.00,
    medicareAmount: 100.00,
    selfAmount: 56.00,
    status: 'paid'
  }
])

// 只显示未缴费的数据
const unpaidItems = computed(() => {
  return paymentItems.value.filter(item => item.status === 'unpaid')
})

function selectItem(item) {
  if (item.status === 'unpaid') {
    emit('navigate', 'payment-detail', item)
  }
}

function goBack() {
  emit('navigate', 'payment-select')
}

onMounted(() => {
  // 模拟数据加载
  setTimeout(() => {
    loading.value = false
  }, 800)
  
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
  <div class="payment-list-container">
    <Loading v-if="loading" text="正在加载缴费信息..." />
    <StepIndicator :currentStep="2" />
    <div class="header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <div class="title">待缴费列表</div>
      <div class="countdown">{{ countdown }}s</div>
    </div>
    
    <div class="main-content">
      <div class="list-header">
        <span>共 {{ unpaidItems.length }} 条待缴费记录</span>
        <span class="tip">点击选择缴费项目</span>
      </div>
      
      <div class="payment-list">
        <div
          v-for="item in unpaidItems"
          :key="item.id"
          class="payment-item"
          @click="selectItem(item)"
        >
          <div class="item-header">
            <span class="order-no">订单号: {{ item.orderNo }}</span>
            <span class="date">{{ item.date }}</span>
            <span class="status" :class="item.status">{{ item.status === 'paid' ? '已缴费' : '待缴费' }}</span>
          </div>
          
          <div class="item-body">
            <div class="item-info">
              <p><strong>科室:</strong> {{ item.department }}</p>
              <p><strong>医生:</strong> {{ item.doctor }}</p>
              <p><strong>项目:</strong> {{ item.items.join('、') }}</p>
            </div>
            <div class="item-amount">
              <p class="total">总计: ¥{{ item.totalAmount.toFixed(2) }}</p>
              <p class="medicare">医保: ¥{{ item.medicareAmount.toFixed(2) }}</p>
              <p class="self">自费: ¥{{ item.selfAmount.toFixed(2) }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="footer">
      <p>请选择需要缴费的项目</p>
    </div>
  </div>
</template>

<style scoped>
.payment-list-container {
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
  padding: 20px 40px;
  overflow-y: auto;
}

.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background-color: white;
  border-radius: 10px;
  margin-bottom: 20px;
  font-size: 16px;
}

.tip {
  color: #666;
}

.payment-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.payment-item {
  background-color: white;
  border-radius: 10px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.payment-item:hover:not(.paid) {
  transform: translateX(5px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
  border-left: 4px solid #3498db;
}

.payment-item.paid {
  opacity: 0.7;
  cursor: not-allowed;
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
  margin-bottom: 15px;
}

.order-no {
  font-weight: bold;
  color: #333;
}

.date {
  color: #666;
}

.status {
  padding: 3px 10px;
  border-radius: 15px;
  font-size: 14px;
  font-weight: bold;
}

.status.unpaid {
  background-color: #fff3cd;
  color: #856404;
}

.status.paid {
  background-color: #d4edda;
  color: #155724;
}

.item-body {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.item-info p {
  margin: 8px 0;
  color: #555;
}

.item-amount {
  text-align: right;
}

.item-amount p {
  margin: 5px 0;
}

.total {
  font-size: 18px;
  font-weight: bold;
  color: #e74c3c;
}

.medicare {
  color: #27ae60;
}

.self {
  color: #3498db;
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
