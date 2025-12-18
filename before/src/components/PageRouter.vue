<template>
  <div class="page-router">
    <!-- 患者信息读取页面 -->
    <div v-if="currentPage === 'patientInfoReader'" class="patient-info-reader-page">
      <PatientInfoReader 
        @back="$emit('back')"
        @patientInfoFetched="$emit('patientInfoFetched', $event)"
        @goToIDCardInput="$emit('goToPage', 'idCardInput')"
      />
    </div>

    <!-- 患者信息确认页面 -->
    <div v-else-if="currentPage === 'patientInfoConfirm'" class="patient-info-confirm-page">
      <PatientInfoConfirm 
        :patientInfo="patientInfo"
        @back="$emit('back')"
        @confirm="$emit('patientInfoConfirmed', $event)"
      />
    </div>

    <!-- 身份证号输入页面 -->
    <div v-else-if="currentPage === 'idCardInput'" class="id-card-input-page">
      <IDCardInput 
        @back="$emit('back')"
        @idCardConfirmed="$emit('idCardConfirmed', $event)"
      />
    </div>

    <!-- 预约挂号页面 -->
    <div v-else-if="currentPage === 'registration'" class="registration-page">
      <div class="page-header">
        <button class="back-btn" @click="$emit('back')">← 返回</button>
        <h2>预约挂号</h2>
        <div class="patient-name-tag">{{ patientInfo?.name }}</div>
      </div>
      <div class="registration-content">
        <Registration />
      </div>
      <Footer />
    </div>
  </div>
</template>

<script setup>
import PatientInfoReader from './PatientInfoReader.vue'
import PatientInfoConfirm from './PatientInfoConfirm.vue'
import IDCardInput from './IDCardInput.vue'
import Registration from './Registration.vue'
import Footer from './Footer.vue'

defineProps({
  currentPage: {
    type: String,
    required: true
  },
  patientInfo: {
    type: Object,
    default: null
  }
})

defineEmits(['back', 'goToPage', 'patientInfoFetched', 'patientInfoConfirmed', 'idCardConfirmed'])
</script>

<style scoped>
.page-router {
  width: 100%;
  height: 100vh;
}

/* 预约挂号页面样式 */
.registration-page {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
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

.patient-name-tag {
  margin-left: auto;
  background: #e3f2fd;
  color: #1976d2;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
}

.registration-content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
</style>