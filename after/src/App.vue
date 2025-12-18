<template>
  <div class="app-container">
    <!-- 顶部医院信息 -->
    <header class="header">
      <div class="logo">🏥 医院自助服务系统</div>
    </header>

    <!-- 主要内容区域 -->
    <main class="main-content">
      <!-- 首页模块 -->
      <div v-if="currentPage === 'home'" class="home-page">
        <div class="function-grid">
          <div class="function-item" @click="goToPage('readPatient')">
            <div class="item-icon">📅</div>
            <div class="item-text">预约挂号</div>
          </div>
          <div class="function-item" @click="showMessage('功能开发中')">
            <div class="item-icon">🩺</div>
            <div class="item-text">当日挂号</div>
          </div>
          <div class="function-item" @click="showMessage('功能开发中')">
            <div class="item-icon">📝</div>
            <div class="item-text">报告打印</div>
          </div>
          <div class="function-item" @click="showMessage('功能开发中')">
            <div class="item-icon">💳</div>
            <div class="item-text">缴费</div>
          </div>
          <div class="function-item" @click="showMessage('功能开发中')">
            <div class="item-icon">📄</div>
            <div class="item-text">病历查询</div>
          </div>
          <div class="function-item" @click="showMessage('功能开发中')">
            <div class="item-icon">ℹ️</div>
            <div class="item-text">医院信息</div>
          </div>
        </div>
      </div>

      <!-- 读取患者信息页面 -->
      <div v-if="currentPage === 'readPatient'" class="read-patient-page">
        <div class="page-header">
          <button class="back-btn" @click="goToPage('home')">← 返回</button>
          <h2>读取患者信息</h2>
        </div>
        
        <div class="patient-methods">
          <div class="method-item" @click="showCustomInput('idCard')">
            <div class="method-icon">🪪</div>
            <div class="method-text">身份证号</div>
          </div>
          <div class="method-item" @click="showCustomInput('medicalCard')">
            <div class="method-icon">💳</div>
            <div class="method-text">医保卡</div>
          </div>
          <div class="method-item" @click="showCustomInput('electronicCard')">
            <div class="method-icon">📱</div>
            <div class="method-text">电子医保码</div>
          </div>
        </div>
      </div>

      <!-- 患者信息确认页面 -->
      <div v-if="currentPage === 'confirmPatient'" class="confirm-patient-page">
        <div class="page-header">
          <button class="back-btn" @click="reselectPatient()">← 重新选择</button>
          <h2>患者信息确认</h2>
        </div>
        
        <div class="patient-info-card">
          <div class="info-item">
            <label>姓名：</label>
            <span>{{ currentPatient?.name }}</span>
          </div>
          <div class="info-item">
            <label>性别：</label>
            <span>{{ currentPatient?.gender }}</span>
          </div>
          <div class="info-item">
            <label>年龄：</label>
            <span>{{ currentPatient?.age }}岁</span>
          </div>
          <div class="info-item">
            <label>身份证号：</label>
            <span>{{ currentPatient?.id }}</span>
          </div>
          <div class="info-item">
            <label>医保卡卡号：</label>
            <span>{{ currentPatient?.cardNo }}</span>
          </div>
          <div class="info-item">
            <label>联系电话：</label>
            <span>{{ currentPatient?.phone }}</span>
          </div>
        </div>
        
        <div class="confirm-buttons">
          <button class="cancel-btn" @click="reselectPatient()">取消</button>
          <button class="confirm-btn" @click="confirmPatientInfo()">确认并继续</button>
        </div>
      </div>

      <!-- 预约挂号页面 -->
      <div v-if="currentPage === 'registration'" class="registration-page">
        <div class="page-header">
          <button class="back-btn" @click="goToPage('confirmPatient')">← 返回</button>
          <h2>预约挂号 - {{ currentPatient?.name }}</h2>
        </div>

        <div class="department-section">
          <h3>选择科室</h3>
          <div class="department-list">
            <div 
              v-for="dept in departments" 
              :key="dept.id"
              class="department-item"
              :class="{ active: selectedDept === dept.id }"
              @click="selectDepartment(dept.id)"
            >
              {{ dept.name }}
            </div>
          </div>
        </div>

        <div v-if="selectedDept" class="doctor-section">
          <h3>选择医生</h3>
          <div class="doctor-list">
            <div 
              v-for="doctor in getDoctorsByDept(selectedDept)" 
              :key="doctor.id"
              class="doctor-item"
            >
              <div class="doctor-info">
                <div class="doctor-name">{{ doctor.name }}</div>
                <div class="doctor-title">{{ doctor.title }}</div>
                <div class="doctor-specialty">{{ doctor.specialty }}</div>
              </div>
              <div class="doctor-available">
                <div class="available-slots">剩余号源: {{ doctor.availableSlots }}</div>
                <button 
                  class="book-btn"
                  :disabled="doctor.availableSlots <= 0"
                  @click="bookAppointment(doctor)"
                >
                  预约
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- 自定义输入对话框 -->
    <div v-if="showInputDialog" class="dialog-overlay">
      <div class="dialog-content">
        <h3 class="dialog-title">{{ inputDialogTitle }}</h3>
        <input 
          v-if="inputDialogType !== 'confirm'" 
          type="text" 
          class="dialog-input"
          v-model="dialogInputValue"
          placeholder="请输入相关信息"
          autofocus
        >
        <div class="dialog-buttons">
          <button class="dialog-btn dialog-cancel" @click="closeInputDialog()">取消</button>
          <button class="dialog-btn dialog-confirm" @click="confirmInputDialog()">确认</button>
        </div>
      </div>
    </div>

    <!-- 底部设备信息 -->
    <footer class="footer">
      <div class="device-info">
        <span>设备编号: HOS-2024-001</span>
        <span>服务时间: 07:00-19:00</span>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const currentPage = ref('home')
const selectedDept = ref(null)
const currentPatient = ref(null)

// 科室数据
const departments = [
  { id: 1, name: '内科' },
  { id: 2, name: '外科' },
  { id: 3, name: '儿科' },
  { id: 4, name: '妇科' },
  { id: 5, name: '眼科' },
  { id: 6, name: '耳鼻喉科' },
  { id: 7, name: '口腔科' },
  { id: 8, name: '骨科' }
]

// 医生数据
const doctors = [
  { id: 1, deptId: 1, name: '张医生', title: '主任医师', specialty: '心血管内科', availableSlots: 5 },
  { id: 2, deptId: 1, name: '李医生', title: '副主任医师', specialty: '呼吸内科', availableSlots: 8 },
  { id: 3, deptId: 2, name: '王医生', title: '主任医师', specialty: '普外科', availableSlots: 3 },
  { id: 4, deptId: 3, name: '赵医生', title: '主治医师', specialty: '儿童保健', availableSlots: 10 },
  { id: 5, deptId: 4, name: '刘医生', title: '主任医师', specialty: '妇科肿瘤', availableSlots: 6 },
  { id: 6, deptId: 5, name: '陈医生', title: '副主任医师', specialty: '白内障', availableSlots: 4 }
]

// 页面跳转
const goToPage = (page) => {
  currentPage.value = page
  if (page === 'registration') {
    selectedDept.value = null
  } else if (page === 'readPatient') {
    currentPatient.value = null
  }
}

// 选择科室
const selectDepartment = (deptId) => {
  selectedDept.value = deptId
}

// 根据科室获取医生
const getDoctorsByDept = (deptId) => {
  return doctors.filter(doctor => doctor.deptId === deptId)
}

// 模拟患者信息
const mockPatients = [
  { id: '110101199001011234', name: '张三', gender: '男', age: 34, cardNo: '1234567890', phone: '13800138000' },
  { id: '110101199505056789', name: '李四', gender: '女', age: 29, cardNo: '0987654321', phone: '13900139000' },
  { id: '110101200010104567', name: '王五', gender: '男', age: 24, cardNo: '5678901234', phone: '13700137000' }
]

// 读取患者信息
const readPatientInfo = (method, input) => {
  // 模拟根据不同方式获取患者信息
  let patient = null
  
  if (method === 'idCard') {
    patient = mockPatients.find(p => p.id === input)
  } else if (method === 'medicalCard') {
    patient = mockPatients.find(p => p.cardNo === input)
  } else if (method === 'electronicCard') {
    // 电子医保码简单模拟
    patient = mockPatients[0]
  }
  
  if (patient) {
    currentPatient.value = patient
    goToPage('confirmPatient')
  } else {
    alert('未找到患者信息，请检查输入或尝试其他方式')
  }
}

// 确认患者信息
const confirmPatientInfo = () => {
  if (currentPatient.value) {
    goToPage('registration')
  }
}

// 重新选择患者
const reselectPatient = () => {
  currentPatient.value = null
  goToPage('readPatient')
}

// 预约挂号
const bookAppointment = (doctor) => {
  alert(`成功为 ${currentPatient.value?.name} 预约 ${doctor.name} (${doctor.title})\n\n科室: ${departments.find(d => d.id === doctor.deptId)?.name}\n特长: ${doctor.specialty}`)
  goToPage('home')
}

// 自定义输入对话框状态
const showInputDialog = ref(false)
const inputDialogTitle = ref('')
const inputDialogType = ref('') // 'text' 或 'confirm'
const currentInputMethod = ref('')
const dialogInputValue = ref('')

// 显示自定义输入对话框
const showCustomInput = (method) => {
  currentInputMethod.value = method
  
  if (method === 'idCard') {
    inputDialogTitle.value = '请输入身份证号'
    inputDialogType.value = 'text'
    dialogInputValue.value = ''
    showInputDialog.value = true
  } else if (method === 'medicalCard') {
    inputDialogTitle.value = '请输入医保卡卡号'
    inputDialogType.value = 'text'
    dialogInputValue.value = ''
    showInputDialog.value = true
  } else if (method === 'electronicCard') {
    inputDialogTitle.value = '电子医保码'
    inputDialogType.value = 'confirm'
    showInputDialog.value = true
  }
}

// 关闭自定义输入对话框
const closeInputDialog = () => {
  showInputDialog.value = false
  dialogInputValue.value = ''
}

// 确认自定义输入对话框
const confirmInputDialog = () => {
  if (inputDialogType.value === 'text') {
    if (dialogInputValue.value.trim()) {
      readPatientInfo(currentInputMethod.value, dialogInputValue.value.trim())
      closeInputDialog()
    } else {
      alert('请输入必要信息')
    }
  } else if (inputDialogType.value === 'confirm') {
    readPatientInfo(currentInputMethod.value, '')
    closeInputDialog()
  }
}

// 显示消息
const showMessage = (message) => {
  alert(message)
}
</script>

<style scoped>
.app-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f7fa;
}

/* 自定义输入对话框样式 */
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.dialog-content {
  background-color: white;
  border-radius: 8px;
  padding: 2rem;
  width: 90%;
  max-width: 400px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.dialog-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  text-align: center;
}

.dialog-input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e1e8ed;
  border-radius: 6px;
  font-size: 1rem;
  margin-bottom: 1.5rem;
  box-sizing: border-box;
  transition: border-color 0.3s ease;
}

.dialog-input:focus {
  outline: none;
  border-color: #3498db;
}

.dialog-buttons {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}

.dialog-btn {
  flex: 1;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.dialog-cancel {
  background-color: #e74c3c;
  color: white;
}

.dialog-cancel:hover {
  background-color: #c0392b;
}

.dialog-confirm {
  background-color: #3498db;
  color: white;
}

.dialog-confirm:hover {
  background-color: #2980b9;
}

.header {
  background-color: #2c3e50;
  color: white;
  padding: 1rem;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.main-content {
  flex: 1;
  overflow-y: auto;
  padding: 2rem;
}

/* 首页样式 */
.function-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.function-item {
  background-color: white;
  border-radius: 12px;
  padding: 2rem 1rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.function-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.item-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.item-text {
  font-size: 1.1rem;
  font-weight: 500;
  color: #333;
}

/* 读取患者信息页面样式 */
.read-patient-page {
  max-width: 800px;
  margin: 0 auto;
}

.patient-methods {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3rem;
}

.method-item {
  background-color: white;
  border-radius: 12px;
  padding: 2.5rem 1rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.method-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.method-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.method-text {
  font-size: 1.2rem;
  font-weight: 500;
  color: #333;
}

/* 患者信息确认页面样式 */
.confirm-patient-page {
  max-width: 700px;
  margin: 0 auto;
}

.patient-info-card {
  background-color: white;
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.info-item {
  display: flex;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid #e9ecef;
}

.info-item:last-child {
  border-bottom: none;
}

.info-item label {
  font-weight: 600;
  color: #2c3e50;
  min-width: 120px;
}

.info-item span {
  color: #333;
}

.confirm-buttons {
  display: flex;
  justify-content: center;
  gap: 2rem;
}

.cancel-btn {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 0.8rem 2rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
}

.cancel-btn:hover {
  background-color: #c0392b;
}

.confirm-btn {
  background-color: #27ae60;
  color: white;
  border: none;
  padding: 0.8rem 2rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
}

.confirm-btn:hover {
  background-color: #219a52;
}

/* 预约挂号页面样式 */
.registration-page {
  max-width: 900px;
  margin: 0 auto;
}

.page-header {
  display: flex;
  align-items: center;
  margin-bottom: 2rem;
}

.back-btn {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  margin-right: 1rem;
  font-size: 1rem;
}

.back-btn:hover {
  background-color: #2980b9;
}

.department-section,
.doctor-section {
  background-color: white;
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.department-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.department-item {
  background-color: #f8f9fa;
  border: 2px solid transparent;
  border-radius: 8px;
  padding: 1rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.department-item:hover {
  background-color: #e9ecef;
}

.department-item.active {
  background-color: #3498db;
  color: white;
  border-color: #3498db;
}

.doctor-list {
  margin-top: 1rem;
}

.doctor-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  margin-bottom: 1rem;
  background-color: #fafbfc;
}

.doctor-info {
  flex: 1;
}

.doctor-name {
  font-size: 1.3rem;
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 0.3rem;
}

.doctor-title {
  color: #3498db;
  font-size: 1rem;
  margin-bottom: 0.3rem;
}

.doctor-specialty {
  color: #666;
  font-size: 0.9rem;
}

.doctor-available {
  text-align: center;
}

.available-slots {
  color: #27ae60;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.book-btn {
  background-color: #27ae60;
  color: white;
  border: none;
  padding: 0.5rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
}

.book-btn:hover:not(:disabled) {
  background-color: #219a52;
}

.book-btn:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.footer {
  background-color: #2c3e50;
  color: white;
  padding: 1rem;
  text-align: center;
}

.device-info {
  display: flex;
  justify-content: space-around;
  font-size: 0.9rem;
}

/* 竖屏适配 */
@media (max-width: 768px) {
  .function-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }

  .patient-methods {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }

  .main-content {
    padding: 1rem;
  }

  .department-list {
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  }

  .doctor-item {
    flex-direction: column;
    align-items: flex-start;
  }

  .doctor-available {
    align-self: stretch;
    margin-top: 1rem;
  }

  .confirm-buttons {
    flex-direction: column;
    gap: 1rem;
  }

  .info-item {
    flex-direction: column;
    align-items: flex-start;
  }

  .info-item label {
    margin-bottom: 0.5rem;
  }
}
</style>