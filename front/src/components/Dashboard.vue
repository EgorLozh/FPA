<template>
  <section class="dashboard">
    <div class="search-bar">
      <input 
        type="text" 
        v-model="searchQuery" 
        placeholder="Search stores..." 
        @input="filterStores" 
      />
    </div>
    <h2>Store Rankings</h2>
    <StoreList 
      :stores="filteredStores" 
      @selectStore="selectStore"
    />
    <section class="employees-section">
      <h2 v-if="selectedStore">
        Employees at {{ selectedStore.name }}
      </h2>
      <h2 v-else>All Employees</h2>
      <div class="employee-cards">
        <EmployeeCard
          v-for="employee in filteredEmployees"
          :key="employee.id"
          :name="employee.name"
          :score="employee.score"
          :rating="employee.rating"
        />
      </div>
    </section>
  </section>
</template>

<script>
import StoreList from './StoreList.vue';
import EmployeeCard from './EmployeeCard.vue';

export default {
  components: { StoreList, EmployeeCard },
  props: {
    stores: Array,
    employees: Array,
  },
  data() {
    return {
      searchQuery: "",
      filteredStores: this.stores,
      selectedStore: null,
    };
  },
  computed: {
    filteredEmployees() {
      if (this.selectedStore) {
        return this.employees.filter(
          (employee) => employee.storeId === this.selectedStore.id
        );
      }
      return this.employees;
    },
  },
  methods: {
    filterStores() {
      const query = this.searchQuery.toLowerCase();
      this.filteredStores = this.stores.filter((store) =>
        store.name.toLowerCase().includes(query)
      );
    },
    selectStore(store) {
      this.selectedStore = store;
    },
  },
};
</script>

<style>
.dashboard {
  max-width: 80%;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin: 0 auto; /* Center the dashboard */
}

.search-bar {
  max-width: 100%;
  display: flex;
  justify-content: center;
}

.search-bar input {
  width: 80%;
  padding: 8px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.employees-section {
  margin-top: 32px;
}

.employee-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 16px;
}
</style>
