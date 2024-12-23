<template>
  <div class="app-container">
    <Navbar />
    <div class="main-content">
      <Dashboard>
        <template #header>
          <h1>Script Tracker</h1>
        </template>
        <template #menu>
          <ul class="menu-list">
            <li>Dashboard</li>
            <li>Reports</li>
            <li>Employees</li>
            <li>Stores</li>
          </ul>
        </template>
        <template #actions>
          <button class="btn-primary">New Report</button>
          <button class="btn-secondary">Log in / Sign up</button>
        </template>
      </Dashboard>
      <section class="employees-section">
        <h2>Employees</h2>
        <div class="employee-cards">
          <EmployeeCard
            v-for="employee in employees"
            :key="employee.name"
            :name="employee.name"
            :score="employee.score"
            :rating="employee.rating"
          />
        </div>
      </section>
      <StoreList :stores="stores" />
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import Dashboard from "@/components/Dashboard.vue";
import EmployeeCard from "@/components/EmployeeCard.vue";
import StoreList from "@/components/StoreList.vue";

export default {
  name: "App",
  components: { Navbar, Footer, Dashboard, EmployeeCard, StoreList },
  data() {
    return {
      employees: [
        { name: "Bob Smith", score: 92, rating: 9 },
        { name: "Jane Doe", score: 98, rating: 10 },
        { name: "John Johnson", score: 80, rating: 8 },
      ],
      stores: [
        { name: "Downtown Store", vector: "path/to/vector02.svg" },
        { name: "Uptown Store", vector: "path/to/vector03.svg" },
        { name: "Midtown Store", vector: "path/to/vector04.svg" },
        { name: "Westside Store", vector: "path/to/vector05.svg" },
        { name: "Eastside Store", vector: "path/to/vector06.svg" },
      ],
    };
  },
};
</script>

<style>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  padding: 16px;
}

.employees-section {
  margin-top: 32px;
}

.employee-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 16px;
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
</style>
