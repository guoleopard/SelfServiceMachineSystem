<template>
  <div class="app-container">
    <!-- 首页 -->
    <HomePage v-if="currentPage === 'home'" @service-selected="handleServiceSelected" />
    
    <!-- 读取患者信息页面 -->
    <PatientInfoReader v-if="currentPage === 'patient-info-reader'" 
      @id-card-read-selected="handleIdCardReadSelected"
      @card-read-selected="handleCardReadSelected"
      @manual-input-selected="handleManualInputSelected"
      @back-to-home="handleBackToHome"
    />
    
    <!-- 身份证号读取结果页面 -->
    <IdCardResult v-if="currentPage === 'id-card-result'" 
      :id-card-number="idCardNumber"
      @add-char="addIdCardChar"
      @delete-char="deleteIdCardChar"
      @clear-all="clearIdCardNumber"
      @confirm-id-card="confirmIdCardNumber"
      @back="handleBackFromIdCardResult"
    />
    
    <!-- 患者信息确认页面 -->
    <PatientInfoConfirm v-if="currentPage === 'patient-info-confirm'" 
      :patient-info="selectedPatientInfo"
      @cancel="handleCancelPatientInfo"
      @confirm="handleConfirmPatientInfo"
    />
  </div>
</template>

<script>
import HomePage from './components/HomePage.vue'
import PatientInfoReader from './components/PatientInfoReader.vue'
import PatientInfoConfirm from './components/PatientInfoConfirm.vue'
import IdCardResult from './components/IdCardResult.vue'
import NumericKeyboard from './components/NumericKeyboard.vue'

export default {
  name: 'App',
  components: {
    HomePage,
    PatientInfoReader,
    PatientInfoConfirm,
    IdCardResult,
    NumericKeyboard
  },
  data() {
    return {
      currentPage: 'home',
      idCardNumber: '',
      selectedPatientInfo: null,
      // 模拟患者数据
      patients: [
        { id: '110101199001011234', name: '张三', gender: '男', age: 34, cardNo: '1234567890', phone: '13800138000' },
        { id: '110101199505056789', name: '李四', gender: '女', age: 29, cardNo: '0987654321', phone: '13900139000' }
      ]
    }
  },
  methods: {
    // 处理服务选择
    handleServiceSelected(serviceType) {
      console.log('选择服务:', serviceType)
      // 目前只实现了门诊挂号的患者信息读取流程
      this.currentPage = 'patient-info-reader'
    },
    
    // 处理身份证读取选择
    handleIdCardReadSelected() {
      console.log('选择身份证读取')
      this.currentPage = 'id-card-result'
      this.idCardNumber = ''
    },
    
    // 处理就诊卡读取选择
    handleCardReadSelected() {
      console.log('选择就诊卡读取')
      alert('就诊卡读取功能正在开发中...')
    },
    
    // 处理手动输入选择
    handleManualInputSelected() {
      console.log('选择手动输入')
      alert('手动输入功能正在开发中...')
    },
    
    // 返回首页
    handleBackToHome() {
      console.log('返回首页')
      this.currentPage = 'home'
    },
    
    // 从身份证结果页面返回
    handleBackFromIdCardResult() {
      console.log('从身份证结果页面返回')
      this.currentPage = 'patient-info-reader'
      this.idCardNumber = ''
    },
    
    // 添加身份证字符
    addIdCardChar(char) {
      if (this.idCardNumber.length < 18) {
        this.idCardNumber += char
      }
    },
    
    // 删除身份证字符
    deleteIdCardChar() {
      this.idCardNumber = this.idCardNumber.slice(0, -1)
    },
    
    // 清空身份证号
    clearIdCardNumber() {
      this.idCardNumber = ''
    },
    
    // 确认身份证号
    confirmIdCardNumber() {
      if (this.idCardNumber.length !== 18) {
        alert('身份证号必须为18位')
        return
      }
      
      console.log('确认身份证号:', this.idCardNumber)
      
      // 查找患者信息
      const patient = this.patients.find(p => p.id === this.idCardNumber)
      
      if (patient) {
        this.selectedPatientInfo = patient
        this.currentPage = 'patient-info-confirm'
      } else {
        alert('未找到该身份证号对应的患者信息')
      }
    },
    
    // 取消患者信息确认
    handleCancelPatientInfo() {
      console.log('取消患者信息确认')
      this.currentPage = 'id-card-result'
      this.selectedPatientInfo = null
    },
    
    // 确认患者信息
    handleConfirmPatientInfo() {
      console.log('确认患者信息')
      alert('患者信息已确认，将进入下一步流程...')
      this.currentPage = 'home'
      this.selectedPatientInfo = null
      this.idCardNumber = ''
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Microsoft YaHei', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  padding: 2rem;
}

.app-container {
  max-width: 1400px;
  margin: 0 auto;
}
</style>