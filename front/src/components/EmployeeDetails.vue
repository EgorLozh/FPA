<template>
  <div class="employee-details-page">
    <h2>{{ employee ? employee.name : 'Employee Not Found' }}</h2>
    <div v-if="employee">
      <img :src="employee.avatar || defaultAvatar" :alt="`Avatar of ${employee.name}`" />
      <p>Score: {{ employee.score }}</p>
      <p>Rating: {{ employee.rating }}</p>
      <p v-if="storeName">Store: {{ storeName }}</p>
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
      employee: null,
      defaultAvatar: "path/to/default-avatar.jpg"
    };
  },
  computed: {
    storeName() {
      if (!this.employee) return null;
      const store = this.$root.$data.stores.find(store => store.id === this.employee.storeId);
      return store ? store.name : null;
    }
  },
  created() {
    this.employee = this.$root.$data.employees.find(emp => emp.id === this.id);
  },
  watch: {
    id: {
      immediate: true,
      handler(newId) {
        this.employee = this.$root.$data.employees.find(emp => emp.id === newId);
      }
    }
  }
};
</script>

<style>
.employee-details-page {
  padding: 20px;
}

.employee-details-page img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}
</style>
