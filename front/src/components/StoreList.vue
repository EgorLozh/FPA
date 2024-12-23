<template>
  <div class="store-list">
    <ul>
      <li v-for="(store, index) in stores" :key="index">
        {{ store }}
        <span>&gt;</span>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  stores: Array,
});
</script>

<style scoped>
.store-list {
  list-style: none;
  padding: 0;
}

.store-list li {
  padding: 8px 0;
  border-bottom: 1px solid #eee;
  cursor: pointer;
}

.store-list li:hover {
  color: #007bff;
}
</style>
