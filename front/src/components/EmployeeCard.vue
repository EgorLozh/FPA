<template>
  <li class="employee-card" @click="goToEmployeePage">
    <img :src="avatar || defaultAvatar" :alt="`Avatar of ${name || 'Unnamed Employee'}`" />
    <div class="employee-details">
      <h4>{{ name || "Unnamed Employee" }}</h4>
      <div class="employee-stats">
        <p>Score: {{ score ?? "N/A" }}</p>
        <p>Rating: {{ rating ?? "N/A" }}</p>
        <p v-if="storeName">Store: {{ storeName }}</p>
      </div>
    </div>
  </li>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      required: true
    },
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
    storeName: {
      type: String,
      default: "",
    },
  },
  computed: {
    defaultAvatar() {
      return "path/to/default-avatar.jpg"; // Укажите путь к изображению по умолчанию
    },
  },
  methods: {
    goToEmployeePage() {
      this.$router.push({ name: 'Employee', params: { id: this.id } });
    }
  }
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
  transition: transform 0.3s, box-shadow 0.3s;
}

.employee-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.employee-card img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover; /* Подгонка изображения для предотвращения искажений */
}

.employee-details {
  display: flex;
  flex-direction: column;
}

.employee-details h4 {
  margin: 0;
  font-size: 16px;
}

.employee-stats {
  display: flex;
  gap: 10px;
}

.employee-stats p {
  margin: 0;
  font-size: 14px;
  color: #555;
}
</style>
