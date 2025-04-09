<template>
  <div class="bird-detection-container">
    <!-- Banner Section -->
    <section class="banner">
      <h1 class="banner-title">鸟类识别</h1>
      <p class="banner-subtitle">上传图片，了解您花园中的鸟类</p>
    </section>

    <!-- Upload Section -->
    <section class="upload-section">
      <div class="container">
        <label for="upload" class="upload-button">
          <span v-if="!isLoading">选择图片上传</span>
          <span v-else>处理中...</span>
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

    <!-- Preview Section -->
    <section class="preview-section" v-if="previewUrl">
      <div class="container">
        <div class="content-grid">
          <!-- Left Column - Image Preview -->
          <div class="image-container">
            <div class="image-card">
              <img :src="previewUrl" alt="预览图片" class="preview-image" ref="previewImage" />
              <div v-if="result" class="detection-box" :style="getBoundingBoxStyle()"></div>
            </div>
          </div>

          <!-- Right Column - Detection Results -->
          <div class="result-container" v-if="result">
            <div class="result-card">
              <h2>识别结果</h2>
              <div class="result-content">
                <div class="result-item">
                  <span class="result-label">鸟类名称:</span>
                  <span class="result-value">{{ result.class_name }}</span>
                </div>
                <div class="result-item">
                  <span class="result-label">置信度:</span>
                  <span class="result-value">{{ (result.confidence * 100).toFixed(2) }}%</span>
                </div>
                <div class="result-item">
                  <span class="result-label">类别ID:</span>
                  <span class="result-value">{{ result.class_id }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Error Message -->
    <div v-if="error" class="error-container">
      <div class="error-message">
        {{ error }}
      </div>
    </div>

    <!-- Call to Action -->
    <section class="cta-section">
      <router-link to="/plantadvice" class="btn btn-large">探索适合鸟类的植物</router-link>
    </section>

    <!-- Information Section -->
    <section class="info-section">
      <div class="container">
        <div class="info-content">
          <div class="info-text">
            <h2>了解您周围的鸟类</h2>
            <p>
              识别鸟类是建立鸟类友好庭院的第一步。通过了解您附近的鸟类种类，您可以选择更适合它们的植物和栖息环境。
            </p>
          </div>
          <div class="info-description">
            <p>
              上传您在庭院中看到的鸟类照片，我们的系统将帮助您识别它们。一旦识别出鸟类种类，您可以前往"植物建议"页面，
              查找适合吸引和支持这些鸟类的本地植物。
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
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
     * 上传图片进行鸟类识别
     * @param {File} imageFile - 图片文件对象（来自 input[type=file]）
     * @returns {Promise<Object>} 识别结果（包含识别的鸟类名称、置信度、框坐标等）
     */
    const detectBirdFromImage = async (imageFile) => {
      // Ensure imageFile is a valid File object before proceeding
      if (!imageFile || !(imageFile instanceof File)) {
        const errorMsg = 'Invalid imageFile provided. Expected a File object.'
        console.error(errorMsg)
        throw new Error(errorMsg)
      }

      try {
        const formData = new FormData()
        formData.append('file', imageFile)

        const apiUrl = 'http://3.26.98.65:8000/predict/' // Consider making this configurable

        // 解决CORS问题：添加withCredentials配置
        const response = await axios.post(apiUrl, formData, {
          withCredentials: false, // 如果不需要发送cookies，设为false
        })

        console.log('API Response Status:', response.status)
        console.log('API Response Data:', response.data)

        // 返回检测到的第一个鸟类（如果有）
        if (response.data && response.data.detections && response.data.detections.length > 0) {
          return response.data.detections[0]
        } else {
          throw new Error('未检测到鸟类')
        }
      } catch (error) {
        console.error('Error calling bird detection API:', error)
        if (error.response) {
          // Server responded with an error status (4xx or 5xx)
          console.error('Error Response Data:', error.response.data)
          console.error('Error Response Status:', error.response.status)
        } else if (error.request) {
          // Request made, but no response received (network issue, server down, CORS preflight failed)
          console.error(
            'No response received from server. Check network connection, server status at ' +
              (error.config?.url || 'API URL') +
              ', and CORS configuration on the server.',
          )
        } else {
          // Error setting up the request
          console.error('Error Message:', error.message)
        }
        // Re-throw the error for the calling component to handle
        throw error
      }
    }

    const handleFileUpload = async (event) => {
      const file = event.target.files[0]
      if (!file) return

      // 清除之前的结果
      result.value = null
      error.value = ''

      // 显示预览
      previewUrl.value = URL.createObjectURL(file)

      // 获取图片尺寸并开始识别
      const img = new Image()
      img.onload = async () => {
        // 开始识别
        try {
          isLoading.value = true
          const detectionResult = await detectBirdFromImage(file)
          result.value = detectionResult
        } catch (err) {
          error.value = '识别失败，请重试: ' + (err.message || '未知错误')
          console.error(err)
        } finally {
          isLoading.value = false
        }
      }
      img.src = previewUrl.value
    }

    const getBoundingBoxStyle = () => {
      if (!result.value || !result.value.bounding_box) return {}

      // 使用服务器返回的边界框坐标
      // API返回的格式是 [x, y, width, height] 像素坐标
      const [x, y, width, height] = result.value.bounding_box

      // 获取预览图片的尺寸
      const imgElement = previewImage.value
      if (!imgElement) return {}

      const imgWidth = imgElement.clientWidth
      const imgHeight = imgElement.clientHeight

      // 计算边界框的相对位置（百分比）
      // 注意：这里假设API返回的是像素坐标，需要转换为百分比
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
/* Global styles matching other views */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.btn {
  display: inline-block;
  padding: 12px 24px;
  border-radius: 30px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  text-align: center;
}

.btn-large {
  padding: 15px 30px;
  font-size: 18px;
  background-color: rgba(194, 229, 156, 0.9);
  color: #0a3200;
  border: 2px solid #c2e59c;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

/* Banner Section */
.banner {
  height: 400px;
  background-image:
    linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('@/assets/images/birds-bg.jpeg');
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0 20px;
  color: white;
}

.banner-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 10px;
}

.banner-subtitle {
  font-size: 1.2rem;
}

/* Upload Section */
.upload-section {
  padding: 40px 0;
  text-align: center;
  background-color: #f9f9f9;
}

.upload-button {
  display: inline-block;
  padding: 15px 30px;
  background-color: rgba(194, 229, 156, 0.9);
  color: #0a3200;
  border: 2px solid #c2e59c;
  border-radius: 30px;
  cursor: pointer;
  font-size: 18px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.upload-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.upload-button input {
  display: none;
}

/* Preview Section */
.preview-section {
  padding: 60px 0;
  background-color: #ffffff;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

.image-container {
  display: flex;
  justify-content: center;
}

.image-card {
  position: relative;
  max-width: 100%;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.preview-image {
  max-width: 100%;
  max-height: 500px;
  display: block;
}

.detection-box {
  position: absolute;
  border: 3px solid #ff4500;
  box-sizing: border-box;
  pointer-events: none;
  box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.5);
}

.result-container {
  display: flex;
  justify-content: center;
}

.result-card {
  width: 100%;
  background-color: #f0f7e6;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.result-card h2 {
  color: #0a3200;
  font-size: 1.8rem;
  margin-bottom: 20px;
  border-bottom: 2px solid #c2e59c;
  padding-bottom: 10px;
}

.result-content {
  padding: 10px 0;
}

.result-item {
  display: flex;
  margin-bottom: 15px;
  padding: 10px;
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 8px;
}

.result-label {
  font-weight: 600;
  color: #0a3200;
  width: 100px;
}

.result-value {
  flex: 1;
}

/* Error Message */
.error-container {
  padding: 20px;
  text-align: center;
}

.error-message {
  display: inline-block;
  color: #ff4500;
  background-color: rgba(255, 69, 0, 0.1);
  padding: 15px 30px;
  border-radius: 8px;
  font-weight: 500;
}

/* CTA Section */
.cta-section {
  padding: 40px 0;
  text-align: center;
  background-color: #f9f9f9;
}

/* Info Section */
.info-section {
  padding: 80px 0;
  background-color: #ffffff;
}

.info-content {
  display: flex;
  gap: 60px;
}

.info-text {
  flex: 1;
}

.info-text h2 {
  font-size: 2.2rem;
  color: #0a3200;
  line-height: 1.3;
  margin-bottom: 30px;
}

.info-description {
  flex: 1;
}

.info-text p,
.info-description p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #333;
}

/* Responsive Design */
@media (max-width: 992px) {
  .content-grid {
    grid-template-columns: 1fr;
  }

  .info-content {
    flex-direction: column;
    gap: 30px;
  }
}

@media (max-width: 768px) {
  .banner-title {
    font-size: 2rem;
  }

  .banner-subtitle {
    font-size: 1rem;
  }

  .preview-image {
    max-height: 400px;
  }

  .info-text h2 {
    font-size: 1.8rem;
  }
}
</style>
