<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

const props = defineProps({
  duration: {
    type: Number,
    default: 90
  },
  autoStart: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['timeout', 'tick'])

const countdown = ref(props.duration)
let timer = null

function start() {
  countdown.value = props.duration
  stop()
  timer = setInterval(() => {
    countdown.value--
    emit('tick', countdown.value)
    if (countdown.value <= 0) {
      stop()
      emit('timeout')
    }
  }, 1000)
}

function stop() {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

function reset() {
  stop()
  countdown.value = props.duration
}

watch(() => props.duration, (newVal) => {
  countdown.value = newVal
  if (props.autoStart) {
    start()
  }
})

onMounted(() => {
  if (props.autoStart) {
    start()
  }
})

onUnmounted(() => {
  stop()
})

defineExpose({ start, stop, reset, countdown })
</script>

<template>
  <div class="countdown-timer">
    <span class="time">{{ countdown }}</span>
    <span class="unit">s</span>
  </div>
</template>

<style scoped>
.countdown-timer {
  display: flex;
  align-items: center;
  background-color: #e74c3c;
  padding: 5px 15px;
  border-radius: 5px;
  color: white;
  font-weight: bold;
}

.time {
  font-size: 20px;
}

.unit {
  font-size: 16px;
  margin-left: 2px;
}
</style>
