<template>
  <div class="bird-detection-container">
    <!-- Hero Section with Overlay Text -->
    <section class="hero-section">
      <div class="hero-content">
        <h1 class="hero-title">Your Backyard Birds Identified With Precision</h1>
        <p class="hero-subtitle">
          Discover the beauty of your garden visitors - where every identified bird brings you
          closer to nature.
        </p>

        <div class="features-list">
          <div class="feature-item">
            <span class="feature-icon">✓</span> Instant Bird Species Recognition
          </div>
          <div class="feature-item">
            <span class="feature-icon">✓</span> High Accuracy Detection Technology
          </div>
          <div class="feature-item">
            <span class="feature-icon">✓</span> Personalized Garden Recommendations
          </div>
        </div>

        <!-- Upload Button as Main CTA -->
        <label for="upload" class="upload-button">
          <span v-if="!isLoading">Upload Image Now!</span>
          <span v-else>Processing...</span>
          <input
            type="file"
            id="upload"
            accept="image/*"
            @change="handleFileUpload"
            :disabled="isLoading"
          />
        </label>
      </div>
    </section>

    <!-- Results Section (Only visible after upload) -->
    <section class="results-section" v-if="previewUrl">
      <div class="results-container">
        <div class="results-grid">
          <!-- Image Preview Column -->
          <div class="image-preview-column">
            <div class="preview-wrapper">
              <img
                :src="previewUrl"
                alt="Bird image preview"
                class="preview-image"
                ref="previewImage"
              />
              <div v-if="result" class="detection-box" :style="getBoundingBoxStyle()"></div>
            </div>
          </div>

          <!-- Results Column -->
          <div class="results-details-column">
            <div v-if="result" class="results-card">
              <h2 class="results-heading">Detection Results</h2>
              <div class="result-item">
                <span class="result-label">Species:</span>
                <span class="result-value">{{ result.class_name }}</span>
              </div>
              <div class="result-item">
                <span class="result-label">Confidence:</span>
                <span class="result-value">{{ (result.confidence * 100).toFixed(2) }}%</span>
              </div>
              <p class="results-description">
                We've detected this bird species in your image. Learn more about how to attract and
                support this species in your garden.
              </p>
              <router-link to="/plantadvice" class="secondary-button"
                >Find Suitable Plants</router-link
              >
            </div>

            <div v-else-if="isLoading" class="processing-message">
              <div class="loading-spinner"></div>
              <p>Analyzing your image...</p>
              <p class="processing-subtext">
                Our AI is identifying bird species and characteristics
              </p>
            </div>

            <div v-else class="upload-success-message">
              <h3>Image uploaded successfully!</h3>
              <p>We're analyzing your photo to identify the bird species.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Error Message Section -->
    <section class="error-section" v-if="error">
      <div class="error-message">
        {{ error }}
      </div>
    </section>

    <!-- Email Subscription Section -->
    <section class="subscription-section">
      <div class="subscription-content">
        <h2 class="subscription-title">Want To Learn More About Birds In Your Area?</h2>
        <p class="subscription-subtitle">
          Join our newsletter for seasonal bird watching tips and garden planning advice.
        </p>

        <div class="subscription-form">
          <input type="email" placeholder="Your email address" class="email-input" />
          <button class="subscribe-button">Subscribe</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'BirdDetection',
  setup() {
    const previewUrl = ref('')
    const result = ref(null)
    const error = ref('')
    const isLoading = ref(false)
    const previewImage = ref(null)

    /**
     * Upload image for bird species detection
     * @param {File} imageFile - Image file object from input[type=file]
     * @returns {Promise<Object>} Detection result with bird species name, confidence, bounding box, etc.
     */
    const detectBirdFromImage = async (imageFile) => {
      if (!imageFile || !(imageFile instanceof File)) {
        const errorMsg = 'Invalid image file provided. Please select a valid image.'
        console.error(errorMsg)
        throw new Error(errorMsg)
      }

      try {
        const formData = new FormData()
        formData.append('file', imageFile)

        const apiUrl = 'http://3.26.98.65:8000/predict/'

        // Configure CORS settings
        const response = await axios.post(apiUrl, formData, {
          withCredentials: false,
        })

        console.log('API Response Status:', response.status)
        console.log('API Response Data:', response.data)

        // Return the first detection if available
        if (response.data && response.data.detections && response.data.detections.length > 0) {
          return response.data.detections[0]
        } else {
          throw new Error('No birds detected in the image. Please try with a clearer photo.')
        }
      } catch (error) {
        console.error('Error calling bird detection API:', error)
        if (error.response) {
          console.error('Error Response Data:', error.response.data)
          console.error('Error Response Status:', error.response.status)
        } else if (error.request) {
          console.error(
            'No response received from server. Please check your internet connection and try again.',
          )
        } else {
          console.error('Error Message:', error.message)
        }
        throw error
      }
    }

    const handleFileUpload = async (event) => {
      const file = event.target.files[0]
      if (!file) return

      // Clear previous results
      result.value = null
      error.value = ''

      // Show preview
      previewUrl.value = URL.createObjectURL(file)

      // Start detection process
      const img = new Image()
      img.onload = async () => {
        try {
          isLoading.value = true
          const detectionResult = await detectBirdFromImage(file)
          result.value = detectionResult
        } catch (err) {
          error.value = err.message || 'Detection failed. Please try again with a different image.'
          console.error(err)
        } finally {
          isLoading.value = false
        }
      }
      img.src = previewUrl.value
    }

    const getBoundingBoxStyle = () => {
      if (!result.value || !result.value.bounding_box) return {}

      // Use bounding box coordinates from API response
      const [x, y, width, height] = result.value.bounding_box

      // Get preview image dimensions
      const imgElement = previewImage.value
      if (!imgElement) return {}

      // Calculate relative position (percentage)
      const boxStyle = {
        left: `${(x / imgElement.naturalWidth) * 100}%`,
        top: `${(y / imgElement.naturalHeight) * 100}%`,
        width: `${(width / imgElement.naturalWidth) * 100}%`,
        height: `${(height / imgElement.naturalHeight) * 100}%`,
      }

      return boxStyle
    }

    return {
      previewUrl,
      result,
      error,
      isLoading,
      handleFileUpload,
      getBoundingBoxStyle,
      previewImage,
    }
  },
}
</script>

<style scoped>
.bird-detection-container {
  font-family: 'Arial', sans-serif;
  color: #333;
}

/* Hero Section Styles */
.hero-section {
  position: relative;
  height: 100vh;
  min-height: 600px;
  background-image:
    linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('@/assets/images/bird-hero.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 0 10%;
}

.hero-content {
  max-width: 600px;
  color: #f0f0f0;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: #f3f9c0;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.2rem;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.features-list {
  margin-bottom: 2.5rem;
}

.feature-item {
  display: flex;
  align-items: center;
  margin-bottom: 0.8rem;
  font-size: 1.1rem;
}

.feature-icon {
  color: #f3f9c0;
  margin-right: 10px;
  font-weight: bold;
}

.upload-button {
  display: inline-block;
  background-color: #f3f9c0;
  color: #1a2d00;
  font-weight: 600;
  padding: 15px 30px;
  border-radius: 4px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  text-align: center;
}

.upload-button:hover {
  background-color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.upload-button input {
  display: none;
}

/* Results Section Styles */
.results-section {
  padding: 80px 10%;
  background-color: #f8f9fa;
}

.results-container {
  max-width: 1200px;
  margin: 0 auto;
}

.results-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: center;
}

.image-preview-column {
  position: relative;
}

.preview-wrapper {
  position: relative;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  border-radius: 8px;
  overflow: hidden;
  background-color: #fff;
}

.preview-image {
  width: 100%;
  display: block;
}

.detection-box {
  position: absolute;
  border: 3px solid #ff6b6b;
  box-sizing: border-box;
  pointer-events: none;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(255, 107, 107, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 107, 107, 0);
  }
}

.results-details-column {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.results-card {
  background-color: #fff;
  border-radius: 8px;
  padding: 30px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.results-heading {
  color: #1a2d00;
  font-size: 2rem;
  margin-bottom: 1.5rem;
  border-bottom: 2px solid #f3f9c0;
  padding-bottom: 0.5rem;
}

.result-item {
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

.result-label {
  font-weight: 600;
  color: #555;
  display: inline-block;
  width: 100px;
}

.result-value {
  font-weight: 500;
  color: #1a2d00;
}

.results-description {
  margin: 1.5rem 0;
  color: #666;
  line-height: 1.6;
}

.secondary-button {
  display: inline-block;
  background-color: #1a2d00;
  color: #f3f9c0;
  padding: 12px 24px;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  text-align: center;
}

.secondary-button:hover {
  background-color: #2c4b00;
  transform: translateY(-2px);
}

.processing-message {
  text-align: center;
  padding: 40px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.loading-spinner {
  display: inline-block;
  width: 50px;
  height: 50px;
  border: 5px solid #f3f9c0;
  border-radius: 50%;
  border-top-color: #1a2d00;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.processing-subtext {
  color: #777;
  font-style: italic;
  margin-top: 10px;
}

.upload-success-message {
  text-align: center;
  padding: 40px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.upload-success-message h3 {
  color: #1a2d00;
  margin-bottom: 1rem;
}

/* Error Section */
.error-section {
  padding: 20px 10%;
  text-align: center;
}

.error-message {
  display: inline-block;
  color: #fff;
  background-color: #ff6b6b;
  padding: 15px 30px;
  border-radius: 8px;
  font-weight: 500;
}

/* Subscription Section */
.subscription-section {
  padding: 80px 10%;
  background-color: #1a2d00;
  color: #fff;
  text-align: center;
}

.subscription-content {
  max-width: 700px;
  margin: 0 auto;
}

.subscription-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: #f3f9c0;
}

.subscription-subtitle {
  font-size: 1.2rem;
  line-height: 1.6;
  margin-bottom: 2.5rem;
  color: #f0f0f0;
}

.subscription-form {
  display: flex;
  max-width: 500px;
  margin: 0 auto;
}

.email-input {
  flex: 1;
  padding: 15px;
  border: 1px solid rgba(243, 249, 192, 0.3);
  background-color: rgba(255, 255, 255, 0.1);
  color: #fff;
  border-radius: 4px 0 0 4px;
  font-size: 1rem;
}

.email-input::placeholder {
  color: rgba(255, 255, 255, 0.7);
}

.subscribe-button {
  background-color: #f3f9c0;
  color: #1a2d00;
  font-weight: 600;
  padding: 15px 25px;
  border: none;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
  transition: all 0.3s ease;
}

.subscribe-button:hover {
  background-color: #ffffff;
}

/* Responsive Styles */
@media (max-width: 992px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .results-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .hero-section {
    padding: 0 5%;
    text-align: center;
    justify-content: center;
  }

  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .feature-item {
    justify-content: center;
  }

  .subscription-form {
    flex-direction: column;
  }

  .email-input {
    border-radius: 4px;
    margin-bottom: 10px;
  }

  .subscribe-button {
    border-radius: 4px;
  }
}
</style>
