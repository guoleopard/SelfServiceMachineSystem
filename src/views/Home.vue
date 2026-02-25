<script setup>
import { ref } from 'vue'

const emit = defineEmits(['navigate'])

const modules = [
  { id: 1, name: '预约挂号', icon: '📅', path: 'appointment' },
  { id: 2, name: '缴费查询', icon: '💳', path: 'payment' },
  { id: 3, name: '报告打印', icon: '📄', path: 'report' },
  { id: 4, name: '自助缴费', icon: '💳', path: 'selfPayment' },
  { id: 5, name: '信息查询', icon: '🔍', path: 'info' },
  { id: 6, name: '满意度评价', icon: '⭐', path: 'feedback' }
]

function navigateToModule(module) {
  emit('navigate', module.path)
}
</script>

<template>
  <div class="home-container">
    <!-- 顶部医院logo -->
    <div class="header">
      <div class="logo">🏥 医院自助服务系统</div>
    </div>

    <!-- 中间功能模块导航 -->
    <div class="main-content">
      <div class="modules-grid">
        <div
          v-for="module in modules"
          :key="module.id"
          class="module-item"
          @click="navigateToModule(module)"
        >
          <div class="module-icon">{{ module.icon }}</div>
          <div class="module-name">{{ module.name }}</div>
        </div>
      </div>
    </div>

    <!-- 底部设备信息 -->
    <div class="footer">
      <div class="device-info">
        <p>设备编号: HZ-2024-001</p>
        <p>服务热线: 400-123-4567</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
}

.header {
  height: 120px;
  background-color: #2c3e50;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.logo {
  font-size: 28px;
  font-weight: bold;
  text-align: center;
}

.main-content {
  flex: 1;
  padding: 40px;
  overflow-y: auto;
}

.modules-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  max-width: 600px;
  margin: 0 auto;
}

.module-item {
  background-color: #ecf0f1;
  border-radius: 15px;
  padding: 40px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.module-item:hover {
  transform: translateY(-5px);
  background-color: #3498db;
  color: white;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

.module-icon {
  font-size: 48px;
  margin-bottom: 15px;
}

.module-name {
  font-size: 20px;
  font-weight: 600;
}

.footer {
  height: 80px;
  background-color: #2c3e50;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.device-info {
  text-align: center;
  font-size: 14px;
}

.device-info p {
  margin: 5px 0;
}
</style>