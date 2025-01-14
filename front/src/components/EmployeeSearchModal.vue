<template>
  <transition name="modal-fade">
    <div v-if="show" class="modal-overlay" @click="close">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>Select Employee</h3>
          <button class="close-button" @click="close">&times;</button>
        </div>
        
        <div class="search-controls">
          <SearchInput
            v-model="searchQuery"
            placeholder="Search employees..."
            @input="filterEmployees"
          />
          <div class="sort-controls">
            <select v-model="sortKey" @change="sortEmployees" class="button">
              <option value="name">Name</option>
            </select>
            <button @click="toggleSortOrder" class="button">
              {{ sortOrder === 'asc' ? 'Ascending' : 'Descending' }}
            </button>
          </div>
        </div>

        <div class="employees-list">
          <div v-for="employee in filteredEmployees" 
               :key="employee.id" 
               class="employee-item"
               @click="selectEmployee(employee)">
            <div class="avatar-container" 
                 :class="{ 'no-image': !employee.avatar }"
                 :style="{ background: !employee.avatar ? generateGradient(employee.id) : null }">
              <div class="initials">{{ getInitials(employee.name) }}</div>
            </div>
            <div class="employee-info">
              <div class="employee-name">{{ employee.name }}</div>
              <div class="employee-store">{{ getDepartmentName(employee) }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import SearchInput from './SearchInput.vue'

export default {
  name: 'EmployeeSearchModal',
  components: { SearchInput },
  props: {
    show: Boolean,
    employees: Array,
    departments: Array // Переименовано с stores на departments
  },
  data() {
    return {
      searchQuery: '',
      sortKey: 'name',
      sortOrder: 'asc',
      filteredEmployees: []
    }
  },
  watch: {
    show(newVal) {
      if (newVal) {
        this.filteredEmployees = [...this.employees];
        this.sortEmployees();
      }
    },
    employees: {
      immediate: true,
      handler(newEmployees) {
        this.filteredEmployees = [...newEmployees];
        this.sortEmployees();
      }
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    selectEmployee(employee) {
      this.$emit('select', employee);
      this.close();
    },
    filterEmployees() {
      const query = this.searchQuery.toLowerCase();
      this.filteredEmployees = this.employees.filter(employee =>
        employee.name.toLowerCase().includes(query)
      );
      this.sortEmployees();
    },
    sortEmployees() {
      this.filteredEmployees.sort((a, b) => {
        let result = a.name.localeCompare(b.name);
        return this.sortOrder === 'asc' ? result : -result;
      });
    },
    toggleSortOrder() {
      this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
      this.sortEmployees();
    },
    getDepartmentName(employee) {
      const department = this.departments.find(dept => dept.id === employee.departement_id);
      return department ? department.name : 'Unknown Department';
    },
    getInitials(name) {
      if (!name) return '?';
      return name
        .split(' ')
        .map(word => word[0])
        .join('')
        .toUpperCase()
        .slice(0, 2);
    },
    generateGradient(id) {
      const hue = (id * 137.508) % 360;
      const saturation = 65;
      const lightness = 65;
      const color1 = `hsl(${hue}, ${saturation}%, ${lightness}%)`;
      const color2 = `hsl(${(hue + 40) % 360}, ${saturation}%, ${lightness}%)`;
      return `linear-gradient(45deg, ${color1}, ${color2})`;
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 8px;
  width: 90%;
  max-width: 600px;
  max-height: 80vh;
  display: flex;
  flex-direction: column;
  transform-origin: top;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  border-bottom: 1px solid #eee;
}

.close-button {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.search-controls {
  padding: 15px;
  border-bottom: 1px solid #eee;
}

.sort-controls {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.employees-list {
  overflow-y: auto;
  padding: 15px;
}

.employee-item {
  display: flex;
  align-items: center;
  padding: 10px;
  border: 1px solid #eee;
  margin-bottom: 8px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.employee-item:hover {
  background-color: #f5f5f5;
}

.avatar-container {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
}

.avatar-container.no-image {
  background-color: unset;
}

.initials {
  color: white;
  font-size: 18px;
  font-weight: bold;
}

.employee-info {
  flex-grow: 1;
}

.employee-name {
  font-weight: bold;
}

.employee-store {
  font-size: 0.9em;
  color: #666;
}

.employee-score {
  color: #2193f2;
  font-weight: bold;
}

.button {
  background-color: #2193f2;
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.button:hover {
  background-color: #1976d2;
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(33, 147, 242, 0.3);
}

.button:active {
  transform: scale(0.95) translateY(0);
  box-shadow: 0 1px 4px rgba(33, 147, 242, 0.2);
}

select.button {
  background-color: white;
  color: #2193f2;
  border: 1px solid #2193f2;
}

select.button:hover {
  background-color: #f5f5f5;
}

/* Transition classes */
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.modal-fade-enter-to,
.modal-fade-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>
