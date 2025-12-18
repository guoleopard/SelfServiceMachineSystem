<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="device-info">
        <span class="label">设备编号：</span>
        <span class="value">SSM-2024-001</span>
      </div>
      <div class="device-status">
        <span class="status-indicator online"></span>
        <span>在线服务</span>
      </div>
      <div class="service-hours">
        <span>服务时间：07:00-21:00</span>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
  background-color: #2c3e50;
  color: white;
  padding: 20px 40px;
  box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.1);
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 15px;
}

.device-info,
.device-status,
.service-hours {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
}

.device-info .label {
  color: #bdc3c7;
}

.device-info .value {
  color: #4a90e2;
  font-weight: 500;
}

.status-indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  display: inline-block;
}

.status-indicator.online {
  background-color: #50c878;
  box-shadow: 0 0 8px rgba(80, 200, 120, 0.6);
}

.service-hours {
  color: #95a5a6;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .footer {
    padding: 15px 20px;
  }

  .footer-content {
    flex-direction: column;
    text-align: center;
    gap: 10px;
  }

  .device-info,
  .device-status,
  .service-hours {
    font-size: 12px;
  }
}
</style>
