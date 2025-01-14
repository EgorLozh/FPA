<template>
  <section class="dashboard">
    <h2>Department Rankings</h2>
    <div class="search-section">
      <SearchInput
        v-model="searchQuery"
        placeholder="Search departments by name..."
        @input="filterDepartments"
      />
    </div>
    <transition-group name="fade" tag="div">
      <DepartmentList 
        :departments="filteredDepartments" 
        @selectDepartment="selectDepartment"
      />
    </transition-group>
  </section>
</template>

<script>
import SearchInput from './SearchInput.vue';
import DepartmentList from './DepartmentList.vue';

export default {
  components: { 
    SearchInput,
    DepartmentList, 
  },
  props: {
    departments: { // Принимаем отделы из API
      type: Array,
      required: true,
      default: () => [], // Инициализируем пустым массивом по умолчанию
    },
  },
  data() {
    return {
      searchQuery: "",
      filteredDepartments: [], // Инициализируем пустым массивом
      selectedDepartment: null,
    };
  },
  watch: {
    // Обновляем filteredDepartments при изменении departments
    departments: {
      immediate: true, // Выполнить сразу при создании компонента
      handler(newDepartments) {
        this.filteredDepartments = newDepartments || [];
      },
    },
  },
  methods: {
    filterDepartments() {
      const query = this.searchQuery.toLowerCase();
      this.filteredDepartments = (this.departments || []).filter((department) =>
        department.name.toLowerCase().includes(query)
      );
    },
    selectDepartment(department) {
      this.selectedDepartment = department;
    },
  },
};
</script>

<style>
.dashboard {
  max-width: 100%;
  width: 90%;
  padding: 20px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
}

.search-section {
  max-width: 800px;
  margin: 0 auto 20px;
  padding: 0 20px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>