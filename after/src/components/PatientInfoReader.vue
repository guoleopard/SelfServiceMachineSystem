<template>
  <div class="patient-info-reader">
    <div class="page-header">
      <h1>👤 读取患者信息</h1>
      <p>请选择您的信息读取方式</p>
    </div>
    
    <div class="patient-methods">
      <div class="method-card" @click="handleIdCardRead">
        <div class="card-icon">🪪</div>
        <h3>身份证读取</h3>
        <p>将身份证放置在读取区域</p>
      </div>
      
      <div class="method-card" @click="handleCardRead">
        <div class="card-icon">💳</div>
        <h3>就诊卡读取</h3>
        <p>将就诊卡插入读卡器</p>
      </div>
      
      <div class="method-card" @click="handleManualInput">
        <div class="card-icon">⌨️</div>
        <h3>手动输入</h3>
        <p>手动输入您的身份信息</p>
      </div>
    </div>
    
    <div class="back-button">
      <button class="btn-back" @click="handleBack">
        ← 返回首页
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PatientInfoReader',
  methods: {
    handleIdCardRead() {
      console.log('选择身份证读取')
      this.$emit('id-card-read-selected')
    },
    
    handleCardRead() {
      console.log('选择就诊卡读取')
      this.$emit('card-read-selected')
    },
    
    handleManualInput() {
      console.log('选择手动输入')
      this.$emit('manual-input-selected')
    },
    
    handleBack() {
      console.log('返回首页')
      this.$emit('back-to-home')
    }
  }
}
</script>

<style scoped>
.patient-info-reader {
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

.patient-methods {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  max-width: 1000px;
  margin: 0 auto 3rem;
}

.method-card {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  border-radius: 16px;
  padding: 2rem;
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.method-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.card-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.method-card h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.method-card p {
  font-size: 1rem;
  opacity: 0.9;
}

.back-button {
  text-align: center;
}

.btn-back {
  background-color: #95a5a6;
  color: white;
  border: none;
  padding: 1rem 2rem;
  font-size: 1.1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-back:hover {
  background-color: #7f8c8d;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .patient-methods {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .page-header h1 {
    font-size: 2rem;
  }
}
</style>