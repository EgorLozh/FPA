<template>
  <section class="dashboard">
    <h2>Store Rankings</h2>
    <div class="search-section">
      <SearchInput
        v-model="searchQuery"
        placeholder="Search stores by name..."
        @input="filterStores"
      />
    </div>
    <transition-group name="fade" tag="div">
      <StoreList 
        :stores="filteredStores" 
        @selectStore="selectStore"
      />
    </transition-group>
  </section>
</template>

<script>
import SearchInput from './SearchInput.vue';
import StoreList from './StoreList.vue';
import EmployeeCard from './EmployeeCard.vue';

export default {
  components: { 
    SearchInput,
    StoreList, 
    EmployeeCard 
  },
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
  computed: {
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
  max-width: 100%; /* Change this to a larger value */
  width: 90%; /* Add this line to set a specific width */
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin: 0 auto; /* Центрирование дашборда */
}

/* Удалить старые стили поиска, так как они больше не нужны */
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

.search-section {
  max-width: 800px;
  margin: 0 auto 20px;
  padding: 0 20px;
}

.employee-card {
  margin-bottom: 20px; /* Add this line to add space between employee cards */
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
