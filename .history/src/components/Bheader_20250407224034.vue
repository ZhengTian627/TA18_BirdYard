<template>
  <header class="header">
    <div class="container">
      <div class="logo">
        <router-link to="/">
          <img src="@/assets/images/logo.png" alt="Bird-Yard Logo" />
          <span>BirdYard</span>
        </router-link>
      </div>
      <nav class="nav-menu">
        <ul>
          <li><router-link to="/">HOME</router-link></li>
          <li><router-link to="/about">ABOUT US</router-link></li>
          <li><router-link to="/contact">CONTACT US</router-link></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: 'BHeader',
}
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 20px 0;
  z-index: 1000;
  background-color: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(5px);
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1400px;
  width: 90%;
  margin: 0 auto;
  padding: 0 20px;
}

.logo a {
  display: flex;
  align-items: center;
  color: #ffffff;
  font-size: 24px;
  font-weight: bold;
  text-decoration: none;
}

.logo img {
  height: 40px;
  margin-right: 10px;
}

.nav-menu ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-menu li {
  margin-left: 30px;
}

.nav-menu a {
  color: #ffffff;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
  transition: color 0.3s ease;
}

.nav-menu a:hover {
  color: #c2e59c;
}

@media (max-width: 768px) {
  .container {
    flex-direction: column;
    align-items: center;
  }

  .nav-menu {
    margin-top: 15px;
  }

  .nav-menu ul {
    flex-direction: column;
    align-items: center;
  }

  .nav-menu li {
    margin: 10px 0;
    margin-left: 0;
  }
}
</style>
