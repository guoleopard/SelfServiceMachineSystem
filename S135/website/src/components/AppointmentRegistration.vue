<template>
  <div class="appointment-page">
    <header class="page-header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <h1>预约挂号</h1>
    </header>

    <main class="page-content">
      <!-- 科室选择 -->
      <section class="section">
        <h2 class="section-title">选择科室</h2>
        <div class="department-grid">
          <div 
            class="department-item" 
            v-for="department in departments" 
            :key="department.id"
            :class="{ active: selectedDepartment === department.id }"
            @click="selectDepartment(department.id)"
          >
            {{ department.name }}
          </div>
        </div>
      </section>

      <!-- 医生列表 -->
      <section class="section" v-if="selectedDepartment">
        <h2 class="section-title">选择医生</h2>
        <div class="doctor-list">
          <div 
            class="doctor-item" 
            v-for="doctor in filteredDoctors" 
            :key="doctor.id"
            :class="{ active: selectedDoctor === doctor.id }"
            @click="selectDoctor(doctor.id)"
          >
            <div class="doctor-info">
              <div class="doctor-avatar">{{ doctor.name.charAt(0) }}</div>
              <div class="doctor-details">
                <div class="doctor-name">{{ doctor.name }}</div>
                <div class="doctor-title">{{ doctor.title }}</div>
                <div class="doctor-department">{{ doctor.department }}</div>
              </div>
            </div>
            <div class="doctor-status">
              <span class="status-available">{{ doctor.status }}</span>
            </div>
          </div>
        </div>
      </section>

      <!-- 预约时间选择 -->
      <section class="section" v-if="selectedDoctor">
        <h2 class="section-title">选择时间</h2>
        <div class="time-grid">
          <div 
            class="time-item" 
            v-for="timeSlot in timeSlots" 
            :key="timeSlot.id"
            :class="{ available: timeSlot.available, selected: selectedTime === timeSlot.id }"
            @click="selectTime(timeSlot.id)"
          >
            {{ timeSlot.time }}
          </div>
        </div>
      </section>

      <!-- 患者信息 -->
      <section class="section" v-if="selectedTime">
        <h2 class="section-title">患者信息</h2>
        <div class="form-group">
          <label for="patientName">姓名</label>
          <input 
            type="text" 
            id="patientName" 
            v-model="patientInfo.name"
            placeholder="请输入患者姓名"
          />
        </div>
        <div class="form-group">
          <label for="patientId">身份证号</label>
          <input 
            type="text" 
            id="patientId" 
            v-model="patientInfo.id"
            placeholder="请输入身份证号"
          />
        </div>
        <div class="form-group">
          <label for="patientPhone">手机号码</label>
          <input 
            type="tel" 
            id="patientPhone" 
            v-model="patientInfo.phone"
            placeholder="请输入手机号码"
          />
        </div>
      </section>

      <!-- 预约确认 -->
      <section class="section" v-if="selectedTime">
        <div class="appointment-summary">
          <h3>预约信息</h3>
          <div class="summary-item">
            <span class="label">科室:</span>
            <span class="value">{{ selectedDepartmentName }}</span>
          </div>
          <div class="summary-item">
            <span class="label">医生:</span>
            <span class="value">{{ selectedDoctorName }}</span>
          </div>
          <div class="summary-item">
            <span class="label">时间:</span>
            <span class="value">{{ selectedTimeSlot }}</span>
          </div>
        </div>
      </section>

      <!-- 提交按钮 -->
      <div class="action-buttons">
        <button class="btn-primary" @click="submitAppointment" :disabled="!canSubmit">
          确认预约
        </button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const emit = defineEmits(['back']);

const selectedDepartment = ref(null);
const selectedDoctor = ref(null);
const selectedTime = ref(null);

const patientInfo = ref({
  name: '',
  id: '',
  phone: ''
});

const departments = ref([
  { id: 1, name: '内科' },
  { id: 2, name: '外科' },
  { id: 3, name: '妇产科' },
  { id: 4, name: '儿科' },
  { id: 5, name: '眼科' },
  { id: 6, name: '耳鼻喉科' },
  { id: 7, name: '口腔科' },
  { id: 8, name: '皮肤科' }
]);

const doctors = ref([
  { id: 101, name: '张医生', title: '主任医师', department: '内科', status: '可预约' },
  { id: 102, name: '李医生', title: '副主任医师', department: '内科', status: '可预约' },
  { id: 103, name: '王医生', title: '主治医师', department: '外科', status: '可预约' },
  { id: 104, name: '赵医生', title: '主任医师', department: '外科', status: '已满' },
  { id: 105, name: '刘医生', title: '副主任医师', department: '妇产科', status: '可预约' },
  { id: 106, name: '陈医生', title: '主治医师', department: '儿科', status: '可预约' },
  { id: 107, name: '孙医生', title: '主任医师', department: '眼科', status: '可预约' },
  { id: 108, name: '周医生', title: '副主任医师', department: '耳鼻喉科', status: '可预约' },
  { id: 109, name: '吴医生', title: '主治医师', department: '口腔科', status: '可预约' },
  { id: 110, name: '郑医生', title: '主任医师', department: '皮肤科', status: '可预约' }
]);

const timeSlots = ref([
  { id: 201, time: '08:00-08:30', available: true },
  { id: 202, time: '08:30-09:00', available: true },
  { id: 203, time: '09:00-09:30', available: false },
  { id: 204, time: '09:30-10:00', available: true },
  { id: 205, time: '10:00-10:30', available: true },
  { id: 206, time: '10:30-11:00', available: false },
  { id: 207, time: '11:00-11:30', available: true },
  { id: 208, time: '14:00-14:30', available: true },
  { id: 209, time: '14:30-15:00', available: true },
  { id: 210, time: '15:00-15:30', available: true }
]);

const filteredDoctors = computed(() => {
  if (!selectedDepartment.value) return [];
  const department = departments.value.find(d => d.id === selectedDepartment.value);
  return doctors.value.filter(d => d.department === department?.name);
});

const selectedDepartmentName = computed(() => {
  if (!selectedDepartment.value) return '';
  const department = departments.value.find(d => d.id === selectedDepartment.value);
  return department?.name || '';
});

const selectedDoctorName = computed(() => {
  if (!selectedDoctor.value) return '';
  const doctor = doctors.value.find(d => d.id === selectedDoctor.value);
  return doctor?.name || '';
});

const selectedTimeSlot = computed(() => {
  if (!selectedTime.value) return '';
  const timeSlot = timeSlots.value.find(t => t.id === selectedTime.value);
  return timeSlot?.time || '';
});

const canSubmit = computed(() => {
  return selectedDepartment.value && selectedDoctor.value && selectedTime.value &&
         patientInfo.value.name && patientInfo.value.id && patientInfo.value.phone;
});

const selectDepartment = (departmentId) => {
  selectedDepartment.value = departmentId;
  selectedDoctor.value = null;
  selectedTime.value = null;
};

const selectDoctor = (doctorId) => {
  selectedDoctor.value = doctorId;
  selectedTime.value = null;
};

const selectTime = (timeId) => {
  const timeSlot = timeSlots.value.find(t => t.id === timeId);
  if (timeSlot && timeSlot.available) {
    selectedTime.value = timeId;
  }
};

const goBack = () => {
  console.log('返回首页');
  // 触发父组件的返回事件
  emit('back');
};

const submitAppointment = () => {
  if (!canSubmit.value) return;
  
  console.log('提交预约信息:', {
    department: selectedDepartmentName.value,
    doctor: selectedDoctorName.value,
    time: selectedTimeSlot.value,
    patient: patientInfo.value
  });
  
  // 这里可以添加预约提交逻辑
  alert('预约成功！请携带身份证按时就诊。');
  
  // 重置表单
  selectedDepartment.value = null;
  selectedDoctor.value = null;
  selectedTime.value = null;
  patientInfo.value = { name: '', id: '', phone: '' };
};
</script>

<style scoped>
.appointment-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #333;
}

.page-header {
  padding: 20px;
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 20px;
}

.back-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #667eea;
  font-weight: 600;
}

.page-header h1 {
  font-size: 28px;
  font-weight: 700;
  color: #333;
  margin: 0;
}

.page-content {
  flex: 1;
  padding: 30px 20px;
  overflow-y: auto;
}

.section {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 16px;
  padding: 25px;
  margin-bottom: 30px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 22px;
  font-weight: 600;
  color: #333;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #667eea;
}

.department-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
}

.department-item {
  padding: 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 18px;
  font-weight: 500;
}

.department-item:hover {
  border-color: #667eea;
  background: #f5f5f5;
}

.department-item.active {
  border-color: #667eea;
  background: #667eea;
  color: #fff;
}

.doctor-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.doctor-item {
  display: flex;
  align-items: center;
  padding: 20px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  gap: 20px;
}

.doctor-item:hover {
  border-color: #667eea;
  background: #f5f5f5;
}

.doctor-item.active {
  border-color: #667eea;
  background: #667eea;
  color: #fff;
}

.doctor-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: 700;
}

.doctor-details {
  flex: 1;
}

.doctor-name {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 5px;
}

.doctor-title {
  font-size: 14px;
  color: #666;
  margin-bottom: 3px;
}

.doctor-department {
  font-size: 12px;
  color: #999;
}

.doctor-status {
  font-size: 14px;
  font-weight: 600;
}

.status-available {
  color: #4caf50;
}

.time-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}

.time-item {
  padding: 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 16px;
  font-weight: 500;
}

.time-item.available:hover {
  border-color: #667eea;
  background: #f5f5f5;
}

.time-item.available.selected {
  border-color: #667eea;
  background: #667eea;
  color: #fff;
}

.time-item:not(.available) {
  opacity: 0.5;
  cursor: not-allowed;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 8px;
  color: #333;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 16px;
  transition: all 0.3s ease;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.appointment-summary {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.appointment-summary h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 15px;
  color: #333;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  font-size: 16px;
}

.summary-item .label {
  font-weight: 500;
  color: #666;
}

.summary-item .value {
  font-weight: 600;
  color: #333;
}

.action-buttons {
  margin-top: 30px;
  text-align: center;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  border: none;
  padding: 15px 40px;
  font-size: 20px;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
  max-width: 300px;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .department-grid {
    grid-template-columns: 1fr;
  }

  .time-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>