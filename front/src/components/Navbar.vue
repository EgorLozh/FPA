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
        transform: 'translateX(0px)',
        opacity: '0'
      }
    }
  },
  methods: {
    login() {
      this.$router.push('/login');
    },
    newMessage() {
      this.$router.push('/new-report');
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
    window.addEventListener('resize', this.updateHighlight);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateHighlight);
  }
};
</script>

<style>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px;
  background-color: var(--vt-c-white);
  color: var(--vt-c-black);
  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: #ffffff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.nav-links {
  position: relative;
  list-style: none;
  display: flex;
  gap: 30px;
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
  font-size: 18px;
  transition: color 0.3s, transform 0.3s;
  padding: 8px 16px;
  border-radius: 4px;
  display: block;
}

.nav-links a:hover {
  color: #2193f2;
  transform: scale(1.1);
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
  font-size: 24px;
  transition: color 0.3s, transform 0.3s;
  color: var(--vt-c-black) !important;
  text-decoration: none;
}

.logo:hover {
  color: #2193f2;
  transform: scale(1.1);
}

.logo:active {
  transform: scale(0.95);
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