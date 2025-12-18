<template>
  <div class="id-card-input">
    <div class="page-header">
      <button class="back-btn" @click="$emit('back')">← 返回</button>
      <h2>身份证号读取</h2>
    </div>
    
    <div class="content">
      <div class="input-section">
        <div class="input-card">
          <h3>请输入身份证号码</h3>
          <div class="id-card-display">
            <span v-for="(char, index) in idCardNumber" :key="index" class="char">
              {{ char }}
            </span>
            <span v-if="idCardNumber.length < 18" class="cursor">|</span>
          </div>
          <p class="input-hint">请使用下方键盘输入身份证号码</p>
        </div>
      </div>
      
      <!-- 自定义数字键盘 -->
      <div class="keyboard-section">
        <div class="keyboard-card">
          <div class="keyboard-grid">
            <button class="key" v-for="key in keyboardKeys" :key="key" @click="handleKeyPress(key)">
              {{ key }}
            </button>
          </div>
          <div class="keyboard-actions">
            <button class="btn btn-secondary" @click="clearInput">清空</button>
            <button class="btn btn-primary" @click="confirmInput" :disabled="idCardNumber.length !== 18">
              确认
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <Footer />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Footer from './Footer.vue'

const emit = defineEmits(['back', 'idCardConfirmed'])

const idCardNumber = ref('')

// 键盘按键
const keyboardKeys = ref([
  '1', '2', '3', '4', '5', '6', '7', '8', '9',
  'X', '0', '删除'
])

// 处理按键
const handleKeyPress = (key) => {
  if (key === '删除') {
    idCardNumber.value = idCardNumber.value.slice(0, -1)
  } else {
    // 限制身份证号长度为18位
    if (idCardNumber.value.length < 18) {
      idCardNumber.value += key
    }
  }
}

// 清空输入
const clearInput = () => {
  idCardNumber.value = ''
}

// 确认输入
const confirmInput = () => {
  if (idCardNumber.value.length === 18) {
    emit('idCardConfirmed', idCardNumber.value)
  }
}
</script>

<style scoped>
.id-card-input {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f8f9fa;
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

.content {
  flex: 1;
  padding: 40px;
  overflow-y: auto;
}

.input-section {
  margin-bottom: 30px;
}

.input-card {
  background: white;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.input-card h3 {
  margin: 0 0 20px 0;
  color: #2c3e50;
  font-size: 20px;
  font-weight: 600;
  text-align: center;
}

.id-card-display {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  padding: 24px;
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  border-radius: 8px;
  font-size: 24px;
  font-weight: 500;
  margin-bottom: 16px;
  min-height: 60px;
}

.char {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  background: white;
  border-radius: 4px;
  border: 1px solid #dee2e6;
}

.cursor {
  animation: blink 1s infinite;
  color: #4a90e2;
  font-weight: bold;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

.input-hint {
  margin: 0;
  color: #6c757d;
  font-size: 14px;
  text-align: center;
}

.keyboard-section {
  margin-top: 30px;
}

.keyboard-card {
  background: white;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.keyboard-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}

.key {
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  border-radius: 8px;
  padding: 20px;
  font-size: 18px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.key:hover {
  background: #e9ecef;
  border-color: #4a90e2;
}

.key:active {
  background: #dee2e6;
}

.keyboard-actions {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.btn {
  padding: 12px 32px;
  font-size: 16px;
  font-weight: 500;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: #4a90e2;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background: #357abd;
}

.btn-primary:disabled {
  background: #cbd5e0;
  cursor: not-allowed;
}

.btn-secondary {
  background: #f8f9fa;
  color: #2c3e50;
  border: 1px solid #dee2e6;
}

.btn-secondary:hover {
  background: #e9ecef;
}
</style>