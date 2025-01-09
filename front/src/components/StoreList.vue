<template>
  <div>
    <ul class="store-list">
      <li 
        v-for="store in stores" 
        :key="store.id" 
        class="store-card"
      >
        <details @toggle="handleSelectStore(store)">
          <summary>{{ store.name }}</summary>
          <ul class="employee-list">
            <EmployeeCard
              v-for="employee in store.employees"
              :key="employee.id"
              :name="employee.name"
              :score="employee.score"
              :rating="employee.rating"
              :avatar="employee.avatar"
              :storeName="store.name"
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
      required: true,
    },
  },
  methods: {
    handleSelectStore(store) {
      this.$emit("selectStore", store);
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
