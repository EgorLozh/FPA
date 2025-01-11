<template>
  <div class="app-container">
    <Navbar />
    <div class="main-content">
      <router-view :employees="employees" :stores="stores" />
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "App",
  components: { Navbar, Footer },
  data() {
    return {
      employees: [
        { id: 1, name: "Bob Smith", score: 92, rating: 9, storeId: 1 },
        { id: 2, name: "Jane Doe", score: 98, rating: 10, storeId: 1 },
        { id: 3, name: "John Johnson", score: 80, rating: 8, storeId: 2 },
        { id: 4, name: "Alice Brown", score: 85, rating: 8, storeId: 3 },
      ],
      stores: [
        { id: 1, name: "Downtown Store", vector: "path/to/vector02.svg" },
        { id: 2, name: "Uptown Store", vector: "path/to/vector03.svg" },
        { id: 3, name: "Midtown Store", vector: "path/to/vector04.svg" },
        { id: 4, name: "Westside Store", vector: "path/to/vector05.svg" },
        { id: 5, name: "Eastside Store", vector: "path/to/vector06.svg" },
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
