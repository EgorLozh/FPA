<template>
  <div id="app">
    <!-- Навигационная панель -->
    <Navbar />

    <!-- Основной контент: Dashboard -->
    <main>
      <Dashboard>
        <!-- Секция с сотрудниками -->
        <section class="employee-section">
          <h2>Employees</h2>
          <input type="text" placeholder="Search employees..." v-model="searchQuery" />
          <div class="employee-list">
            <EmployeeCard
              v-for="employee in filteredEmployees"
              :key="employee.id"
              :name="employee.name"
              :score="employee.score"
              :rating="employee.rating"
              :avatar="employee.avatar"
            />
          </div>
        </section>

        <!-- Секция с магазинами -->
        <section class="store-section">
          <h2>Stores</h2>
          <StoreList :stores="stores" />
        </section>
      </Dashboard>
    </main>

    <!-- Футер -->
    <Footer />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Dashboard from "./components/Dashboard.vue";
import EmployeeCard from "./components/EmployeeCard.vue";
import Footer from "./components/Footer.vue";
import StoreList from "./components/StoreList.vue";

export default {
  components: {
    Navbar,
    Dashboard,
    EmployeeCard,
    Footer,
    StoreList,
  },
  data() {
    return {
      searchQuery: "",
      employees: [
        { id: 1, name: "Bob Smith", score: "92%", rating: "9/10", avatar: "cat1.jpg" },
        { id: 2, name: "Jane Doe", score: "98%", rating: "10/10", avatar: "cat2.jpg" },
        { id: 3, name: "John Johnson", score: "80%", rating: "8/10", avatar: "cat3.jpg" },
      ],
      stores: [
        { id: 1, name: "Downtown Store" },
        { id: 2, name: "Uptown Store" },
        { id: 3, name: "Midtown Store" },
        { id: 4, name: "Westside Store" },
        { id: 5, name: "Eastside Store" },
      ],
    };
  },
  computed: {
    filteredEmployees() {
      return this.employees.filter((employee) =>
        employee.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
};
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  height: 100%;
}

main {
  flex-grow: 1;
  padding: 20px 5%;
}

.employee-section,
.store-section {
  margin-bottom: 40px;
}

input[type="text"] {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.employee-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.store-section {
  margin-top: 30px;
}
</style>
