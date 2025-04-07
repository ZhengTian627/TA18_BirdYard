<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    background-image:
      linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('@/assets/images/homepage.jpeg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    justify-content: center;
    text-align: center;
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
