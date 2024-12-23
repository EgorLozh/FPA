<template>
  <li class="employee-card">
    <img :src="avatar" alt="Avatar" />
    <div>
      <h4>{{ name }}</h4>
      <p>Score: {{ score }}</p>
      <p>Rating: {{ rating }}</p>
    </div>
  </li>
</template>

<script>
export default {
  props: {
    name: String,
    score: String,
    rating: String,
    avatar: String,
  },
};
</script>

<style>
.employee-card {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.employee-card img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}
</style>
