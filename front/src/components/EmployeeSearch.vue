<template>
  <div class="search-container">
    <div class="search-box">
      <input 
        type="text" 
        v-model="searchQuery" 
        :placeholder="placeholder"
        @focus="showList = true"
      >
      <div class="search-options" v-if="showSortOptions">
        <select v-model="sortKey" @change="handleSort">
          <option value="name">Name</option>
          <option value="score">Score</option>
          <option value="storeName">Store</option>
        </select>
        <button @click="toggleSortOrder" class="sort-button">
          {{ sortOrder === 'asc' ? 'Ascending' : 'Descending' }}
        </button>
      </div>
    </div>
    <div class="employee-list" v-if="showList && filteredEmployees.length > 0">
      <div v-for="employee in sortedEmployees" 
           :key="employee.id" 
           class="employee-item"
           @click="selectEmployee(employee)">
        <div class="employee-info">
          <img :src="employee.avatar" alt="avatar" class="employee-avatar" v-if="employee.avatar">
          <span class="employee-name">{{ employee.name }}</span>
        </div>
        <span class="employee-score" v-if="employee.score">Score: {{ employee.score }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EmployeeSearch',
  props: {
    employees: {
      type: Array,
      required: true
    },
    placeholder: {
      type: String,
      default: 'Search employees...'
    },
    showSortOptions: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      searchQuery: '',
      showList: false,
      sortKey: 'name',
      sortOrder: 'asc'
    }
  },
  computed: {
    filteredEmployees() {
      return this.employees.filter(emp => 
        emp.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      )
    },
    sortedEmployees() {
      return [...this.filteredEmployees].sort((a, b) => {
        let result;
        if (this.sortKey === 'score') {
          result = b.score - a.score;
        } else {
          result = a.name.localeCompare(b.name);
        }
        return this.sortOrder === 'asc' ? result : -result;
      })
    }
  },
  methods: {
    selectEmployee(employee) {
      this.$emit('select', employee);
      this.showList = false;
      this.searchQuery = '';
    },
    handleSort() {
      this.$emit('sort', { key: this.sortKey, order: this.sortOrder });
    },
    toggleSortOrder() {
      this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
      this.handleSort();
    }
  },
  mounted() {
    document.addEventListener('click', (e) => {
      if (!this.$el.contains(e.target)) {
        this.showList = false;
      }
    })
  }
}
</script>

<style scoped>
.search-container {
  position: relative;
  width: 100%;
}

.search-box {
  width: 100%;
}

.search-box input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.search-options {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.employee-list {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  max-height: 300px;
  overflow-y: auto;
  background: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  z-index: 1000;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.employee-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px;
  cursor: pointer;
  border-bottom: 1px solid #eee;
}

.employee-item:hover {
  background-color: #f5f5f5;
}

.employee-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.employee-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}

.employee-score {
  color: #666;
  font-size: 0.9em;
}

.sort-button {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
  cursor: pointer;
}

select {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>
