<template>
  <div class="app-container">
    <Navbar />
    <div class="main-content">
      <Dashboard :stores="stores" :employees="employees">
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
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import Dashboard from "@/components/Dashboard.vue";

export default {
  name: "App",
  components: { Navbar, Footer, Dashboard },
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
