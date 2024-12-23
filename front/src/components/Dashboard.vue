<template>
    <div class="dashboard">
      <!-- Заголовок -->
      <h1>Dashboard</h1>
  
      <!-- Поисковая строка -->
      <div class="search-bar">
        <input
          type="text"
          placeholder="Search employees..."
          v-model="searchQuery"
        />
      </div>
  
      <!-- Список сотрудников -->
      <div class="employee-list">
        <div
          v-for="employee in filteredEmployees"
          :key="employee.id"
          class="employee-card"
        >
          <img :src="employee.avatar" alt="Avatar" class="avatar" />
          <div class="employee-info">
            <h3>{{ employee.name }}</h3>
            <p>Compliance Score: {{ employee.score }}%</p>
          </div>
          <span class="rating">{{ employee.rating }}/10</span>
        </div>
      </div>
  
      <!-- Список магазинов -->
      <div class="store-list">
        <h2>Stores</h2>
        <ul>
          <li v-for="store in stores" :key="store">{{ store }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from "vue";
  
  // Список сотрудников
  const employees = ref([
    {
      id: 1,
      name: "Bob Smith",
      score: 92,
      rating: 9,
      avatar: "https://placekitten.com/50/50", // Пример аватара
    },
    {
      id: 2,
      name: "Jane Doe",
      score: 98,
      rating: 10,
      avatar: "https://placekitten.com/51/51",
    },
    {
      id: 3,
      name: "John Johnson",
      score: 80,
      rating: 8,
      avatar: "https://placekitten.com/52/52",
    },
  ]);
  
  // Список магазинов
  const stores = ref([
    "Downtown Store",
    "Uptown Store",
    "Midtown Store",
    "Westside Store",
    "Eastside Store",
  ]);
  
  // Поиск сотрудников
  const searchQuery = ref("");
  
  const filteredEmployees = computed(() => {
    return employees.value.filter((employee) =>
      employee.name.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  });
  </script>
  
  <style scoped>
  .dashboard {
    font-family: Arial, sans-serif;
    padding: 20px;
    background-color: #f9fafb;
  }
  
  h1 {
    font-size: 2em;
    margin-bottom: 10px;
  }
  
  .search-bar input {
    width: 100%;
    padding: 10px;
    font-size: 1em;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 20px;
  }
  
  .employee-list {
    margin-bottom: 30px;
  }
  
  .employee-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #fff;
    margin-bottom: 10px;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
  }
  
  .employee-info h3 {
    margin: 0;
    font-size: 1.1em;
  }
  
  .employee-info p {
    margin: 5px 0 0;
    font-size: 0.9em;
    color: #666;
  }
  
  .rating {
    font-weight: bold;
  }
  
  .store-list h2 {
    font-size: 1.5em;
    margin-bottom: 10px;
  }
  
  .store-list ul {
    list-style-type: none;
    padding: 0;
  }
  
  .store-list li {
    padding: 5px 0;
    cursor: pointer;
    border-bottom: 1px solid #eee;
  }
  
  .store-list li:hover {
    color: #007bff;
    transition: 0.3s;
  }
  </style>
  