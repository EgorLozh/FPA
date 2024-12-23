<template>
  <div id="app">
    <!-- Заголовок -->
    <header>
      <h1>Dashboard</h1>
      <input type="text" placeholder="Search employees..." />
    </header>

    <!-- Список сотрудников -->
    <section>
      <EmployeeCard
        v-for="employee in employees"
        :key="employee.id"
        :name="employee.name"
        :score="employee.score"
        :rating="employee.rating"
        :avatar="employee.avatar"
      />
    </section>

    <!-- Список магазинов -->
    <section>
      <h2>Stores</h2>
      <StoreList :stores="stores" />
    </section>
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
      stores: ['Downtown Store', 'Uptown Store', 'Midtown Store', 'Westside Store', 'Eastside Store']
    };
  }
};
</script>

<style>
/* Общие стили */
#app {
  font-family: Arial, sans-serif;
  color: #f0f0f0; /* Светлый текст для контраста */
  background-color: #121212; /* Тёмный фон */
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto; /* Центрирование всего контента */
}

/* Шапка с заголовком и поиском */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

h1 {
  font-size: 2rem;
  margin: 0;
}

input {
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #333;
  color: #f0f0f0;
  width: 300px;
}

input::placeholder {
  color: #aaa;
}

/* Секция сотрудников */
section {
  margin-bottom: 40px;
}

section h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  border-bottom: 1px solid #555;
  padding-bottom: 5px;
}

/* Карточки сотрудников */
.employee-card {
  display: flex;
  align-items: center;
  background-color: #1e1e1e;
  border-radius: 10px;
  padding: 15px;
  margin-bottom: 15px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
}

.employee-card img {
  border-radius: 50%;
  width: 50px;
  height: 50px;
  margin-right: 15px;
}

/* Список магазинов */
.store-list {
  background-color: #1e1e1e;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
}

.store-list ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.store-list li {
  padding: 10px 0;
  border-bottom: 1px solid #333;
  display: flex;
  justify-content: space-between;
}

.store-list li:last-child {
  border-bottom: none;
}

.store-list li:hover {
  color: #00c6ff;
  cursor: pointer;
}
</style>