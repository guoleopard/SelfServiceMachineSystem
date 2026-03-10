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
  orderNo: 'PAY202401150001',
  selfAmount: 76.50,
  items: ['血常规检查', '心电图检查']
}

const paymentData = ref(props.paymentData || defaultData)

function goHome() {
  emit('navigate', 'home')
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
  <div class="payment-complete-container">
    <Loading v-if="loading" text="正在处理支付结果..." />
    <div class="header">
      <div class="title">缴费完成</div>
      <div class="countdown">{{ countdown }}s</div>
    </div>
    
    <StepIndicator :currentStep="5" />
    
    <div class="main-content">
      <div class="success-icon">
        <div class="checkmark">✓</div>
      </div>
      
      <h1 class="success-title">缴费成功</h1>
      <p class="success-message">您的缴费已成功完成</p>
      
      <div class="payment-info">
        <div class="info-row">
          <span class="label">订单号:</span>
          <span class="value">{{ paymentData.orderNo }}</span>
        </div>
        <div class="info-row">
          <span class="label">缴费项目:</span>
          <span class="value">{{ paymentData.items?.join('、') }}</span>
        </div>
        <div class="info-row highlight">
          <span class="label">支付金额:</span>
          <span class="value amount">¥{{ paymentData.selfAmount?.toFixed(2) }}</span>
        </div>
      </div>
      
      <div class="tips">
        <p>💡 温馨提示:</p>
        <ul>
          <li>请凭缴费凭证到相应科室进行检查</li>
          <li>如需发票，请前往收费窗口打印</li>
          <li>如有疑问，请咨询服务台</li>
        </ul>
      </div>
      
      <button class="home-btn" @click="goHome">返回首页</button>
    </div>
    
    <div class="footer">
      <p>感谢您使用自助缴费服务</p>
    </div>
  </div>
</template>

<style scoped>
.payment-complete-container {
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
  text-align: center;
}

.success-icon {
  width: 120px;
  height: 120px;
  background-color: #27ae60;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 30px;
  animation: pulse 2s infinite;
}

.checkmark {
  font-size: 72px;
  color: white;
  font-weight: bold;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(39, 174, 96, 0.7);
  }
  70% {
    box-shadow: 0 0 0 20px rgba(39, 174, 96, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(39, 174, 96, 0);
  }
}

.success-title {
  font-size: 36px;
  color: #27ae60;
  margin-bottom: 10px;
}

.success-message {
  font-size: 18px;
  color: #666;
  margin-bottom: 40px;
}

.payment-info {
  background-color: white;
  border-radius: 15px;
  padding: 30px;
  width: 100%;
  max-width: 500px;
  margin-bottom: 30px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.info-row {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  border-bottom: 1px solid #eee;
}

.info-row:last-child {
  border-bottom: none;
}

.label {
  color: #666;
}

.value {
  color: #333;
  font-weight: 500;
}

.highlight {
  background-color: #f8f9fa;
  margin: 10px -30px -10px;
  padding: 15px 30px;
  border-radius: 0 0 15px 15px;
}

.highlight .amount {
  color: #e74c3c;
  font-size: 24px;
  font-weight: bold;
}

.tips {
  background-color: #fff3cd;
  border-radius: 10px;
  padding: 20px;
  width: 100%;
  max-width: 500px;
  margin-bottom: 30px;
  text-align: left;
}

.tips p {
  font-weight: bold;
  color: #856404;
  margin-bottom: 10px;
}

.tips ul {
  margin: 0;
  padding-left: 20px;
  color: #856404;
}

.tips li {
  margin: 5px 0;
}

.home-btn {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 15px 50px;
  font-size: 20px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.home-btn:hover {
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
