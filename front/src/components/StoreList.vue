<template>
  <div>
    <ul class="store-list">
      <li 
        v-for="store in stores" 
        :key="store.id" 
        class="store-card"
      >
        <details @toggle="handleToggle(store)">
          <summary>{{ store.name }}</summary>
        </details>
        <transition 
          name="slide-fade" 
          @before-enter="handleBeforeEnter" 
          @enter="handleEnter" 
          @leave="handleLeave" 
          @after-enter="handleAfterEnter(store)" 
          @after-leave="handleAfterLeave(store)"
        >
          <ul v-if="store.open" class="employee-list">
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
        </transition>
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
    handleToggle(store) {
      store.open = !store.open;
      this.$emit("toggleStore", store);
    },
    handleBeforeEnter(el) {
      console.log('Before enter:', el);
    },
    handleEnter(el, done) {
      console.log('Enter:', el);
      done();
    },
    handleLeave(el, done) {
      console.log('Leave:', el);
      done();
    },
    handleAfterEnter(store) {
      this.$emit("afterEnter", store);
    },
    handleAfterLeave(store) {
      this.$emit("afterLeave", store);
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
  position: relative;
}

.slide-fade-enter-active {
  transition: all 0.5s ease;
}
.slide-fade-leave-active {
  transition: all 0.5s ease;
}
.slide-fade-enter, .slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>
