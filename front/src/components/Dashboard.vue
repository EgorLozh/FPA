<template>
  <section class="dashboard">
    <!-- Поиск магазинов -->
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
    <div class="overall-rating">
      <h3>Overall Employee Rating: {{ overallRating }}</h3>
    </div>
    <div class="employee-search">
      <input 
        type="text" 
        v-model="employeeSearchQuery" 
        placeholder="Search employees..." 
        @input="filterEmployees" 
      />
    </div>
    <ul class="employee-list">
      <EmployeeCard
        v-for="employee in filteredEmployees"
        :key="employee.id"
        :name="employee.name"
        :score="employee.score"
        :rating="employee.rating"
        :avatar="employee.avatar"
        :storeName="employee.storeName"
      />
    </ul>
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
      searchQuery: "", // Поиск по магазинам
      filteredStores: this.stores,
      selectedStore: null,
      employeeSearchQuery: "",
      filteredEmployees: this.getAllEmployees(),
    };
  },
  computed: {
    overallRating() {
      const totalRating = this.stores.reduce((sum, store) => {
        return sum + store.employees.reduce((storeSum, employee) => storeSum + employee.rating, 0);
      }, 0);
      const totalEmployees = this.stores.reduce((sum, store) => sum + store.employees.length, 0);
      return (totalEmployees > 0) ? (totalRating / totalEmployees).toFixed(2) : "N/A";
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
    getAllEmployees() {
      return this.stores.flatMap(store => store.employees.map(employee => ({
        ...employee,
        storeName: store.name,
      })));
    },
    filterEmployees() {
      const query = this.employeeSearchQuery.toLowerCase();
      this.filteredEmployees = this.getAllEmployees().filter(employee =>
        employee.name.toLowerCase().includes(query)
      );
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
  margin: 0 auto; /* Центрирование дашборда */
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

.overall-rating {
  text-align: center;
  margin: 20px 0;
}

.employee-search {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.employee-search input {
  width: 80%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
