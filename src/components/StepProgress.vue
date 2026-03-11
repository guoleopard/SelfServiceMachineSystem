<script setup>
defineProps({
  currentStep: {
    type: Number,
    required: true
  },
  steps: {
    type: Array,
    default: () => ['选择验证方式', '选择缴费项目', '确认缴费详情', '选择支付方式', '完成缴费']
  }
})
</script>

<template>
  <div class="step-progress">
    <div class="steps-container">
      <div 
        v-for="(step, index) in steps" 
        :key="index"
        class="step-item"
        :class="{ 
          active: index + 1 === currentStep,
          completed: index + 1 < currentStep
        }"
      >
        <div class="step-circle">
          <span v-if="index + 1 < currentStep" class="check-mark">✓</span>
          <span v-else>{{ index + 1 }}</span>
        </div>
        <span class="step-label">{{ step }}</span>
        <div v-if="index < steps.length - 1" class="step-line"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.step-progress {
  background: white;
  padding: 20px 40px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.steps-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1000px;
  margin: 0 auto;
  position: relative;
}

.step-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  flex: 1;
}

.step-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #e0e0e0;
  color: #999;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 16px;
  margin-bottom: 8px;
  transition: all 0.3s;
  z-index: 1;
}

.step-item.active .step-circle {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  transform: scale(1.1);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.step-item.completed .step-circle {
  background: #4CAF50;
  color: white;
}

.check-mark {
  font-size: 18px;
}

.step-label {
  font-size: 12px;
  color: #999;
  text-align: center;
  white-space: nowrap;
}

.step-item.active .step-label {
  color: #667eea;
  font-weight: 600;
}

.step-item.completed .step-label {
  color: #4CAF50;
}

.step-line {
  position: absolute;
  top: 20px;
  left: 50%;
  width: 100%;
  height: 3px;
  background: #e0e0e0;
  z-index: 0;
}

.step-item.completed .step-line {
  background: #4CAF50;
}
</style>
