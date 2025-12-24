<template>
  <div class="home-page">
    <!-- 医院 Logo 区域 -->
    <header class="header">
      <div class="logo">
        <div class="logo-text">医院自助机系统</div>
      </div>
    </header>

    <!-- 功能模块导航区域 -->
    <main class="main-content">
      <div class="module-grid">
        <div class="module-item" @click="navigateTo('appointment')">
          <div class="module-icon">📅</div>
          <div class="module-title">预约挂号</div>
        </div>
        <div class="module-item" @click="navigateTo('registration')">
          <div class="module-icon">🩺</div>
          <div class="module-title">就诊服务</div>
        </div>
        <div class="module-item" @click="navigateTo('payment')">
          <div class="module-icon">💳</div>
          <div class="module-title">缴费结算</div>
        </div>
        <div class="module-item" @click="navigateTo('report')">
          <div class="module-icon">📋</div>
          <div class="module-title">报告查询</div>
        </div>
        <div class="module-item" @click="navigateTo('records')">
          <div class="module-icon">📁</div>
          <div class="module-title">病历查询</div>
        </div>
        <div class="module-item" @click="navigateTo('settings')">
          <div class="module-icon">⚙️</div>
          <div class="module-title">系统设置</div>
        </div>
      </div>
    </main>

    <!-- 底部设备信息 -->
    <footer class="footer">
      <div class="device-info">
        <span>设备编号: SSM-2025-001</span>
        <span>当前时间: {{ currentTime }}</span>
        <span>在线状态: <span class="status-online">正常</span></span>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const emit = defineEmits(['navigate']);

const currentTime = ref('');

const navigateTo = (route) => {
  console.log(`导航到: ${route}`);
  // 触发父组件的导航事件
  emit('navigate', route);
};

const updateTime = () => {
  const now = new Date();
  currentTime.value = now.toLocaleString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  });
};

onMounted(() => {
  updateTime();
  const interval = setInterval(updateTime, 1000);
  onUnmounted(() => clearInterval(interval));
});
</script>

<style scoped>
.home-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #333;
}

.header {
  padding: 20px;
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.logo-text {
  font-size: 32px;
  font-weight: 700;
  color: #667eea;
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.main-content {
  flex: 1;
  padding: 40px 20px;
  overflow-y: auto;
}

.module-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  max-width: 800px;
  margin: 0 auto;
}

.module-item {
  background: rgba(255, 255, 255, 0.95);
  padding: 40px 20px;
  border-radius: 16px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.module-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
  background: #fff;
}

.module-icon {
  font-size: 60px;
  margin-bottom: 20px;
}

.module-title {
  font-size: 24px;
  font-weight: 600;
  color: #333;
}

.footer {
  padding: 15px;
  background: rgba(255, 255, 255, 0.95);
  border-top: 2px solid #e0e0e0;
}

.device-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  color: #666;
}

.status-online {
  color: #4caf50;
  font-weight: 600;
}

@media (max-width: 768px) {
  .module-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .module-item {
    padding: 30px 15px;
  }

  .module-icon {
    font-size: 50px;
  }

  .module-title {
    font-size: 20px;
  }

  .device-info {
    flex-direction: column;
    gap: 5px;
  }
}
</style>