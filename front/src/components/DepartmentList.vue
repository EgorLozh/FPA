<template>
  <ul class="department-list">
    <li
      v-for="department in departments"
      :key="department.id"
      class="department-item"
      :class="{ expanded: department.isExpanded }"
      @click="toggleDepartment(department)"
    >
      <div class="department-header">
        <h3>{{ department.name }}</h3>
        <span class="toggle-icon">
          {{ department.isExpanded ? "▲" : "▼" }}
        </span>
      </div>
      <transition name="slide-fade">
        <div v-if="department.isExpanded" class="employee-list">
          <EmployeeCard
            v-for="employee in department.employees"
            :key="employee.id"
            :id="employee.id"
            :name="employee.name"
            :departmentId="employee.department_id"
          />
        </div>
      </transition>
    </li>
  </ul>
</template>

<script>
import EmployeeCard from './EmployeeCard.vue';

export default {
  components: { EmployeeCard },
  props: {
    departments: {
      type: Array,
      required: true,
    },
  },
  methods: {
    toggleDepartment(department) {
      department.isExpanded = !department.isExpanded;
    },
  },
};
</script>

<style scoped>
.department-list {
  list-style: none;
  padding: 0;
}

.department-item {
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 15px;
  background-color: #fff;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.department-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.department-item.expanded {
  background-color: #f9f9f9;
}

.department-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.department-header h3 {
  margin: 0;
  font-size: 18px;
  color: #333;
}

.toggle-icon {
  font-size: 14px;
  color: #666;
}

.employee-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid #eee;
}

/* Анимация раскрытия */
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>