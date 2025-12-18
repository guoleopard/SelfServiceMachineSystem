<template>
  <div class="patient-info-confirm">
    <div class="page-header">
      <button class="back-btn" @click="$emit('back')">← 返回</button>
      <h2>患者信息确认</h2>
    </div>
    
    <div class="content">
      <div class="info-card">
        <div class="info-header">
          <div class="avatar">👤</div>
          <div class="name-section">
            <h3 class="patient-name">{{ patientInfo.name }}</h3>
            <div class="basic-info">
              <span class="gender">{{ patientInfo.gender }}</span>
              <span class="age">{{ patientInfo.age }}岁</span>
            </div>
          </div>
        </div>
        
        <div class="info-details">
          <div class="detail-item">
            <span class="label">身份证号：</span>
            <span class="value">{{ patientInfo.idCard }}</span>
          </div>
          <div class="detail-item">
            <span class="label">医保卡：</span>
            <span class="value">{{ patientInfo.medicalCard }}</span>
          </div>
          <div class="detail-item">
            <span class="label">电子医保码：</span>
            <span class="value">{{ patientInfo.electronicCard }}</span>
          </div>
          <div class="detail-item">
            <span class="label">联系电话：</span>
            <span class="value">{{ patientInfo.phone }}</span>
          </div>
        </div>
      </div>
      
      <div class="action-buttons">
        <button class="btn btn-secondary" @click="$emit('back')">重新获取</button>
        <button class="btn btn-primary" @click="$emit('confirm', patientInfo)">确认信息</button>
      </div>
    </div>
    
    <Footer />
  </div>
</template>

<script setup>
import Footer from './Footer.vue'

defineProps({
  patientInfo: {
    type: Object,
    required: true
  }
})

defineEmits(['back', 'confirm'])
</script>

<style scoped>
.patient-info-confirm {
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
  padding: 40px;
  margin-bottom: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.info-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 1px solid #e9ecef;
}

.avatar {
  font-size: 64px;
}

.name-section {
  flex: 1;
}

.patient-name {
  margin: 0 0 8px 0;
  color: #2c3e50;
  font-size: 24px;
  font-weight: 600;
}

.basic-info {
  display: flex;
  gap: 20px;
}

.gender,
.age {
  padding: 6px 16px;
  background: #f8f9fa;
  border-radius: 20px;
  font-size: 14px;
  color: #6c757d;
}

.info-details {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.detail-item {
  display: flex;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid #f1f3f5;
}

.detail-item:last-child {
  border-bottom: none;
}

.label {
  width: 150px;
  font-size: 15px;
  font-weight: 500;
  color: #495057;
}

.value {
  flex: 1;
  font-size: 15px;
  color: #2c3e50;
  font-family: 'Courier New', monospace;
}

.action-buttons {
  display: flex;
  gap: 16px;
  justify-content: center;
  max-width: 600px;
  margin: 0 auto;
}

.action-buttons .btn {
  min-width: 160px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .content {
    padding: 20px;
  }
  
  .info-card {
    padding: 20px;
  }
  
  .info-header {
    flex-direction: column;
    text-align: center;
  }
  
  .detail-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  
  .label {
    width: auto;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .action-buttons .btn {
    width: 100%;
  }
}
</style>
