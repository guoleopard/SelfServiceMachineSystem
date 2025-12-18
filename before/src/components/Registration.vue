<template>
  <div class="registration-container">
    <!-- 科室选择 -->
    <div class="section">
      <h3>选择科室</h3>
      <div class="department-grid">
        <div 
          v-for="dept in departments" 
          :key="dept.id"
          class="department-item"
          :class="{ active: selectedDept === dept.id }"
          @click="selectDepartment(dept.id)"
        >
          <div class="dept-icon">{{ dept.icon }}</div>
          <div class="dept-name">{{ dept.name }}</div>
        </div>
      </div>
    </div>

    <!-- 医生列表 -->
    <div v-if="selectedDept" class="section">
      <h3>选择医生</h3>
      <div class="doctor-list">
        <div 
          v-for="doctor in filteredDoctors" 
          :key="doctor.id"
          class="doctor-item"
        >
          <div class="doctor-info">
            <div class="doctor-name">{{ doctor.name }}</div>
            <div class="doctor-title">{{ doctor.title }}</div>
            <div class="doctor-department">{{ doctor.department }}</div>
            <div class="doctor-specialty">擅长：{{ doctor.specialty }}</div>
          </div>
          <div class="doctor-actions">
            <div class="available-slots">剩余号源：{{ doctor.availableSlots }}</div>
            <button 
              class="btn btn-primary book-btn"
              :disabled="doctor.availableSlots <= 0"
              @click="bookAppointment(doctor)"
            >
              {{ doctor.availableSlots > 0 ? '预约' : '约满' }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- 预约成功提示 -->
    <div v-if="showSuccess" class="success-modal">
      <div class="success-content">
        <div class="success-icon">✅</div>
        <h3>预约成功！</h3>
        <p>您已成功预约 {{ bookedDoctor?.name }} 医生</p>
        <p class="appointment-number">预约号：{{ appointmentNumber }}</p>
        <button class="btn btn-primary" @click="closeSuccess">确定</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// 科室数据
const departments = ref([
  { id: 1, name: '内科', icon: '❤️' },
  { id: 2, name: '外科', icon: '🩺' },
  { id: 3, name: '儿科', icon: '👶' },
  { id: 4, name: '妇科', icon: '👩' },
  { id: 5, name: '眼科', icon: '👁️' },
  { id: 6, name: '耳鼻喉科', icon: '👃' },
  { id: 7, name: '口腔科', icon: '🦷' },
  { id: 8, name: '皮肤科', icon: '🤚' },
  { id: 9, name: '中医科', icon: '🌿' }
])

// 医生数据
const doctors = ref([
  { id: 101, name: '张三', title: '主任医师', department: '内科', specialty: '心血管疾病、高血压、冠心病', availableSlots: 5 },
  { id: 102, name: '李四', title: '副主任医师', department: '内科', specialty: '消化系统疾病、肠胃病', availableSlots: 3 },
  { id: 103, name: '王五', title: '主任医师', department: '外科', specialty: '骨科手术、关节置换', availableSlots: 4 },
  { id: 104, name: '赵六', title: '主治医师', department: '儿科', specialty: '儿童常见病、呼吸道感染', availableSlots: 6 },
  { id: 105, name: '孙七', title: '主任医师', department: '妇科', specialty: '妇科肿瘤、不孕症', availableSlots: 2 },
  { id: 106, name: '周八', title: '副主任医师', department: '眼科', specialty: '白内障、青光眼', availableSlots: 7 },
  { id: 107, name: '吴九', title: '主治医师', department: '耳鼻喉科', specialty: '鼻炎、鼻窦炎、中耳炎', availableSlots: 5 },
  { id: 108, name: '郑十', title: '主任医师', department: '口腔科', specialty: '种植牙、牙齿矫正', availableSlots: 3 },
  { id: 109, name: '陈一', title: '副主任医师', department: '皮肤科', specialty: '痤疮、湿疹、银屑病', availableSlots: 4 },
  { id: 110, name: '林二', title: '主任医师', department: '中医科', specialty: '中医调理、针灸推拿', availableSlots: 6 }
])

// 状态管理
const selectedDept = ref(null)
const showSuccess = ref(false)
const bookedDoctor = ref(null)
const appointmentNumber = ref('')

// 过滤医生
const filteredDoctors = computed(() => {
  if (!selectedDept.value) return []
  const dept = departments.value.find(d => d.id === selectedDept.value)
  return doctors.value.filter(doctor => doctor.department === dept?.name)
})

// 选择科室
const selectDepartment = (deptId) => {
  selectedDept.value = deptId
}

// 预约
const bookAppointment = (doctor) => {
  if (doctor.availableSlots <= 0) return
  
  bookedDoctor.value = doctor
  appointmentNumber.value = 'AP' + Date.now().toString().slice(-8)
  showSuccess.value = true
  
  // 更新号源
  doctor.availableSlots--
}

// 关闭成功提示
const closeSuccess = () => {
  showSuccess.value = false
  bookedDoctor.value = null
}
</script>

<style scoped>
.registration-container {
  max-width: 1200px;
  margin: 0 auto;
}

.section {
  background: white;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.section h3 {
  margin: 0 0 20px 0;
  color: #2c3e50;
  font-size: 20px;
  font-weight: 600;
}

/* 科室选择 */
.department-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
}

.department-item {
  background: #f8f9fa;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  padding: 20px 12px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.department-item:hover {
  background: #e9ecef;
  border-color: #4a90e2;
}

.department-item.active {
  background: #e3f2fd;
  border-color: #4a90e2;
}

.dept-icon {
  font-size: 32px;
  margin-bottom: 8px;
}

.dept-name {
  font-size: 14px;
  font-weight: 500;
  color: #2c3e50;
}

/* 医生列表 */
.doctor-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.doctor-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 12px;
  transition: all 0.3s ease;
}

.doctor-item:hover {
  background: #e9ecef;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.doctor-info {
  flex: 1;
}

.doctor-name {
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 4px;
}

.doctor-title {
  font-size: 14px;
  color: #4a90e2;
  margin-bottom: 4px;
}

.doctor-department {
  font-size: 13px;
  color: #7f8c8d;
  margin-bottom: 4px;
}

.doctor-specialty {
  font-size: 13px;
  color: #555;
}

.doctor-actions {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  min-width: 150px;
}

.available-slots {
  font-size: 13px;
  color: #7f8c8d;
}

.book-btn {
  width: 100%;
}

.book-btn:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

/* 成功提示 */
.success-modal {
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

.success-content {
  background: white;
  border-radius: 16px;
  padding: 40px;
  text-align: center;
  max-width: 400px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.success-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.success-content h3 {
  margin: 0 0 12px 0;
  color: #2c3e50;
  font-size: 24px;
}

.success-content p {
  margin: 0 0 8px 0;
  color: #555;
  font-size: 16px;
}

.appointment-number {
  font-weight: 600;
  color: #4a90e2;
  font-size: 18px !important;
  margin: 16px 0 !important;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .department-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
  }

  .doctor-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }

  .doctor-actions {
    width: 100%;
    flex-direction: row;
    justify-content: space-between;
  }
}
</style>
