<template>
  <div class="app-container">
    <!-- 首页 -->
    <div v-if="currentPage === 'home'" class="home-page">
      <Header />
      <div class="main-content">
        <div class="function-grid">
          <div class="function-item" @click="goToPage('patientInfoReader')">
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

    <!-- 患者信息读取页面 -->
    <div v-else-if="currentPage === 'patientInfoReader'" class="patient-info-reader-page">
      <PatientInfoReader 
        @back="goToPage('home')"
        @patientInfoFetched="onPatientInfoFetched"
      />
    </div>

    <!-- 患者信息确认页面 -->
    <div v-else-if="currentPage === 'patientInfoConfirm'" class="patient-info-confirm-page">
      <PatientInfoConfirm 
        :patientInfo="currentPatientInfo"
        @back="goToPage('patientInfoReader')"
        @confirm="onPatientInfoConfirmed"
      />
    </div>

    <!-- 预约挂号页面 -->
    <div v-else-if="currentPage === 'registration'" class="registration-page">
      <div class="page-header">
        <button class="back-btn" @click="goToPage('patientInfoConfirm')">← 返回</button>
        <h2>预约挂号</h2>
        <div class="patient-name-tag">{{ currentPatientInfo?.name }}</div>
      </div>
      <div class="registration-content">
        <Registration />
      </div>
      <Footer />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import Registration from './components/Registration.vue'
import PatientInfoReader from './components/PatientInfoReader.vue'
import PatientInfoConfirm from './components/PatientInfoConfirm.vue'

const currentPage = ref('home')
const currentPatientInfo = ref(null)

const goToPage = (page) => {
  currentPage.value = page
}

const showMessage = (message) => {
  alert(message)
}

// 处理患者信息获取
const onPatientInfoFetched = (patientInfo) => {
  currentPatientInfo.value = patientInfo
  currentPage.value = 'patientInfoConfirm'
}

// 处理患者信息确认
const onPatientInfoConfirmed = (patientInfo) => {
  currentPatientInfo.value = patientInfo
  currentPage.value = 'registration'
}
</script>

<style scoped>
.app-container {
  width: 100%;
  height: 100vh;
  background-color: #f8f9fa;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

/* 首页样式 */
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

.registration-content {
  flex: 1;
  padding: 30px;
  overflow-y: auto;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .function-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    padding: 0 20px;
  }

  .main-content {
    padding: 20px;
  }
}

.patient-name-tag {
  font-size: 16px;
  color: #4a90e2;
  font-weight: 500;
  margin-left: auto;
  padding: 8px 16px;
  background: #e3f2fd;
  border-radius: 20px;
}
</style>
