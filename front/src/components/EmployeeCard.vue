<template>
  <li class="employee-card">
    <img :src="avatar || defaultAvatar" alt="Avatar" />
    <div>
      <h4>{{ name || "Unnamed Employee" }}</h4>
      <p>Score: {{ score ?? "N/A" }}</p>
      <p>Rating: {{ rating ?? "N/A" }}</p>
    </div>
  </li>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      default: "Unnamed Employee",
    },
    score: {
      type: Number,
      default: null,
    },
    rating: {
      type: Number,
      default: null,
    },
    avatar: {
      type: String,
      default: "",
    },
  },
  computed: {
    defaultAvatar() {
      return "path/to/default-avatar.jpg"; // Укажите путь к изображению по умолчанию
    },
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
  object-fit: cover; /* Подгонка изображения для предотвращения искажений */
}

.employee-card div h4 {
  margin: 0;
  font-size: 16px;
}

.employee-card div p {
  margin: 0;
  font-size: 14px;
  color: #555;
}
</style>
