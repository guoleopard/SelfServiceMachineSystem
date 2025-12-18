<template>
  <div class="home-page">
    <div class="page-header">
      <h1>🏥 医院自助服务系统</h1>
      <p>请选择您需要的服务</p>
    </div>
    
    <div class="function-grid">
      <div class="function-card" @click="handleService('register')">
        <div class="card-icon">📝</div>
        <h3>门诊挂号</h3>
        <p>为新老患者提供便捷的门诊挂号服务</p>
      </div>
      
      <div class="function-card" @click="handleService('payment')">
        <div class="card-icon">💳</div>
        <h3>费用支付</h3>
        <p>快速完成各项医疗费用的自助支付</p>
      </div>
      
      <div class="function-card" @click="handleService('report')">
        <div class="card-icon">📄</div>
        <h3>报告打印</h3>
        <p>方便快捷地打印各种检验检查报告</p>
      </div>
      
      <div class="function-card" @click="handleService('info')">
        <div class="card-icon">👤</div>
        <h3>信息查询</h3>
        <p>查询您的就诊记录、费用明细等信息</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    handleService(serviceType) {
      console.log('选择服务:', serviceType)
      // 触发父组件的服务选择事件
      this.$emit('service-selected', serviceType)
    }
  }
}
</script>

<style scoped>
.home-page {
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

.function-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.function-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  padding: 2rem;
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.function-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.card-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.function-card h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.function-card p {
  font-size: 1rem;
  opacity: 0.9;
}

@media (max-width: 768px) {
  .function-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .page-header h1 {
    font-size: 2rem;
  }
}
</style>