<template>
  <div>
    <ul class="store-list">
      <li v-for="store in stores" :key="store.id" class="store-card">
        <details>
          <summary>{{ store.name }}</summary>
          <ul class="employee-list">
            <EmployeeCard
              v-for="employee in store.employees"
              :key="employee.id"
              v-bind="employee"
            />
          </ul>
        </details>
      </li>
    </ul>
  </div>
</template>

<script>
import EmployeeCard from './EmployeeCard.vue';

export default {
  components: { EmployeeCard },
  props: {
    stores: {
      type: Array,
      default: () => [
        {
          id: 1,
          name: "Downtown Store",
          employees: [
            { id: 1, name: "Bob Smith", score: 92, rating: 9, avatar: "path/to/avatar1.jpg" },
            { id: 2, name: "Jane Doe", score: 98, rating: 10, avatar: "path/to/avatar2.jpg" },
          ],
        },
        {
          id: 2,
          name: "Uptown Store",
          employees: [
            { id: 3, name: "John Johnson", score: 80, rating: 8, avatar: "path/to/avatar3.jpg" },
            { id: 4, name: "Alice Brown", score: 85, rating: 8, avatar: "path/to/avatar4.jpg" },
          ],
        },
        // Add more stores with placeholder employees as needed
      ],
    },
  },
};
</script>

<style>
.store-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.store-card {
  width: 80%;
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background: #fff;
}

.store-card details {
  width: 100%;
}

.store-card summary {
  cursor: pointer;
  font-weight: bold;
  text-align: center;
}

.employee-list {
  list-style: none;
  padding: 0;
  margin-top: 10px;
}
</style>
