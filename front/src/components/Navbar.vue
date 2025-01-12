<template>
  <nav class="navbar">
    <router-link to="/" class="logo">ScriptTracker</router-link> <!-- Changed div to router-link -->
    <ul class="nav-links">
      <li><router-link to="/dashboard">Dashboard</router-link></li>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/employee-rating">Employee Rating</router-link></li>
    </ul>
    <div class="actions">
      <button @click="login" class="button">Login</button>
      <button @click="newMessage" class="button">New Message</button>
    </div>
  </nav>
</template>

<script>
export default {
  methods: {
    login() {
      console.log('Login clicked');
    },
    newMessage() {
      console.log('New Message clicked');
    },
  },
};
</script>

<style>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px; /* Increased padding */
  background-color: var(--vt-c-white);
  color: var(--vt-c-black);
  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: #ffffff; /* Added background color */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Added shadow */
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 30px; /* Increased gap between links */
  flex-grow: 1;
  justify-content: center;
}

.nav-links a {
  color: var(--vt-c-black);
  text-decoration: none;
  font-size: 18px; /* Increased font size */
  transition: color 0.3s, transform 0.3s; /* Added transition for animation */
}

.nav-links a:hover {
  color: #2193f2; /* Added highlight color */
  transform: scale(1.1); /* Added scale effect */
}

.logo {
  flex-grow: 1;
  font-size: 24px; /* Increased font size */
  transition: color 0.3s, transform 0.3s; /* Added transition for animation */
  color: var(--vt-c-black);
  text-decoration: none;
}

.logo:hover {
  color: #2193f2; /* Added highlight color */
  transform: scale(1.1); /* Added scale effect */
}

.logo:active {
  transform: scale(0.95); /* Added click effect */
}

.actions {
  flex-grow: 1;
  display: flex;
  justify-content: flex-end;
}

.button {
  background-color: #2193f2;
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin: 10px;
  transition: background-color 0.3s, transform 0.3s;
}

.button:active {
  transform: scale(0.95);
}
</style>
