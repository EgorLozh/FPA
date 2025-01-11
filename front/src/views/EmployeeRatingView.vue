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
    </div>
    <ul class="employee-list">
      <EmployeeCard
        v-for="employee in filteredEmployees"
        :key="employee.id"
        :name="employee.name"
        :score="employee.score"
        :rating="calculateRating(employee.score)"
        :avatar="employee.avatar"
        :storeName="employee.storeName"
      />
    </ul>
  </section>
</template>

<script>
import EmployeeCard from '@/components/EmployeeCard.vue';

export default {
  components: { EmployeeCard },
  props: {
    employees: Array,
  },
  data() {
    return {
      employeeSearchQuery: "",
      filteredEmployees: [],
      sortKey: "name",
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
        if (this.sortKey === "score") {
          return b.score - a.score;
        } else if (this.sortKey === "storeName") {
          return a.storeName.localeCompare(b.storeName);
        } else {
          return a.name.localeCompare(b.name);
        }
      });
    },
    calculateRating(score) {
      return (score / 20).toFixed(2); // Example calculation
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
</style>
