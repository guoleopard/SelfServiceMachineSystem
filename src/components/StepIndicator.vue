<script setup>
defineProps({
  currentStep: {
    type: Number,
    required: true
  }
})

const steps = [
  { id: 1, name: '选择方式' },
  { id: 2, name: '待缴列表' },
  { id: 3, name: '缴费详情' },
  { id: 4, name: '选择支付' },
  { id: 5, name: '完成' }
]
</script>

<template>
  <div class="step-indicator">
    <div 
      v-for="step in steps" 
      :key="step.id" 
      class="step-item"
      :class="{ active: currentStep >= step.id, completed: currentStep > step.id }"
    >
      <div class="step-circle">
        <span v-if="currentStep > step.id" class="checkmark">✓</span>
        <span v-else>{{ step.id }}</span>
      </div>
      <div class="step-name">{{ step.name }}</div>
      <div v-if="step.id < steps.length" class="step-line" :class="{ active: currentStep > step.id }"></div>
    </div>
  </div>
</template>

<style scoped>
.step-indicator {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px 30px;
  background-color: #34495e;
}

.step-item {
  display: flex;
  align-items: center;
  position: relative;
}

.step-circle {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background-color: #95a5a6;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 16px;
  transition: all 0.3s ease;
}

.step-item.active .step-circle {
  background-color: #3498db;
  transform: scale(1.1);
}

.step-item.completed .step-circle {
  background-color: #27ae60;
}

.checkmark {
  font-size: 18px;
}

.step-name {
  position: absolute;
  bottom: -22px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 12px;
  color: #bdc3c7;
  white-space: nowrap;
}

.step-item.active .step-name,
.step-item.completed .step-name {
  color: white;
}

.step-line {
  width: 60px;
  height: 3px;
  background-color: #95a5a6;
  margin: 0 10px;
  transition: background-color 0.3s ease;
}

.step-line.active {
  background-color: #27ae60;
}
</style>
