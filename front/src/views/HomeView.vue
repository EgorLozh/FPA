<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const navigateTo = (path) => {
  router.push(path)
}
</script>

<template>
  <main>
    <!-- Приветственное окошко -->
    <div class="welcome-box">
      <h1>Добро пожаловать!</h1>
      <p>Вы можете перейти на другие страницы, используя кнопки ниже.</p>
      <button @click="navigateTo('/dashboard')">Dashboard</button>
      <button @click="navigateTo('/employee-rating')">Employee Rating</button>
    </div>
  </main>
</template>

<style scoped>
.welcome-box {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 20px;
  text-align: center;
}
.welcome-box h1 {
  margin-bottom: 10px;
}
.welcome-box button {
  margin: 5px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}
.welcome-box button:hover {
  background-color: #0056b3;
}
</style>
