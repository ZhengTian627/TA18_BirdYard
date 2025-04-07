<template>
  <div class="contact">
    <!-- 标题区域 -->
    <section class="hero">
      <div class="container">
        <h1>Contact Us</h1>
        <p>We're here to help you create your bird-friendly backyard paradise</p>
      </div>
    </section>

    <!-- 主要内容区域 -->
    <section class="content">
      <div class="container">
        <div class="contact-grid">
          <!-- 左侧：联系表单 -->
          <div class="contact-form">
            <h2>Get In Touch</h2>
            <form @submit.prevent="submitForm">
              <div class="form-group">
                <label for="name">Your Name</label>
                <input type="text" id="name" v-model="form.name" required />
              </div>

              <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" v-model="form.email" required />
              </div>

              <div class="form-group">
                <label for="subject">Subject</label>
                <input type="text" id="subject" v-model="form.subject" required />
              </div>

              <div class="form-group">
                <label for="message">Your Message</label>
                <textarea id="message" rows="5" v-model="form.message" required></textarea>
              </div>

              <button type="submit" class="submit-button">Send Message</button>
            </form>
          </div>

          <!-- 右侧：联系信息 -->
          <div class="contact-info">
            <h2>Contact Information</h2>

            <div class="info-item">
              <h3>Email</h3>
              <p><a href="mailto:info@bird-yard.com">info@bird-yard.com</a></p>
            </div>

            <div class="info-item">
              <h3>Location</h3>
              <p>123 Garden Way<br />Birdsville, CA 94123</p>
            </div>

            <div class="info-item">
              <h3>Hours</h3>
              <p>Monday to Friday: 9am - 5pm<br />Saturday: 10am - 3pm<br />Sunday: Closed</p>
            </div>

            <div class="social-links">
              <h3>Follow Us</h3>
              <div class="social-icons">
                <a href="#" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 地图部分 -->
    <section class="map-section">
      <div class="map-placeholder">
        <!-- 这里可以放置实际的地图组件或图片 -->
        <img src="@/assets/images/map-placeholder.jpg" alt="Our Location Map" />
      </div>
    </section>
  </div>
</template>
<script>
export default {
  name: 'ContactUs',
  data() {
    return {
      form: {
        name: '',
        email: '',
        subject: '',
        message: '',
      },
      formSubmitted: false,
    }
  },
  methods: {
    submitForm() {
      // 这里添加表单提交逻辑
      console.log('Form submitted:', this.form)
      this.formSubmitted = true

      // 清空表单
      this.form = {
        name: '',
        email: '',
        subject: '',
        message: '',
      }

      // 显示成功消息（在实际应用中可以使用更好的UI反馈）
      alert('Your message has been sent. We will contact you soon!')
    },
  },
}
</script>
<style scoped>
.contact {
  padding-top: 0; /* 为固定头部留出空间 */
}

.hero {
  background-color: var(--color-primary);
  color: white;
  padding: 60px 0;
  text-align: center;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hero p {
  font-size: 1.2rem;
  max-width: 600px;
  margin: 0 auto;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.content {
  padding: 80px 0;
  background-color: var(--color-bg-light);
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 50px;
}

/* 表单样式 */
.contact-form h2,
.contact-info h2 {
  color: var(--color-primary);
  margin-bottom: 25px;
  font-size: 1.8rem;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
  color: var(--color-text);
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: var(--color-primary);
  outline: none;
}

.submit-button {
  background-color: var(--color-primary);
  color: white;
  border: none;
  padding: 12px 25px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #072500;
}

/* 联系信息样式 */
.contact-info {
  background-color: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}

.info-item {
  margin-bottom: 25px;
}

.info-item h3 {
  color: var(--color-primary);
  font-size: 1.2rem;
  margin-bottom: 5px;
}

.info-item p {
  color: var(--color-text);
  line-height: 1.6;
}

.info-item a {
  color: var(--color-primary);
  text-decoration: none;
}

.info-item a:hover {
  text-decoration: underline;
}

.social-links h3 {
  color: var(--color-primary);
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.social-icons {
  display: flex;
  gap: 15px;
}

.social-icons a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background-color: #f5f5f5;
  color: var(--color-primary);
  border-radius: 50%;
  transition: all 0.3s;
}

.social-icons a:hover {
  background-color: var(--color-primary);
  color: white;
}

/* 地图部分 */
.map-section {
  height: 90%;
  background-color: #e9e9e9;
}

.map-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.map-placeholder img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 响应式设计 */
@media (max-width: 992px) {
  .contact-grid {
    grid-template-columns: 1fr;
  }

  .contact-info {
    order: -1; /* 在移动设备上将联系信息放在表单之前 */
  }
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.5rem;
  }

  .hero p {
    font-size: 1rem;
  }

  .map-section {
    height: 300px;
  }
}
</style>
