<template>
  <li class="employee-card" @click="goToEmployeePage">
    <div class="avatar-container"
         :class="{ 'no-image': !avatar }"
         :style="{ background: !avatar ? generateGradient : null }">
      <img v-if="avatar" :src="avatar" :alt="`${name || 'Unnamed Employee'}`" />
      <div v-else class="initials">{{ getInitials }}</div>
    </div>
    <div class="employee-details">
      <h4>{{ name || "Unnamed Employee" }}</h4>
      <div class="employee-stats">
        <p>Score: {{ score ?? "N/A" }}</p>
        <p>Reports: {{ reportsCount ?? 0 }}</p>
        <p v-if="departmentName">Store: {{ departmentName }}</p>
        <p>Department ID: {{ departmentId }}</p> <!-- Добавлено для отображения department_id -->
      </div>
    </div>
  </li>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      required: true,
    },
    name: {
      type: String,
      default: "Unnamed Employee",
    },
    departmentId: { // Используем department_id из API
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      score: null, // По умолчанию
      reportsCount: 0, // По умолчанию
      avatar: "", // По умолчанию
      departmentName: "", // По умолчанию
    };
  },
  computed: {
    getInitials() {
      if (!this.name) return '?';
      return this.name
        .split(' ')
        .map(word => word[0])
        .join('')
        .toUpperCase()
        .slice(0, 2);
    },
    generateGradient() {
      const hue = (this.id * 137.508) % 360; // золотое сечение для равномерного распределения
      const saturation = 65; // не слишком яркий
      const lightness = 65; // не слишком тёмный
      const color1 = `hsl(${hue}, ${saturation}%, ${lightness}%)`;
      const color2 = `hsl(${(hue + 40) % 360}, ${saturation}%, ${lightness}%)`;
      return `linear-gradient(45deg, ${color1}, ${color2})`;
    },
  },
  methods: {
    goToEmployeePage() {
      this.$router.push({ name: 'Employee', params: { id: this.id } });
    },
    fetchAdditionalData() {
      // Здесь можно добавить логику для получения дополнительных данных,
      // таких как score, reportsCount, avatar и departmentName, если они доступны через другие API.
      // Например:
      // this.score = await fetchScore(this.id);
      // this.reportsCount = await fetchReportsCount(this.id);
      // this.avatar = await fetchAvatar(this.id);
      // this.departmentName = await fetchDepartmentName(this.departmentId);
    },
  },
  mounted() {
    this.fetchAdditionalData(); // Загружаем дополнительные данные при монтировании компонента
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
  transition: transform 0.3s, box-shadow 0.3s;
}

.employee-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.avatar-container {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #e0e0e0;
}

.avatar-container.no-image {
  background-color: unset; /* Убираем фиксированный цвет фона */
}

.initials {
  color: white;
  font-size: 18px;
  font-weight: bold;
}

.employee-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
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
  flex-wrap: wrap;
}

.employee-stats p {
  margin: 0;
  font-size: 14px;
  color: #555;
}
</style>