<template>
  <div class="app-container">
    <Navbar />
    <div v-if="loading" class="loading">Loading...</div>
    <div v-if="error" class="error">{{ error }}</div>
    <transition 
      name="page-fade" 
      mode="out-in"
      @before-enter="beforeEnter"
      @enter="enter"
      @leave="leave"
    >
      <router-view
        :employees="employees" 
        :stores="stores"
        :loading="loading"
        class="main-content"
      />
    </transition>
    <Footer />
  </div>
</template>

<script>
import { api } from '@/services/api';
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import EmployeeDetails from "@/components/EmployeeDetails.vue";

export default {
  name: "App",
  components: { Navbar, Footer, EmployeeDetails },
  data() {
    return {
      employees: [],
      stores: [],
      loading: false,
      error: null
    };
  },
  async created() {
    await this.fetchData();
  },
  methods: {
    async fetchData() {
      this.loading = true;
      this.error = null;
      try {
        // Загружаем данные параллельно
        const [employeesData, storesData] = await Promise.all([
          api.getEmployees(),
          api.getStores()
        ]);
        this.employees = employeesData;
        this.stores = storesData;
      } catch (err) {
        this.error = "Error loading data: " + err.message;
        console.error("API Error:", err);
      } finally {
        this.loading = false;
      }
    },
    beforeEnter(el) {
      el.style.opacity = 0;
      el.style.transform = 'translateY(10px)';
    },
    enter(el, done) {
      const delay = el.dataset.index * 100;
      setTimeout(() => {
        el.style.transition = 'opacity 0.5s, transform 0.5s';
        el.style.opacity = 1;
        el.style.transform = 'translateY(0)';
        done();
      }, delay);
    },
    leave(el, done) {
      el.style.transition = 'opacity 0.5s, transform 0.5s';
      el.style.opacity = 0;
      el.style.transform = 'translateY(10px)';
      setTimeout(() => {
        done();
      }, 500);
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
  position: relative; /* Ensure correct positioning */
  display: block; /* Ensure block display for animation */
}

.menu-list {
  display: flex;
  gap: 16px;
  list-style: none;
  padding: 0;
}

.button {
  background-color: #2193f2;
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin: 10px;
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

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.page-fade-enter-active, .page-fade-leave-active {
  transition: opacity 0.5s, transform 0.5s;
}

.page-fade-enter, .page-fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

.page-fade-leave-active {
  position: absolute;
  width: 100%;
}

.page-fade-enter-active {
  position: absolute;
  width: 100%;
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
</style>
