<template>
  <div>
    <ul class="store-list">
      <li v-for="store in stores" :key="store.id">
        <details>
          <summary>{{ store.name }}</summary>
          <ul>
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
    stores: Array,
  },
};
</script>

<style>
.store-list {
  list-style: none;
  padding: 0;
}

.store-list details {
  margin-bottom: 10px;
}

.store-list summary {
  cursor: pointer;
  font-weight: bold;
}
</style>
