<template>
  <div class="contact-section" :style="backgroundStyle">
    <div class="contact-container">
      <h2 class="contact-title">{{ title }}</h2>

      <p class="contact-description">{{ description }}</p>

      <div class="features-list">
        <div v-for="(feature, index) in features" :key="index" class="feature-item">
          <span class="feature-icon">✓</span>
          <span class="feature-text">{{ feature }}</span>
        </div>
      </div>

      <div class="subscription-form">
        <input
          type="email"
          v-model="email"
          :placeholder="emailPlaceholder"
          class="email-input"
          @input="validateEmail"
        />
        <button
          class="subscribe-button"
          @click="subscribe"
          :disabled="!isValidEmail || isSubmitting"
        >
          {{ subscribeButtonText }}
        </button>
      </div>

      <div v-if="formMessage" :class="['form-message', formMessageType]">
        {{ formMessage }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactSection',
  props: {
    backgroundImage: {
      type: String,
      default: '/images/garden-background.jpg',
    },
    title: {
      type: String,
      default: 'Your Garden Needs A Bit Of Love? Contact Us Now!',
    },
    description: {
      type: String,
      default:
        'Discover the beauty of Garden Tree – where every seed planted is a step towards a greener, more vibrant future.',
    },
    features: {
      type: Array,
      default: () => [
        'Sustainable Gardening Consultation',
        'Eco-Friendly Landscaping Services',
        'Organic Soil and Fertilizer Subscription Box',
      ],
    },
    emailPlaceholder: {
      type: String,
      default: 'Your email address',
    },
    subscribeButtonText: {
      type: String,
      default: 'Subscribe',
    },
  },
  data() {
    return {
      email: '',
      isValidEmail: false,
      isSubmitting: false,
      formMessage: '',
      formMessageType: 'success',
    }
  },
  computed: {
    backgroundStyle() {
      return {
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${this.backgroundImage})`,
      }
    },
  },
  methods: {
    validateEmail() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      this.isValidEmail = emailRegex.test(this.email)
    },
    async subscribe() {
      if (!this.isValidEmail) return

      this.isSubmitting = true
      this.formMessage = ''

      try {
        // Simulate API call
        await new Promise((resolve) => setTimeout(resolve, 1000))

        // Success response
        this.formMessage = 'Thank you for subscribing!'
        this.formMessageType = 'success'
        this.email = ''

        // Emit success event
        this.$emit('subscribed', this.email)
      } catch (error) {
        // Error handling
        this.formMessage = 'Something went wrong. Please try again.'
        this.formMessageType = 'error'

        // Emit error event
        this.$emit('subscription-error', error)
      } finally {
        this.isSubmitting = false
      }
    },
  },
}
</script>

<style scoped>
.contact-section {
  padding: 80px 20px;
  background-size: cover;
  background-position: center;
  color: #f3f3ca;
  position: relative;
}

.contact-container {
  max-width: 800px;
  margin: 0 auto;
}

.contact-title {
  font-size: 2.5rem;
  line-height: 1.2;
  margin-bottom: 20px;
  font-weight: bold;
}

.contact-description {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 30px;
  max-width: 600px;
}

.features-list {
  margin-bottom: 30px;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  margin-bottom: 15px;
}

.feature-icon {
  font-size: 1.2rem;
  margin-right: 10px;
  color: #f3f3ca;
}

.feature-text {
  font-size: 1.1rem;
}

.subscription-form {
  display: flex;
  margin-bottom: 15px;
  max-width: 500px;
}

.email-input {
  flex: 1;
  padding: 15px;
  font-size: 1rem;
  border: 2px solid rgba(243, 243, 202, 0.2);
  background: rgba(0, 0, 0, 0.2);
  color: #ffffff;
  outline: none;
}

.email-input::placeholder {
  color: rgba(243, 243, 202, 0.7);
}

.subscribe-button {
  padding: 15px 30px;
  border: none;
  background-color: #f3f3ca;
  color: #0a3200;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.subscribe-button:hover {
  background-color: #ffffff;
}

.subscribe-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.form-message {
  margin-top: 15px;
  padding: 10px;
  border-radius: 4px;
}

.form-message.success {
  background-color: rgba(76, 175, 80, 0.2);
}

.form-message.error {
  background-color: rgba(244, 67, 54, 0.2);
}

@media (max-width: 768px) {
  .contact-title {
    font-size: 2rem;
  }

  .subscription-form {
    flex-direction: column;
  }

  .email-input {
    margin-bottom: 15px;
  }
}
</style>
