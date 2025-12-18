<template>
  <div class="patient-info-confirm">
    <div class="page-header">
      <h1>✅ 患者信息确认</h1>
      <p>请确认您的个人信息</p>
    </div>
    
    <div class="info-card">
      <div class="info-item">
        <label>姓名：</label>
        <span>{{ patientInfo.name }}</span>
      </div>
      
      <div class="info-item">
        <label>性别：</label>
        <span>{{ patientInfo.gender }}</span>
      </div>
      
      <div class="info-item">
        <label>年龄：</label>
        <span>{{ patientInfo.age }}岁</span>
      </div>
      
      <div class="info-item">
        <label>身份证号：</label>
        <span>{{ patientInfo.id }}</span>
      </div>
      
      <div class="info-item">
        <label>就诊卡号：</label>
        <span>{{ patientInfo.cardNo }}</span>
      </div>
      
      <div class="info-item">
        <label>联系电话：</label>
        <span>{{ patientInfo.phone }}</span>
      </div>
    </div>
    
    <div class="confirm-buttons">
      <button class="btn-cancel" @click="handleCancel">
        取消
      </button>
      <button class="btn-confirm" @click="handleConfirm">
        确认信息
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PatientInfoConfirm',
  props: {
    patientInfo: {
      type: Object,
      required: true
    }
  },
  methods: {
    handleCancel() {
      console.log('取消确认')
      this.$emit('cancel')
    },
    
    handleConfirm() {
      console.log('确认患者信息')
      this.$emit('confirm')
    }
  }
}
</script>

<style scoped>
.patient-info-confirm {
  padding: 2rem;
}

.page-header {
  text-align: center;
  margin-bottom: 3rem;
}

.page-header h1 {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.page-header p {
  font-size: 1.2rem;
  color: #7f8c8d;
}

.info-card {
  background-color: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  max-width: 600px;
  margin: 0 auto 3rem;
}

.info-item {
  display: flex;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #eee;
}

.info-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.info-item label {
  font-weight: bold;
  color: #2c3e50;
  min-width: 120px;
  font-size: 1.1rem;
}

.info-item span {
  color: #333;
  font-size: 1.1rem;
}

.confirm-buttons {
  display: flex;
  justify-content: center;
  gap: 2rem;
}

.btn-cancel,
.btn-confirm {
  padding: 1rem 2.5rem;
  font-size: 1.1rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-cancel {
  background-color: #e74c3c;
  color: white;
}

.btn-cancel:hover {
  background-color: #c0392b;
  transform: translateY(-2px);
}

.btn-confirm {
  background-color: #27ae60;
  color: white;
}

.btn-confirm:hover {
  background-color: #219a52;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .info-item {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .info-item label {
    margin-bottom: 0.5rem;
  }
  
  .confirm-buttons {
    flex-direction: column;
    gap: 1rem;
  }
}
</style>