<template>
  <div class="patient-info-reader">
    <div class="page-header">
      <button class="back-btn" @click="$emit('back')">← 返回</button>
      <h2>读取患者信息</h2>
    </div>
    
    <div class="content">
      <div class="info-card">
        <p class="description">请选择以下方式之一获取患者信息</p>
        
        <div class="method-grid">
          <!-- 身份证号方式 -->
          <div class="method-item" @click="selectMethod('idCard')">
            <div class="method-icon">🪪</div>
            <div class="method-title">身份证号</div>
            <div class="method-description">手动输入身份证号码</div>
          </div>
          
          <!-- 医保卡方式 -->
          <div class="method-item" @click="selectMethod('medicalCard')">
            <div class="method-icon">💳</div>
            <div class="method-title">医保卡</div>
            <div class="method-description">刷卡或输入医保卡号码</div>
          </div>
          
          <!-- 电子医保码方式 -->
          <div class="method-item" @click="selectMethod('electronicCard')">
            <div class="method-icon">📱</div>
            <div class="method-title">电子医保码</div>
            <div class="method-description">扫描二维码或输入医保码</div>
          </div>
        </div>
      </div>
      
      <!-- 输入区域 -->
      <div v-if="selectedMethod" class="input-section">
        <div class="input-card">
          <h3>{{ getMethodTitle(selectedMethod) }}</h3>
          <input 
            v-model="inputValue" 
            type="text" 
            placeholder="请输入{{ getMethodPlaceholder(selectedMethod) }}"
            class="input-field"
            @keyup.enter="fetchPatientInfo"
          >
          <div class="button-group">
            <button class="btn btn-secondary" @click="cancelInput">取消</button>
            <button class="btn btn-primary" @click="fetchPatientInfo" :disabled="!inputValue.trim()">
              获取信息
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <Footer />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Footer from './Footer.vue'

const emit = defineEmits(['back', 'patientInfoFetched', 'goToIDCardInput']) 

const selectedMethod = ref(null)
const inputValue = ref('')

// 模拟患者数据
const mockPatients = [
  {
    id: '1',
    name: '张三',
    idCard: '110101199001011234',
    medicalCard: 'MC123456789',
    electronicCard: 'EC987654321',
    gender: '男',
    age: 34,
    phone: '13800138000'
  },
  {
    id: '2',
    name: '李四',
    idCard: '110101198505056789',
    medicalCard: 'MC987654321',
    electronicCard: 'EC123456789',
    gender: '女',
    age: 39,
    phone: '13900139000'
  }
]

// 选择获取方式
const selectMethod = (method) => {
  if (method === 'idCard') {
    // 跳转到身份证号输入页面
    emit('goToIDCardInput')
  } else {
    selectedMethod.value = method
    inputValue.value = ''
  }
}

// 取消输入
const cancelInput = () => {
  selectedMethod.value = null
  inputValue.value = ''
}

// 获取方式标题
const getMethodTitle = (method) => {
  const titles = {
    idCard: '身份证号',
    medicalCard: '医保卡',
    electronicCard: '电子医保码'
  }
  return titles[method] || ''
}

// 获取方式占位符
const getMethodPlaceholder = (method) => {
  const placeholders = {
    idCard: '身份证号码',
    medicalCard: '医保卡号码',
    electronicCard: '电子医保码'
  }
  return placeholders[method] || ''
}

// 获取患者信息
const fetchPatientInfo = () => {
  if (!inputValue.value.trim()) return
  
  // 模拟根据输入值查找患者
  let patient = null
  for (let p of mockPatients) {
    if (p.idCard === inputValue.value || 
        p.medicalCard === inputValue.value || 
        p.electronicCard === inputValue.value) {
      patient = p
      break
    }
  }
  
  if (patient) {
    emit('patientInfoFetched', patient)
  } else {
    alert('未找到患者信息，请检查输入是否正确')
  }
}
</script>

<style scoped>
.patient-info-reader {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f8f9fa;
}

.page-header {
  background: white;
  padding: 20px 40px;
  display: flex;
  align-items: center;
  gap: 20px;
  border-bottom: 1px solid #e9ecef;
}

.back-btn {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 8px 16px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
}

.back-btn:hover {
  background: #e9ecef;
}

.page-header h2 {
  margin: 0;
  color: #2c3e50;
  font-size: 24px;
  font-weight: 600;
}

.content {
  flex: 1;
  padding: 40px;
  overflow-y: auto;
}

.info-card {
  background: white;
  border-radius: 12px;
  padding: 30px;
  margin-bottom: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.description {
  text-align: center;
  color: #6c757d;
  font-size: 16px;
  margin-bottom: 30px;
}

.method-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  max-width: 900px;
  margin: 0 auto;
}

.method-item {
  background: #f8f9fa;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  padding: 30px 20px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.method-item:hover {
  background: #e3f2fd;
  border-color: #4a90e2;
  transform: translateY(-5px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.method-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.method-title {
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 8px;
}

.method-description {
  font-size: 13px;
  color: #6c757d;
}

.input-section {
  max-width: 600px;
  margin: 0 auto;
}

.input-card {
  background: white;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.input-card h3 {
  margin: 0 0 20px 0;
  color: #2c3e50;
  font-size: 20px;
  font-weight: 600;
}

.input-field {
  width: 100%;
  padding: 15px 20px;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 16px;
  margin-bottom: 20px;
  transition: all 0.3s ease;
}

.input-field:focus {
  outline: none;
  border-color: #4a90e2;
  box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.1);
}

.button-group {
  display: flex;
  gap: 12px;
  justify-content: center;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .content {
    padding: 20px;
  }
  
  .method-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }
  
  .page-header {
    padding: 15px 20px;
  }
  
  .page-header h2 {
    font-size: 18px;
  }
}
</style>
