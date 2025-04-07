<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-section">
        <h3>Bird-Yard:</h3>
        <p>我们致力于帮助您打造安全、健康的鸟类友好型后院，为鸟类提供真正的家园。</p>
      </div>

      <div class="footer-section">
        <h3>快速链接</h3>
        <ul>
          <li><a href="#">本地植物指南</a></li>
          <li><a href="#">鸟类吸引技巧</a></li>
          <li><a href="#">可持续花园设计</a></li>
          <li><a href="#">季节性维护提示</a></li>
        </ul>
      </div>

      <div class="footer-section">
        <h3>联系我们</h3>
        <p><a href="mailto:info@bird-yard.com">info@bird-yard.com</a></p>
        <p>电话: 400-123-4567</p>
      </div>

      <div class="footer-section">
        <h3>常见问题</h3>
        <ul>
          <li><a href="#">如何选择适合的植物</a></li>
          <li><a href="#">鸟类栖息地设计</a></li>
          <li><a href="#">自然花园护理</a></li>
          <li><a href="#">授粉者花园</a></li>
        </ul>
      </div>

      <div class="footer-section">
        <h3>关注我们</h3>
        <div class="social-links">
          <a href="#" aria-label="微信"><i class="fab fa-weixin"></i></a>
          <a href="#" aria-label="微博"><i class="fab fa-weibo"></i></a>
          <a href="#" aria-label="抖音"><i class="fab fa-tiktok"></i></a>
        </div>
      </div>
    </div>
    <div class="copyright">
      <p>&copy; {{ currentYear }} Bird-Yard 鸟园花境. 版权所有.</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'BFooter',
  computed: {
    currentYear() {
      return new Date().getFullYear()
    },
  },
}
</script>

<style scoped>
.footer {
  background-color: #0a3200;
  color: #ffffff;
  padding: 40px 0 20px;
}

.footer-container {
  max-width: 1400px;
  width: 90%;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.footer-section {
  flex: 1 1 200px;
  margin-bottom: 30px;
  padding: 0 15px;
}

.footer-section h3 {
  color: #c2e59c;
  margin-bottom: 15px;
  font-size: 1.2rem;
  font-weight: 600;
}

.footer-section p {
  font-size: 0.9rem;
  line-height: 1.6;
}

.footer-section ul {
  list-style: none;
  padding: 0;
}

.footer-section ul li {
  margin-bottom: 8px;
}

.footer-section a {
  color: #ffffff;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.3s ease;
}

.footer-section a:hover {
  color: #c2e59c;
}

.social-links {
  display: flex;
  gap: 15px;
}

.social-links a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background-color: rgba(194, 229, 156, 0.2);
  transition: background-color 0.3s ease;
}

.social-links a:hover {
  background-color: rgba(194, 229, 156, 0.4);
}

.copyright {
  text-align: center;
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid rgba(194, 229, 156, 0.2);
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .footer-container {
    flex-direction: column;
  }

  .footer-section {
    margin-bottom: 25px;
    text-align: center;
    flex: 1 1 100%;
  }

  .social-links {
    justify-content: center;
  }
}
</style>
