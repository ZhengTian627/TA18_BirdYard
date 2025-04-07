<script setup>
import { RouterView } from 'vue-router'
import BHeader from './components/Bheader.vue'
import BFooter from './components/BFooter.vue'
</script>

<template>
  <div class="app">
    <BHeader />
    <main>
      <RouterView />
    </main>
    <BFooter />
  </div>
</template>

<style>
/* Global styles */
:root {
  --color-primary: #0a3200;
  --color-secondary: #c2e59c;
  --color-text: #333333;
  --color-light: #ffffff;
  --color-bg-light: #f9f9f9;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  overflow-x: hidden;
}

body {
  margin: 0;
  padding: 0;
  width: 100%;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  color: var(--color-text);
}

.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
}

main {
  flex: 1;
  width: 100%;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: 700;
  line-height: 1.2;
}

a {
  text-decoration: none;
}

img {
  max-width: 100%;
  height: auto;
}
</style>
