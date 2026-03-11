<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  seconds: {
    type: Number,
    default: 90
  }
})

const emit = defineEmits(['timeout'])

const remaining = ref(props.seconds)
let timer = null

function startCountdown() {
  remaining.value = props.seconds
  clearTimer()
  timer = setInterval(() => {
    remaining.value--
    if (remaining.value <= 0) {
      clearTimer()
      emit('timeout')
    }
  }, 1000)
}

function clearTimer() {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

function reset() {
  startCountdown()
}

onMounted(() => {
  startCountdown()
})

onUnmounted(() => {
  clearTimer()
})

defineExpose({ reset })
</script>

<template>
  <div class="countdown-timer">
    <span class="timer-text">{{ remaining }}s</span>
  </div>
</template>

<style scoped>
.countdown-timer {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: rgba(255, 0, 0, 0.1);
  border: 2px solid #e74c3c;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(231, 76, 60, 0.3);
}

.timer-text {
  color: #e74c3c;
  font-size: 16px;
  font-weight: bold;
}
</style>
