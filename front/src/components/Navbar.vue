<template>
  <nav class="navbar">
    <router-link to="/" class="logo">ScriptTracker</router-link>
    <ul class="nav-links">
      <div class="nav-highlight" :style="highlightStyle"></div>
      <li v-for="(link, index) in links" :key="index" :ref="el => updateLinkRefs(el, index)">
        <router-link :to="link.path">{{ link.name }}</router-link>
      </li>
    </ul>
    <div class="actions">
      <button @click="login" class="button">Login</button>
      <button @click="newMessage" class="button">New Message</button>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      links: [
        { path: '/dashboard', name: 'Dashboard' },
        { path: '/', name: 'Home' },
        { path: '/employee-rating', name: 'Employee Rating' }
      ],
      linkRefs: [],
      highlightStyle: {
        width: '0px',
        transform: 'translateX(0px)'
      }
    }
  },
  methods: {
    login() {
      console.log('Login clicked');
    },
    newMessage() {
      console.log('New Message clicked');
    },
    updateLinkRefs(el, index) {
      if (el) this.linkRefs[index] = el;
    },
    updateHighlight() {
      const activeLink = this.linkRefs.find(link => 
        link?.querySelector('.router-link-active')
      );
      
      if (activeLink) {
        const linkRect = activeLink.getBoundingClientRect();
        const navLinksRect = activeLink.closest('.nav-links').getBoundingClientRect();
        
        this.highlightStyle = {
          width: `${linkRect.width}px`,
          transform: `translateX(${linkRect.left - navLinksRect.left}px)`,
          opacity: '1'
        };
      } else {
        // Hide highlight when not on main navigation pages
        this.highlightStyle = {
          width: '0px',
          transform: 'translateX(0px)',
          opacity: '0'
        };
      }
    }
  },
  watch: {
    $route() {
      this.$nextTick(() => {
        this.updateHighlight();
      });
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.updateHighlight();
    });
  }
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
  position: relative;
  list-style: none;
  display: flex;
  gap: 30px; /* Increased gap between links */
  flex-grow: 1;
  justify-content: center;
  padding: 0 20px;
}

.nav-highlight {
  position: absolute;
  height: 100%;
  background-color: #2193f2;
  border-radius: 4px;
  top: 0;
  left: 0;
  z-index: 0;
  opacity: 0;
  pointer-events: none;
  transition: all 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.nav-links a {
  position: relative;
  z-index: 1;
  color: var(--vt-c-black);
  text-decoration: none;
  font-size: 18px; /* Increased font size */
  transition: color 0.3s, transform 0.3s; /* Added transition for animation */
  padding: 8px 16px;
  border-radius: 4px;
  display: block;
}

.nav-links a:hover {
  color: #2193f2; /* Added highlight color */
  transform: scale(1.1); /* Added scale effect */
}

.router-link-active:not(.logo) {
  background-color: transparent;
  color: white !important;
}

.logo.router-link-active {
  background-color: transparent;
  color: var(--vt-c-black);
}

.logo {
  flex-grow: 1;
  font-size: 24px; /* Increased font size */
  transition: color 0.3s, transform 0.3s; /* Added transition for animation */
  color: var(--vt-c-black) !important; /* Добавил !important */
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
