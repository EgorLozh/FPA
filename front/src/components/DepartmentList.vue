<template>
  <div>
    <ul class="department-list">
      <li 
        v-for="department in departments" 
        :key="department.id" 
        class="department-card"
      >
        <details @toggle="handleToggle(department)">
          <summary>{{ department.name }}</summary>
        </details>
        <transition name="slide-fade">
          <ul v-if="department.open" class="employee-list">
            <EmployeeCard
              v-for="worker in department.workers"
              :key="worker.id"
              :id="worker.id"
              :name="worker.name"
              :score="worker.rating"
              :reportsCount="worker.reportsCount"
              :avatar="worker.avatar"
              :departmentName="department.name"
            />
          </ul>
        </transition>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  // ...existing code...
  props: {
    departments: {
      type: Array,
      required: true,
    },
  },
};
</script>
