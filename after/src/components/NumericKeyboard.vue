<template>
  <div class="numeric-keyboard">
    <div class="keyboard-row">
      <button class="keyboard-btn" @click="$emit('input', '1')">1</button>
      <button class="keyboard-btn" @click="$emit('input', '2')">2</button>
      <button class="keyboard-btn" @click="$emit('input', '3')">3</button>
    </div>
    <div class="keyboard-row">
      <button class="keyboard-btn" @click="$emit('input', '4')">4</button>
      <button class="keyboard-btn" @click="$emit('input', '5')">5</button>
      <button class="keyboard-btn" @click="$emit('input', '6')">6</button>
    </div>
    <div class="keyboard-row">
      <button class="keyboard-btn" @click="$emit('input', '7')">7</button>
      <button class="keyboard-btn" @click="$emit('input', '8')">8</button>
      <button class="keyboard-btn" @click="$emit('input', '9')">9</button>
    </div>
    <div class="keyboard-row">
      <button class="keyboard-btn" v-if="allowX" @click="$emit('input', 'X')">X</button>
      <div class="keyboard-empty" v-else></div>
      <button class="keyboard-btn" @click="$emit('input', '0')">0</button>
      <button class="keyboard-btn keyboard-backspace" @click="$emit('backspace')">删除</button>
    </div>
    <div class="keyboard-row" v-if="showActionButtons">
      <button class="keyboard-btn keyboard-clear" @click="$emit('clear')">清空</button>
      <button class="keyboard-btn keyboard-confirm" @click="$emit('confirm')">确认</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NumericKeyboard',
  props: {
    allowX: {
      type: Boolean,
      default: false
    },
    showActionButtons: {
      type: Boolean,
      default: true
    }
  }
}
</script>

<style scoped>
.numeric-keyboard {
  background-color: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  max-width: 350px;
  margin: 0 auto;
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

.keyboard-empty {
  flex: 1;
  max-width: 80px;
  min-width: 60px;
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
</style>