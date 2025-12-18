<template>
  <div class="app-container">
    <!-- 首页 -->
    <div v-if="currentPage === 'home'" class="home-page">
      <Home @goToPage="goToPage" />
    </div>

    <!-- 其他功能页面 -->
    <div v-else class="other-pages">
      <PageRouter 
        :currentPage="currentPage"
        :patientInfo="currentPatientInfo"
        @back="handleBack"
        @goToPage="goToPage"
        @patientInfoFetched="onPatientInfoFetched"
        @patientInfoConfirmed="onPatientInfoConfirmed"
        @idCardConfirmed="onIDCardConfirmed"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Home from './components/Home.vue'
import PageRouter from './components/PageRouter.vue'

const currentPage = ref('home')
const currentPatientInfo = ref(null)

const goToPage = (page) => {
  currentPage.value = page
}

// 处理返回按钮
const handleBack = () => {
  // 根据当前页面返回上一级
  const backMap = {
    'patientInfoReader': 'home',
    'patientInfoConfirm': 'patientInfoReader',
    'idCardInput': 'patientInfoReader',
    'registration': 'patientInfoConfirm'
  }
  currentPage.value = backMap[currentPage.value] || 'home'
}

// 处理患者信息获取
const onPatientInfoFetched = (patientInfo) => {
  currentPatientInfo.value = patientInfo
  currentPage.value = 'patientInfoConfirm'
}

// 处理身份证号确认
const onIDCardConfirmed = (idCardNumber) => {
  // 模拟根据身份证号查找患者
  const mockPatients = [
    { id: '1', name: '张三', idCard: '110101199001011234', medicalCard: 'MC123456789', electronicCard: 'EC987654321', gender: '男', age: 34, phone: '13800138000' },
    { id: '2', name: '李四', idCard: '110101198505056789', medicalCard: 'MC987654321', electronicCard: 'EC123456789', gender: '女', age: 39, phone: '13900139000' }
  ]
  
  let patient = null
  for (let p of mockPatients) {
    if (p.idCard === idCardNumber) {
      patient = p
      break
    }
  }
  
  if (patient) {
    currentPatientInfo.value = patient
    currentPage.value = 'patientInfoConfirm'
  } else {
    alert('未找到患者信息，请检查身份证号是否正确')
  }
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

.home-page {
  width: 100%;
  height: 100%;
}

.other-pages {
  width: 100%;
  height: 100%;
}
</style>