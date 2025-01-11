<template>
  <nav class="navbar">
    <div class="logo">ScriptTracker</div>
    <ul class="nav-links">
      <li><router-link to="/dashboard">Dashboard</router-link></li>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/employee-rating">Employee Rating</router-link></li>
    </ul>
    <div class="actions">
      <button @click="login">Login</button>
      <button @click="newMessage">New Message</button>
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
}

.logo {
  flex-grow: 1;
  font-size: 24px; /* Increased font size */
}

.actions {
  flex-grow: 1;
  display: flex;
  justify-content: flex-end;
}

.actions button {
  margin-left: 15px; /* Increased margin */
  padding: 10px 15px; /* Increased padding */
  background-color: var(--vt-c-white-soft);
  color: var(--vt-c-black);
  border: none;
  cursor: pointer;
  font-size: 16px; /* Increased font size */
  transition: background-color 0.3s, transform 0.3s;
}

.actions button:active {
  transform: scale(0.95);
}
</style>
