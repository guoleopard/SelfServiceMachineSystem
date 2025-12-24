<script setup>
import { ref } from 'vue'

const emit = defineEmits(['navigate'])

// 模拟科室数据
const departments = [
  { id: 1, name: '内科', doctors: [
    { id: 101, name: '张医生', title: '主任医师', available: ['周一', '周三', '周五'] },
    { id: 102, name: '李医生', title: '副主任医师', available: ['周二', '周四', '周六'] },
    { id: 103, name: '王医生', title: '主治医师', available: ['周一', '周二', '周三', '周四', '周五'] }
  ]},
  { id: 2, name: '外科', doctors: [
    { id: 201, name: '赵医生', title: '主任医师', available: ['周一', '周三', '周五', '周六'] },
    { id: 202, name: '孙医生', title: '副主任医师', available: ['周二', '周四', '周日'] }
  ]},
  { id: 3, name: '妇产科', doctors: [
    { id: 301, name: '刘医生', title: '主任医师', available: ['周一', '周三', '周五'] },
    { id: 302, name: '陈医生', title: '副主任医师', available: ['周二', '周四', '周六'] }
  ]},
  { id: 4, name: '儿科', doctors: [
    { id: 401, name: '周医生', title: '主任医师', available: ['周一', '周二', '周三', '周四', '周五'] },
    { id: 402, name: '吴医生', title: '主治医师', available: ['周六', '周日'] }
  ]},
  { id: 5, name: '眼科', doctors: [
    { id: 501, name: '郑医生', title: '主任医师', available: ['周一', '周三', '周五'] },
    { id: 502, name: '冯医生', title: '副主任医师', available: ['周二', '周四', '周六'] }
  ]}
]

const currentStep = ref(1)
const selectedDepartment = ref(null)
const selectedDoctor = ref(null)
const selectedDate = ref(null)
const selectedTime = ref(null)
const patientInfo = ref({
  name: '',
  idCard: '',
  phone: ''
})

const timeSlots = ['上午 8:00-9:00', '上午 9:00-10:00', '上午 10:00-11:00', '上午 11:00-12:00', '下午 1:30-2:30', '下午 2:30-3:30', '下午 3:30-4:30', '下午 4:30-5:30']

function selectDepartment(department) {
  selectedDepartment.value = department
  currentStep.value = 2
}

function selectDoctor(doctor) {
  selectedDoctor.value = doctor
  currentStep.value = 3
}

function selectDate(date) {
  selectedDate.value = date
  currentStep.value = 4
}

function selectTime(time) {
  selectedTime.value = time
  currentStep.value = 5
}

function submitAppointment() {
  // 模拟提交预约
  alert(`预约成功！\n科室: ${selectedDepartment.value.name}\n医生: ${selectedDoctor.value.name}\n日期: ${selectedDate.value}\n时间: ${selectedTime.value}\n患者: ${patientInfo.value.name}`)
  currentStep.value = 6
}

function goBack() {
  if (currentStep.value > 1) {
    currentStep.value--
  } else {
    emit('navigate', 'home')
  }
}

function goHome() {
  emit('navigate', 'home')
}
</script>

<template>
  <div class="appointment-container">
    <!-- 顶部导航 -->
    <div class="appointment-header">
      <button class="back-btn" @click="goBack">←</button>
      <div class="title">预约挂号</div>
    </div>

    <!-- 步骤导航 -->
    <div class="step-indicator">
      <div :class="['step', { active: currentStep >= 1 }]">1. 选择科室</div>
      <div :class="['step', { active: currentStep >= 2 }]">2. 选择医生</div>
      <div :class="['step', { active: currentStep >= 3 }]">3. 选择日期</div>
      <div :class="['step', { active: currentStep >= 4 }]">4. 选择时间</div>
      <div :class="['step', { active: currentStep >= 5 }]">5. 填写信息</div>
      <div :class="['step', { active: currentStep >= 6 }]">6. 完成预约</div>
    </div>

    <!-- 内容区域 -->
    <div class="appointment-content">
      <!-- 步骤1: 选择科室 -->
      <div v-if="currentStep === 1" class="step-content">
        <h2>请选择科室</h2>
        <div class="department-list">
          <div
            v-for="department in departments"
            :key="department.id"
            class="department-item"
            @click="selectDepartment(department)"
          >
            <div class="department-name">{{ department.name }}</div>
            <div class="department-count">{{ department.doctors.length }}位医生</div>
          </div>
        </div>
      </div>

      <!-- 步骤2: 选择医生 -->
      <div v-if="currentStep === 2" class="step-content">
        <h2>请选择医生</h2>
        <div class="doctor-list">
          <div
            v-for="doctor in selectedDepartment.doctors"
            :key="doctor.id"
            class="doctor-item"
            @click="selectDoctor(doctor)"
          >
            <div class="doctor-info">
              <div class="doctor-name">{{ doctor.name }}</div>
              <div class="doctor-title">{{ doctor.title }}</div>
            </div>
            <div class="doctor-available">
              出诊日: {{ doctor.available.join(', ') }}
            </div>
          </div>
        </div>
      </div>

      <!-- 步骤3: 选择日期 -->
      <div v-if="currentStep === 3" class="step-content">
        <h2>请选择预约日期</h2>
        <div class="date-list">
          <div
            v-for="(date, index) in selectedDoctor.available"
            :key="index"
            class="date-item"
            @click="selectDate(date)"
          >
            {{ date }}
          </div>
        </div>
      </div>

      <!-- 步骤4: 选择时间 -->
      <div v-if="currentStep === 4" class="step-content">
        <h2>请选择预约时间</h2>
        <div class="time-list">
          <div
            v-for="(time, index) in timeSlots"
            :key="index"
            class="time-item"
            @click="selectTime(time)"
          >
            {{ time }}
          </div>
        </div>
      </div>

      <!-- 步骤5: 填写信息 -->
      <div v-if="currentStep === 5" class="step-content">
        <h2>请填写患者信息</h2>
        <div class="form-container">
          <div class="form-group">
            <label>姓名</label>
            <input v-model="patientInfo.name" type="text" placeholder="请输入姓名" />
          </div>
          <div class="form-group">
            <label>身份证号</label>
            <input v-model="patientInfo.idCard" type="text" placeholder="请输入身份证号" />
          </div>
          <div class="form-group">
            <label>联系电话</label>
            <input v-model="patientInfo.phone" type="tel" placeholder="请输入联系电话" />
          </div>
          <button class="submit-btn" @click="submitAppointment" :disabled="!patientInfo.name || !patientInfo.idCard || !patientInfo.phone">
            提交预约
          </button>
        </div>
      </div>

      <!-- 步骤6: 完成预约 -->
      <div v-if="currentStep === 6" class="step-content">
        <div class="success-message">
          <div class="success-icon">✅</div>
          <h2>预约成功！</h2>
          <p>您的预约信息已提交，我们会通过短信通知您具体就诊时间。</p>
          <button class="home-btn" @click="goHome">返回首页</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.appointment-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
}

.appointment-header {
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
  min-width: 120px;
}

.step.active {
  background-color: #3498db;
}

.appointment-content {
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

.department-list, .doctor-list, .date-list, .time-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.department-item, .doctor-item, .date-item, .time-item {
  background-color: #ecf0f1;
  border-radius: 10px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.department-item:hover, .doctor-item:hover, .date-item:hover, .time-item:hover {
  transform: translateY(-2px);
  background-color: #3498db;
  color: white;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.department-name {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 5px;
}

.department-count {
  font-size: 14px;
  color: #7f8c8d;
}

.doctor-info {
  margin-bottom: 10px;
}

.doctor-name {
  font-size: 18px;
  font-weight: 600;
}

.doctor-title {
  font-size: 14px;
  color: #7f8c8d;
}

.doctor-available {
  font-size: 14px;
  color: #7f8c8d;
}

.date-item, .time-item {
  text-align: center;
  font-size: 18px;
  font-weight: 600;
}

.form-container {
  max-width: 500px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-size: 16px;
  color: #2c3e50;
  font-weight: 600;
}

.form-group input {
  width: 100%;
  padding: 15px;
  border: 2px solid #bdc3c7;
  border-radius: 10px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.form-group input:focus {
  outline: none;
  border-color: #3498db;
}

.submit-btn, .home-btn {
  width: 100%;
  padding: 15px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.submit-btn:hover, .home-btn:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.submit-btn:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.success-message {
  text-align: center;
  padding: 40px 20px;
}

.success-icon {
  font-size: 60px;
  margin-bottom: 20px;
}

.success-message h2 {
  font-size: 28px;
  color: #2c3e50;
  margin-bottom: 10px;
}

.success-message p {
  font-size: 16px;
  color: #7f8c8d;
  margin-bottom: 30px;
  line-height: 1.6;
}

.home-btn {
  width: 200px;
  margin: 0 auto;
}
</style>