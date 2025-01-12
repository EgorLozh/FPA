<template>
  <div class="employee-details-page">
    <div class="employee-card" v-if="employee">
      <div class="employee-header">
        <div class="avatar-wrapper">
          <div class="name-container" :style="{ background: generateGradient }">
            <div class="full-name">{{ employee.name }}</div>
          </div>
        </div>
        <h2>{{ employee.name }}</h2>
      </div>
      
      <div class="employee-info">
        <div class="info-item">
          <span class="label">Score</span>
          <span class="value">{{ employee.score }}</span>
        </div>
        <div class="info-item">
          <span class="label">Reports Count</span>
          <span class="value">{{ employee.reportsCount }}</span>
        </div>
        <div class="info-item" v-if="storeName">
          <span class="label">Store</span>
          <span class="value">{{ storeName }}</span>
        </div>
      </div>
    </div>
    <div v-else class="not-found">
      <h2>Employee Not Found</h2>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      employee: null
    };
  },
  computed: {
    storeName() {
      if (!this.employee) return null;
      const store = this.$root.$data.stores.find(store => store.id === this.employee.storeId);
      return store ? store.name : null;
    },
    departmentName() {
      if (!this.employee) return null;
      const dept = this.$root.$data.departments.find(dept => dept.id === this.employee.departmentId);
      return dept ? dept.name : null;
    },
    getInitials() {
      if (!this.employee?.name) return '?';
      return this.employee.name
        .split(' ')
        .map(word => word[0])
        .join('')
        .toUpperCase()
        .slice(0, 2);
    },
    generateGradient() {
      const hue = (this.id * 137.508) % 360;
      const saturation = 75;  // Увеличили насыщенность
      const lightness = 60;   // Немного темнее для лучшей читаемости текста
      const color1 = `hsl(${hue}, ${saturation}%, ${lightness}%)`;
      const color2 = `hsl(${(hue + 60) % 360}, ${saturation}%, ${lightness}%)`;
      return `linear-gradient(135deg, ${color1}, ${color2})`;
    }
  },
  created() {
    this.employee = this.$root.$data.workers.find(worker => worker.id === this.id);
  },
  watch: {
    id: {
      immediate: true,
      handler(newId) {
        this.employee = this.$root.$data.workers.find(worker => worker.id === newId);
      }
    }
  }
};
</script>

<style>
/* Сбросим некоторые базовые стили, которые могут мешать */
* {
  box-sizing: border-box;
}

.employee-details-page {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  min-height: 100vh;
}

.employee-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 3rem;
  width: 100%;
}

.employee-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  margin-bottom: 3rem;
  width: 100%;
}

/* Новый контейнер-обертка для аватара */
.avatar-wrapper {
  width: 500px;
  height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.name-container {
  width: 100%;
  height: 100%;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
  padding: 2rem;
}

.full-name {
  color: white;
  font-size: 3.5rem;
  font-weight: 600;
  text-align: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  word-wrap: break-word;
  max-width: 100%;
}

.employee-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.info-item {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.info-item .label {
  color: #666;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.info-item .value {
  font-size: 1.5rem;
  font-weight: 600;
  color: #333;
}

.not-found {
  text-align: center;
  color: #666;
  padding: 3rem;
}
</style>
