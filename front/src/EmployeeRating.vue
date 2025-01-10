<template>
  <section class="employee-rating">
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
import EmployeeCard from '@/components/EmployeeCard.vue';

export default {
  components: { EmployeeCard },
  props: {
    employees: Array,
  },
  data() {
    return {
      employeeSearchQuery: "",
      filteredEmployees: this.employees,
    };
  },
  methods: {
    filterEmployees() {
      const query = this.employeeSearchQuery.toLowerCase();
      this.filteredEmployees = this.employees.filter(employee =>
        employee.name.toLowerCase().includes(query)
      );
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
  width: 80%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
