<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-section">
        <h3>Bird-Yard</h3>
        <p>Creating safe, healthy, bird-friendly backyards - one garden at a time.</p>
      </div>

      <div class="footer-section">
        <h3>Resources</h3>
        <ul>
          <li><a href="#">Native Plants Guide</a></li>
          <li><a href="#">Bird Identification</a></li>
          <li><a href="#">Seasonal Garden Tips</a></li>
          <li><a href="#">DIY Bird Feeders</a></li>
        </ul>
      </div>

      <div class="footer-section">
        <h3>Contact Us</h3>
        <p><a href="mailto:info@bird-yard.com">info@bird-yard.com</a></p>
        <p>123 Garden Way, Birdsville</p>
      </div>

      <div class="footer-section">
        <h3>Learn More</h3>
        <ul>
          <li><a href="#">About Bird-Yard</a></li>
          <li><a href="#">4-Step Garden Plan</a></li>
          <li><a href="#">Habitat Creation</a></li>
          <li><a href="#">Success Stories</a></li>
        </ul>
      </div>

      <div class="footer-section">
        <h3>Follow Us</h3>
        <div class="social-links">
          <a href="#" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
          <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
          <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
        </div>
      </div>
    </div>
    <div class="copyright">
      <p>
        &copy; {{ currentYear }} Bird-Yard. All rights reserved. Where plants take roots, birds find
        home.
      </p>
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
  color: #ffffff;
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
  text-decoration: underline;
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
  background-color: rgba(255, 255, 255, 0.1);
  transition: background-color 0.3s ease;
}

.social-links a:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.copyright {
  text-align: center;
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
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
