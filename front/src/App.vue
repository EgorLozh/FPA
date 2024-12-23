<template>
  <div id="app">
    <!-- Навигация -->
    <nav class="navigation">
      <div class="logo">MyApp</div>
      <div class="nav-buttons">
        <button @click="goTo('home')">Home</button>
        <button @click="goTo('about')">About</button>
        <button @click="goTo('contact')">Contact</button>
        <button @click="goTo('login')">Login</button>
      </div>
    </nav>

    <!-- Основной контент (Dashboard) -->
    <main class="dashboard">
      <section class="search-bar">
        <input type="text" placeholder="Search stores or employees..." />
      </section>

      <section class="store-list-section">
        <h2>Stores</h2>
        <StoreList :stores="stores" />
      </section>

      <section class="employee-list-section">
        <h2>Employees</h2>
        <EmployeeCard
          v-for="employee in employees"
          :key="employee.id"
          :name="employee.name"
          :score="employee.score"
          :rating="employee.rating"
          :avatar="employee.avatar"
        />
      </section>
    </main>

    <!-- Подвал (необязательно) -->
    <footer v-if="showFooter" class="footer">
      <p>MyApp &copy; 2024. All Rights Reserved.</p>
    </footer>
  </div>
</template>

<script>
import EmployeeCard from './components/EmployeeCard.vue';
import StoreList from './components/StoreList.vue';

export default {
  components: { EmployeeCard, StoreList },
  data() {
    return {
      employees: [
        { id: 1, name: 'Bob Smith', score: '92%', rating: '9/10', avatar: 'cat1.jpg' },
        { id: 2, name: 'Jane Doe', score: '98%', rating: '10/10', avatar: 'cat2.jpg' },
        { id: 3, name: 'John Johnson', score: '80%', rating: '8/10', avatar: 'cat3.jpg' }
      ],
      stores: ['Downtown Store', 'Uptown Store', 'Midtown Store', 'Westside Store', 'Eastside Store'],
      showFooter: true
    };
  },
  methods: {
    goTo(page) {
      console.log(`Navigating to ${page}`);
    }
  }
};
</script>

<style>
/* Общие стили */
#app {
  font-family: Arial, sans-serif;
  color: #f0f0f0;
  background-color: #121212;
  max-width: 1200px;
  margin: 0 auto;
}

/* Навигация */
.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #1e1e1e;
  padding: 15px 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
}

.navigation .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.navigation .nav-buttons button {
  margin-left: 10px;
  padding: 10px 15px;
  background-color: #333;
  border: none;
  border-radius: 5px;
  color: #f0f0f0;
  cursor: pointer;
}

.navigation .nav-buttons button:hover {
  background-color: #555;
}

/* Dashboard */
.dashboard {
  padding: 20px;
}

.search-bar input {
  padding: 10px;
  width: 100%;
  border: none;
  border-radius: 5px;
  background-color: #333;
  color: #f0f0f0;
  margin-bottom: 20px;
}

.store-list-section,
.employee-list-section {
  margin-bottom: 40px;
}

.store-list-section h2,
.employee-list-section h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  border-bottom: 1px solid #555;
  padding-bottom: 5px;
}

/* Подвал */
.footer {
  text-align: center;
  padding: 10px 0;
  background-color: #1e1e1e;
  color: #aaa;
}
</style>
