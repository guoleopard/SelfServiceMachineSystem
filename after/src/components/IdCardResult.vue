<template>
  <div class="id-card-result">
    <div class="page-header">
      <h1>🪪 身份证号读取</h1>
      <p>请确认或输入您的身份证号</p>
    </div>
    
    <div class="input-section">
      <div class="input-label">身份证号：</div>
      <div class="input-box">
        {{ idCardNumber || '请输入身份证号' }}
      </div>
    </div>
    
    <!-- 自定义数字键盘 -->
    <div class="id-card-keyboard">
      <div class="keyboard-row">
        <button class="keyboard-btn" @click="$emit('add-char', '1')">1</button>
        <button class="keyboard-btn" @click="$emit('add-char', '2')">2</button>
        <button class="keyboard-btn" @click="$emit('add-char', '3')">3</button>
      </div>
      <div class="keyboard-row">
        <button class="keyboard-btn" @click="$emit('add-char', '4')">4</button>
        <button class="keyboard-btn" @click="$emit('add-char', '5')">5</button>
        <button class="keyboard-btn" @click="$emit('add-char', '6')">6</button>
      </div>
      <div class="keyboard-row">
        <button class="keyboard-btn" @click="$emit('add-char', '7')">7</button>
        <button class="keyboard-btn" @click="$emit('add-char', '8')">8</button>
        <button class="keyboard-btn" @click="$emit('add-char', '9')">9</button>
      </div>
      <div class="keyboard-row">
        <button class="keyboard-btn keyboard-x" @click="$emit('add-char', 'X')">X</button>
        <button class="keyboard-btn" @click="$emit('add-char', '0')">0</button>
        <button class="keyboard-btn keyboard-backspace" @click="$emit('delete-char')">删除</button>
      </div>
      <div class="keyboard-row">
        <button class="keyboard-btn keyboard-clear" @click="$emit('clear-all')">清空</button>
        <button class="keyboard-btn keyboard-confirm" @click="$emit('confirm-id-card')">确认</button>
      </div>
    </div>
    
    <div class="back-button">
      <button class="btn-back" @click="$emit('back')">
        ← 返回上一页
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IdCardResult',
  props: {
    idCardNumber: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>
.id-card-result {
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

.input-section {
  text-align: center;
  margin-bottom: 3rem;
}

.input-label {
  font-size: 1.2rem;
  color: #2c3e50;
  margin-bottom: 1rem;
  font-weight: bold;
}

.input-box {
  background-color: white;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  font-size: 1.4rem;
  color: #333;
  max-width: 500px;
  margin: 0 auto;
  font-family: 'Courier New', monospace;
  letter-spacing: 0.1rem;
}

/* 身份证号输入键盘样式 */
.id-card-keyboard {
  background-color: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  max-width: 350px;
  margin: 0 auto 3rem;
}

.keyboard-row {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.keyboard-btn {
  flex: 1;
  max-width: 80px;
  min-width: 60px;
  padding: 1.8rem 1rem;
  border: none;
  border-radius: 12px;
  font-size: 1.4rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: #f8f9fa;
  color: #333;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.keyboard-btn:hover {
  background-color: #3498db;
  color: white;
  transform: translateY(-2px);
}

.keyboard-x {
  background-color: #e74c3c;
  color: white;
}

.keyboard-x:hover {
  background-color: #c0392b;
}

.keyboard-backspace,
.keyboard-clear {
  background-color: #f39c12;
  color: white;
}

.keyboard-backspace:hover,
.keyboard-clear:hover {
  background-color: #e67e22;
}

.keyboard-confirm {
  background-color: #27ae60;
  color: white;
}

.keyboard-confirm:hover {
  background-color: #219a52;
}

.back-button {
  text-align: center;
}

.btn-back {
  background-color: #95a5a6;
  color: white;
  border: none;
  padding: 1rem 2rem;
  font-size: 1.1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-back:hover {
  background-color: #7f8c8d;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .page-header h1 {
    font-size: 2rem;
  }
}
</style>