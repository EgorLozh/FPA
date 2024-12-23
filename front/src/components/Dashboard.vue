<template>
  <section class="dashboard">
    <div class="search-bar">
      <input type="text" placeholder="Search stores..." />
    </div>
    <h2>Store Rankings</h2>
    <StoreList :stores="stores" />
  </section>
</template>

<script>
import StoreList from './StoreList.vue';

export default {
  components: { StoreList },
  props: {
    stores: Array,
  },
};
</script>

<style>
.dashboard {
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.search-bar input {
  width: 100%;
  padding: 8px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
