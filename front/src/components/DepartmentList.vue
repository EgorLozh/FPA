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
              :department-name="department.name"
            />
          </ul>
        </transition>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    departments: {
      type: Array,
      required: true,
    },
  },
  methods: {
    handleToggle(department) {
      department.open = !department.open;
    },
  },
};
</script>

<style>
.department-list {
  list-style: none;
  padding: 0;
}

.department-card {
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 10px;
}

.employee-list {
  list-style: none;
  padding-left: 20px;
  margin-top: 10px;
}

.slide-fade-enter-active, .slide-fade-leave-active {
  transition: all 0.3s ease;
}

.slide-fade-enter, .slide-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>