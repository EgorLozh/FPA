<template>
  <div class="employee-card">
    <img :src="avatar" :alt="name" />
    <div>
      <h3>{{ name }}</h3>
      <p>Compliance Score: {{ score }}</p>
      <p>{{ rating }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  score: String,
  rating: String,
  avatar: String,
});
</script>

<style scoped>
.employee-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fff;
  margin-bottom: 10px;
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.employee-info h3 {
  margin: 0;
  font-size: 1.1em;
}

.employee-info p {
  margin: 5px 0 0;
  font-size: 0.9em;
  color: #666;
}

.rating {
  font-weight: bold;
}
</style>
