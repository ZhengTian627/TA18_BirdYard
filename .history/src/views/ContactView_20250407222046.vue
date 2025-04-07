<template>
  <div class="debug-container">
    <div class="debug-box left">左侧边界</div>
    <div class="debug-box center">中心区域</div>
    <div class="debug-box right">右侧边界</div>
  </div>
</template>

<script>
export default {
  name: 'DebugLayout',
}
</script>

<style>
.debug-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  z-index: 9999;
  pointer-events: none;
}

.debug-box {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  color: white;
  text-shadow: 0 0 2px black;
}

.left {
  width: 50px;
  background-color: rgba(255, 0, 0, 0.2);
}

.center {
  flex: 1;
  background-color: rgba(0, 0, 255, 0.1);
}

.right {
  width: 50px;
  background-color: rgba(0, 255, 0, 0.2);
}
</style>
