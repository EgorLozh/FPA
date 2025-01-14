<template>
  <div class="app-container">
    <Navbar />
    <div v-if="loading" class="loading">Loading...</div>
    <div v-if="error" class="error">{{ error }}</div>

    <router-view v-slot="{ Component }">
      <transition name="page-fade" mode="out-in">
        <component
          :is="Component"
          :workers="workers"
          :departments="departments"
          :scripts="scripts"
          :reports="reports"
          :requests="requests"
          :loading="loading"
          class="main-content"
        />
      </transition>
    </router-view>

    <Footer />
  </div>
</template>

<script>
import { api } from "@/services/api";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "App",
  components: { Navbar, Footer },
  data() {
    return {
      workers: [],
      departments: [],
      scripts: [],
      reports: [],
      requests: [],
      loading: false,
      error: null,
    };
  },
  async created() {
    await this.fetchData();
  },
  methods: {
    createPlaceholderData() {
    const placeholderDepartment = {
      id: 1,
      name: 'Placeholder Department',
    };

    const placeholderWorker = {
      id: 1,
      name: 'Placeholder Worker',
      department_id: 1,
    };

    this.departments = [placeholderDepartment];
    this.workers = [placeholderWorker];
  },

  async fetchData() {
  this.loading = true;
  this.error = null;
  try {
    const [workersResponse, departmentsResponse] = await Promise.all([
      api.getWorkers(),
      api.getDepartments(),
    ]);

    console.log('Workers Response:', workersResponse);
    console.log('Departments Response:', departmentsResponse);

    // Если массивы пусты, создаем placeholder-данные
    if (workersResponse.length === 0 && departmentsResponse.length === 0) {
      this.createPlaceholderData();
    } else {
      // Если данные есть, используем их
      this.departments = departmentsResponse.map((dept) => ({
        ...dept,
        workers: workersResponse.filter((worker) => worker.department_id === dept.id),
      }));

      this.workers = workersResponse;
    }
  } catch (err) {
    this.error = "Error loading data: " + err.message;
    console.error("API Error:", err);

    // Если произошла ошибка, создаем placeholder-данные
    this.createPlaceholderData();
  } finally {
    this.loading = false;
  }
},
},
};
</script>

<style>
.app-container {
  width: 100%;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  width: 100%;
  padding: 16px;
  position: relative;
  display: block;
}

.loading {
  text-align: center;
  padding: 20px;
  font-size: 1.2em;
  color: #2193f2;
}

.error {
  text-align: center;
  padding: 20px;
  color: red;
  background-color: #ffebee;
  margin: 10px;
  border-radius: 4px;
}

.page-fade-enter-active,
.page-fade-leave-active {
  transition: opacity 0.5s, transform 0.5s;
}

.page-fade-enter,
.page-fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>