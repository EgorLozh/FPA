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
        <p v-if="storeName">Store: {{ storeName }}</p>
        <p>Department ID: {{ departmentId }}</p>
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
    departmentId: {
      type: Number,
      required: true,
    },
    departments: { // Добавляем пропс для списка отделов
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      score: null,
      reportsCount: 0,
      avatar: "",
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
      const hue = (this.id * 137.508) % 360;
      const saturation = 65;
      const lightness = 65;
      const color1 = `hsl(${hue}, ${saturation}%, ${lightness}%)`;
      const color2 = `hsl(${(hue + 40) % 360}, ${saturation}%, ${lightness}%)`;
      return `linear-gradient(45deg, ${color1}, ${color2})`;
    },
    storeName() {
      const department = this.departments.find(dept => dept.id === this.departmentId);
      return department ? department.name : 'Unknown Store';
    },
  },
  methods: {
    goToEmployeePage() {
      this.$router.push({ name: 'Employee', params: { id: this.id } });
    },
    fetchAdditionalData() {
      // Логика для получения дополнительных данных
    },
  },
  mounted() {
    this.fetchAdditionalData();
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
  background-color: unset;
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