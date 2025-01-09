<template>
  <section class="dashboard">
    <!-- Поиск магазинов -->
    <div class="search-bar">
      <input 
        type="text" 
        v-model="searchQuery" 
        placeholder="Search stores..." 
        @input="filterStores" 
      />
    </div>
    <h2>Store Rankings</h2>
    <StoreList 
      :stores="filteredStores" 
      @selectStore="selectStore"
    />
  </section>
</template>

<script>
import StoreList from './StoreList.vue';

export default {
  components: { StoreList },
  props: {
    stores: Array,
    employees: Array,
  },
  data() {
    return {
      searchQuery: "", // Поиск по магазинам
      filteredStores: this.stores,
      selectedStore: null,
    };
  },
  methods: {
    filterStores() {
      const query = this.searchQuery.toLowerCase();
      this.filteredStores = this.stores.filter((store) =>
        store.name.toLowerCase().includes(query)
      );
    },
    selectStore(store) {
      this.selectedStore = store;
    },
  },
};
</script>

<style>
.dashboard {
  max-width: 80%;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin: 0 auto; /* Центрирование дашборда */
}

.search-bar {
  max-width: 100%;
  display: flex;
  justify-content: center;
}

.search-bar input {
  width: 80%;
  padding: 8px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
