<template>
  <header class="header">
    <div class="logo-section">
      <div class="logo-placeholder">
        <span class="logo-text">🏥 医院自助服务系统</span>
      </div>
    </div>
    <div class="header-title">
      <h1>欢迎使用医院自助服务机</h1>
    </div>
  </header>
</template>

<script setup>
</script>

<style scoped>
.header {
  background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
  color: white;
  padding: 30px 40px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.logo-section {
  margin-bottom: 20px;
}

.logo-placeholder {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 20px;
  display: inline-block;
  backdrop-filter: blur(10px);
}

.logo-text {
  font-size: 28px;
  font-weight: 700;
  color: white;
}

.header-title h1 {
  margin: 0;
  font-size: 24px;
  font-weight: 500;
  opacity: 0.95;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .header {
    padding: 20px 15px;
  }

  .logo-text {
    font-size: 22px;
  }

  .header-title h1 {
    font-size: 18px;
  }
}
</style>
