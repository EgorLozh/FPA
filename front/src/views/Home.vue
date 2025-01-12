<template>
  <div class="home-container">
    <h1>Welcome to the App</h1>
    <button @click="navigateTo('Dashboard')" class="button">Go to Dashboard</button>
    <button @click="navigateTo('EmployeeRating')" class="button">Go to Employee Rating</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    navigateTo(routeName) {
      this.$router.push({ name: routeName });
    }
  }
};
</script>

<style>
.home-container {
  padding: 20px;
  text-align: center;
}

.button {
  margin: 10px;
}
</style>
