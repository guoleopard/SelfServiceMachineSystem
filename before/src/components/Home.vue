<template>
  <div class="home-page">
    <Header />
    <div class="main-content">
      <div class="function-grid">
        <div class="function-item" @click="$emit('goToPage', 'patientInfoReader')">
          <div class="icon">📅</div>
          <div class="label">预约挂号</div>
        </div>
        <div class="function-item" @click="showMessage('该功能暂未开放')">
          <div class="icon">🏥</div>
          <div class="label">当日挂号</div>
        </div>
        <div class="function-item" @click="showMessage('该功能暂未开放')">
          <div class="icon">📋</div>
          <div class="label">报告打印</div>
        </div>
        <div class="function-item" @click="showMessage('该功能暂未开放')">
          <div class="icon">💊</div>
          <div class="label">药品查询</div>
        </div>
        <div class="function-item" @click="showMessage('该功能暂未开放')">
          <div class="icon">💳</div>
          <div class="label">缴费服务</div>
        </div>
        <div class="function-item" @click="showMessage('该功能暂未开放')">
          <div class="icon">ℹ️</div>
          <div class="label">医院信息</div>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import Header from './Header.vue'
import Footer from './Footer.vue'

const emit = defineEmits(['goToPage'])

const showMessage = (message) => {
  alert(message)
}
</script>

<style scoped>
.home-page {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 40px 60px;
  overflow-y: auto;
}

.function-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  max-width: 900px;
  margin: 0 auto;
}

.function-item {
  background: white;
  border-radius: 16px;
  padding: 40px 20px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  border: 1px solid #e9ecef;
}

.function-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  border-color: #4a90e2;
}

.function-item .icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.function-item .label {
  font-size: 18px;
  font-weight: 500;
  color: #2c3e50;
}
</style>