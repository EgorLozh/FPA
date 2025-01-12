<template>
  <section class="employee-rating">
    <h2>Employee Ratings</h2>
    <div class="employee-search">
      <input 
        type="text" 
        v-model="employeeSearchQuery" 
        placeholder="Search employees..." 
        @input="filterEmployees" 
      />
      <select v-model="sortKey" @change="sortEmployees">
        <option value="name">Name</option>
        <option value="score">Score</option>
        <option value="storeName">Store</option>
      </select>
      <button @click="toggleSortOrder" class="button">
        {{ sortOrder === 'asc' ? 'Ascending' : 'Descending' }}
      </button>
    </div>
    <transition-group name="fade" tag="ul" class="employee-list">
      <li v-for="(employee, index) in filteredEmployees" :key="employee.id">
        <span>{{ index + 1 }}</span>
        <EmployeeCard
          :id="employee.id"
          :name="employee.name"
          :score="employee.score"
          :reportsCount="employee.reportsCount"
          :avatar="employee.avatar"
          :storeName="getStoreName(employee)"
        />
      </li>
    </transition-group>
  </section>
</template>

<script>
import EmployeeCard from '@/components/EmployeeCard.vue';

export default {
  components: { EmployeeCard },
  props: {
    employees: Array,
    stores: Array,
  },
  data() {
    return {
      employeeSearchQuery: "",
      filteredEmployees: [],
      sortKey: "name",
      sortOrder: "asc",
    };
  },
  mounted() {
    this.filteredEmployees = this.employees || [];
    this.sortEmployees();
  },
  watch: {
    employees: {
      immediate: true,
      handler(newEmployees) {
        this.filteredEmployees = newEmployees || [];
        this.sortEmployees();
      }
    }
  },
  methods: {
    filterEmployees() {
      const query = this.employeeSearchQuery.toLowerCase();
      this.filteredEmployees = this.employees.filter(employee =>
        employee.name.toLowerCase().includes(query)
      );
      this.sortEmployees();
    },
    sortEmployees() {
      this.filteredEmployees.sort((a, b) => {
        let result;
        if (this.sortKey === "score") {
          result = b.score - a.score;
        } else if (this.sortKey === "storeName") {
          const storeA = this.getStoreName(a);
          const storeB = this.getStoreName(b);
          result = storeA.localeCompare(storeB);
        } else {
          result = a.name.localeCompare(b.name);
        }
        return this.sortOrder === 'asc' ? result : -result;
      });
    },
    toggleSortOrder() {
      this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
      this.sortEmployees();
    },
    getStoreName(employee) {
      const store = this.stores.find(store => store.id === employee.storeId);
      return store ? store.name : 'Unknown Store';
    },
  },
};
</script>

<style>
.employee-rating {
  max-width: 80%;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
}

.employee-search {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.employee-search input {
  width: 60%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.employee-search select {
  width: 20%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin-left: 10px;
}

.employee-search button {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin-left: 10px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}
.employee-search button:active {
  transform: scale(0.95);
}

.employee-list li {
  display: flex;
  align-items: center;
  width: 100%; /* Allow the list items to take full width */
}

.employee-list li span {
  margin-right: 10px;
  font-weight: bold;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
