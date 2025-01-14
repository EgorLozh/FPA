<template>
  <div class="dashboard-container">
    <Dashboard
      :departments="departmentsWithEmployees"
      :workers="workers"
    />
  </div>
</template>

<script>
import Dashboard from "@/components/Dashboard.vue";

export default {
  name: "DashboardView",
  components: { Dashboard },
  props: {
    workers: {
      type: Array,
      required: true,
      default: () => [],
    },
    departments: {
      type: Array,
      required: true,
      default: () => [],
    },
  },
  computed: {
    departmentsWithEmployees() {
      const departments = this.departments || [];
      const workers = this.workers || [];

      return departments.map((department) => ({
        ...department,
        employees: workers.filter(
          (worker) => worker.department_id === department.id
        ),
      }));
    },
  },
};
</script>

<style>
.dashboard-container {
  width: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  transition: opacity 0.5s;
}

.dashboard-container-enter-active, .dashboard-container-leave-active {
  transition: opacity 0.5s;
}

.dashboard-container-enter, .dashboard-container-leave-to {
  opacity: 0;
}

.menu-list {
  display: flex;
  gap: 16px;
  list-style: none;
  padding: 0;
}

.btn-primary {
  background-color: #2193f2;
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-secondary {
  background-color: #e8edf4;
  color: #0c141c;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.button {
  background-color: #2193f2;
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin: 10px;
  transition: background-color 0.3s, transform 0.3s;
}

.button:active {
  transform: scale(0.95);
}
</style>