<template>
  <transition name="modal-fade">
    <div v-if="show" class="modal-overlay" @click="close">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>Select Employee</h3>
          <button class="close-button" @click="close">&times;</button>
        </div>

        <div class="search-controls">
          <SearchInput
            v-model="searchQuery"
            placeholder="Search employees..."
            @input="filterWorkers"
          />
          <div class="sort-controls">
            <select v-model="sortKey" @change="sortWorkers" class="button">
              <option value="name">Name</option>
            </select>
            <button @click="toggleSortOrder" class="button">
              {{ sortOrder === 'asc' ? 'Ascending' : 'Descending' }}
            </button>
          </div>
        </div>

        <div class="workers-list">
          <template v-if="filteredWorkers.length > 0">
            <EmployeeCard
              v-for="worker in filteredWorkers"
              :key="worker.id"
              :id="worker.id"
              :name="worker.name"
              :departmentId="worker.department_id"
              @click="selectWorker(worker)"
            />
          </template>
          <div v-else class="no-results">No workers found.</div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import SearchInput from "./SearchInput.vue";
import EmployeeCard from "./EmployeeCard.vue";

export default {
  name: "EmployeeSearchModal",
  components: { SearchInput, EmployeeCard },
  props: {
    show: Boolean,
    workers: { // Исправлено на workers
      type: Array,
      default: () => [],
    },
    departments: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      searchQuery: "",
      sortKey: "name",
      sortOrder: "asc",
      filteredWorkers: [], // Исправлено на workers
    };
  },
  watch: {
    show(newVal) {
      if (newVal) {
        this.filteredWorkers = [...this.workers]; // Исправлено на workers
        this.sortWorkers(); // Исправлено на workers
      }
    },
    workers: { // Исправлено на workers
      immediate: true,
      handler(newWorkers) { // Исправлено на workers
        console.log("Workers:", newWorkers);
        if (Array.isArray(newWorkers)) {
          this.filteredWorkers = [...newWorkers]; // Исправлено на workers
          this.sortWorkers(); // Исправлено на workers
        } else {
          this.filteredWorkers = []; // Исправлено на workers
        }
      },
    },
  },
  methods: {
    close() {
      this.$emit("close");
    },
    selectWorker(worker) { // Исправлено на workers
      this.$emit("select", worker);
      this.close();
    },
    filterWorkers() { // Исправлено на workers
      const query = this.searchQuery.toLowerCase();
      this.filteredWorkers = this.workers.filter((worker) => // Исправлено на workers
        worker.name.toLowerCase().includes(query)
      );
      this.sortWorkers(); // Исправлено на workers
    },
    sortWorkers() { // Исправлено на workers
      this.filteredWorkers.sort((a, b) => { // Исправлено на workers
        let result = a.name.localeCompare(b.name);
        return this.sortOrder === "asc" ? result : -result;
      });
    },
    toggleSortOrder() {
      this.sortOrder = this.sortOrder === "asc" ? "desc" : "asc";
      this.sortWorkers(); // Исправлено на workers
    },
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 8px;
  width: 90%;
  max-width: 600px;
  max-height: 80vh;
  display: flex;
  flex-direction: column;
  transform-origin: top;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  border-bottom: 1px solid #eee;
}

.close-button {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.search-controls {
  padding: 15px;
  border-bottom: 1px solid #eee;
}

.sort-controls {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.workers-list {
  overflow-y: auto;
  padding: 15px;
}

.no-results {
  text-align: center;
  color: #666;
  padding: 20px;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.modal-fade-enter-to,
.modal-fade-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>