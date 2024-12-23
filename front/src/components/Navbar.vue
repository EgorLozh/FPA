<template>
    <nav class="navbar">
      <div class="logo">Logo</div>
      <ul class="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
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
    padding: 10px 20px;
    background-color: #333;
    color: #fff;
    position: sticky;
    top: 0;
    z-index: 1000;
  }
  
  .nav-links {
    list-style: none;
    display: flex;
    gap: 20px;
    flex-grow: 1;
  }
  
  .nav-links a {
    color: white;
    text-decoration: none;
  }
  
  .actions button {
    margin-left: 10px;
    padding: 5px 10px;
    background-color: #444;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
  