<template>
  <section class="employee-rating">
    <h2>Employee Ratings</h2>
    <div class="search-section">
      <SearchInput
        v-model="employeeSearchQuery"
        placeholder="Search employees by name..."
        @input="filterEmployees"
      />
      <div class="sort-controls">
        <select v-model="sortKey" @change="sortEmployees" class="button">
          <option value="name">Name</option>
          <option value="rating">Rating</option>
          <option value="departmentName">Department</option>
        </select>
        <button @click="toggleSortOrder" class="button">
          {{ sortOrder === 'asc' ? 'Ascending' : 'Descending' }}
        </button>
      </div>
    </div>
    <transition-group name="fade" tag="ul" class="employee-list">
      <li v-for="(employee, index) in filteredEmployees" :key="employee.id">
        <span>{{ index + 1 }}</span>
        <EmployeeCard
          :id="employee.id"
          :name="employee.name"
          :department-name="getDepartmentName(employee)"
        />
      </li>
    </transition-group>
  </section>
</template>

<script>
import SearchInput from '@/components/SearchInput.vue'
import EmployeeCard from '@/components/EmployeeCard.vue'

export default {
  components: { 
    SearchInput,
    EmployeeCard 
  },
  props: {
    workers: Array,
    departments: Array,
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
    this.filteredEmployees = this.workers || [];
    this.sortEmployees();
  },
  watch: {
    workers: {
      immediate: true,
      handler(newWorkers) {
        this.filteredEmployees = newWorkers || [];
        this.sortEmployees();
      }
    }
  },
  methods: {
    filterEmployees() {
      const query = this.employeeSearchQuery.toLowerCase();
      this.filteredEmployees = this.workers.filter(worker =>
        worker.name.toLowerCase().includes(query)
      );
      this.sortEmployees();
    },
    sortEmployees() {
      this.filteredEmployees.sort((a, b) => {
        let result;
        if (this.sortKey === "rating") {
          result = b.rating - a.rating;
        } else if (this.sortKey === "departmentName") {
          const deptA = this.getDepartmentName(a);
          const deptB = this.getDepartmentName(b);
          result = deptA.localeCompare(deptB);
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
    getDepartmentName(worker) {
      const department = this.departments.find(dept => dept.id === worker.departement_id);
      return department ? department.name : 'Unknown Department';
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

.search-section {
  max-width: 800px;
  margin: 0 auto 20px;
  padding: 0 20px;
}

.sort-controls {
  display: flex;
  gap: 10px;
  margin-top: 10px;
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