<template>
  <div class="app-container">
    <Navbar />
    <div class="main-content">
      <router-view
       :employees="employees" 
       :stores="stores" 
       :calculateRating="calculateRating" />
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
        { id: 1, name: "Bob Smith", score: 92, rating: 0, storeId: 1 },
        { id: 2, name: "Jane Doe", score: 98, rating: 0, storeId: 1 },
        { id: 3, name: "John Johnson", score: 80, rating: 0, storeId: 2 },
        { id: 4, name: "Alice Brown", score: 85, rating: 0, storeId: 3 },
        { id: 5, name: "Random Person 1", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
        { id: 6, name: "Random Person 2", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
        { id: 7, name: "Random Person 3", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
        { id: 8, name: "Random Person 4", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
        { id: 9, name: "Random Person 5", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
        { id: 10, name: "Random Person 6", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
        { id: 11, name: "Random Person 7", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
        { id: 12, name: "Random Person 8", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
        { id: 13, name: "Random Person 9", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
        { id: 14, name: "Random Person 10", score: Math.floor(Math.random() * 100), rating: 0, storeId: Math.floor(Math.random() * 5) + 1 },
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
  methods: {
    calculateRating(score) {
      return (score / 20).toFixed(2); 
    },
    initializeRatings() {
      this.employees.forEach(employee => {
        employee.rating = this.calculateRating(employee.score);
      });
    },
  },
  created() {
    this.initializeRatings();
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
