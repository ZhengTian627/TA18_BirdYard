<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-section">
        <h3>UV SAFE:</h3>
        <p>A go-to platform for sun protection awareness and personalised recommendations.</p>
      </div>

      <div class="footer-section">
        <h3>Links Support</h3>
        <ul>
          <li><a href="#">UV Impacts</a></li>
          <li><a href="#">Safety Alert</a></li>
          <li><a href="#">My UV-Shield</a></li>
          <li><a href="#">Safety Plan</a></li>
        </ul>
      </div>

      <div class="footer-section">
        <h3>Contact Us</h3>
        <p><a href="mailto:info@uv-safe.com.au">info@uv-safe.com.au</a></p>
      </div>

      <div class="footer-section">
        <h3>FAQ</h3>
        <ul>
          <li><a href="#">About Bird-Yard</a></li>
          <li><a href="#">Plant Selection</a></li>
          <li><a href="#">Garden Care</a></li>
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
      <p>&copy; {{ currentYear }} Bird-Yard. All rights reserved.</p>
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
  background-color: #3c7047;
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
