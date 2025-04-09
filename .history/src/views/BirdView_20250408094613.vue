<!-- BirdDetection.vue -->
<template>
  <div class="bird-detection-container">
    <h1>鸟类识别</h1>

    <div class="upload-section">
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

    <div v-if="previewUrl" class="preview-container">
      <div class="image-container">
        <img :src="previewUrl" alt="预览图片" class="preview-image" />
        <div v-if="result" class="detection-box" :style="getBoundingBoxStyle()"></div>
      </div>
    </div>

    <div v-if="result" class="result-container">
      <h2>识别结果</h2>
      <div class="result-item"><strong>鸟类名称:</strong> {{ result.name }}</div>
      <div class="result-item">
        <strong>置信度:</strong> {{ (result.confidence * 100).toFixed(2) }}%
      </div>
    </div>

    <div v-if="error" class="error-message">
      {{ error }}
    </div>
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
    const imageWidth = ref(0)
    const imageHeight = ref(0)

    /**
     * 上传图片进行鸟类识别
     * @param {File} imageFile - 图片文件对象（来自 input[type=file]）
     * @returns {Promise<Object>} 识别结果（包含识别的鸟类名称、置信度、框坐标等）
     */
    const detectBirdFromImage = async (imageFile) => {
      try {
        const formData = new FormData()
        formData.append('file', imageFile)
        const response = await axios.post('http://3.26.98.65:8000/predict/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        return response.data // ✅ 返回识别结果
      } catch (error) {
        console.error('识别失败:', error)
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

      // 获取图片尺寸
      const img = new Image()
      img.onload = async () => {
        imageWidth.value = img.width
        imageHeight.value = img.height

        // 开始识别
        try {
          isLoading.value = true
          const detectionResult = await detectBirdFromImage(file)
          result.value = detectionResult
        } catch (err) {
          error.value = '识别失败，请重试'
          console.error(err)
        } finally {
          isLoading.value = false
        }
      }
      img.src = previewUrl.value
    }

    const getBoundingBoxStyle = () => {
      if (!result.value || !result.value.bbox) return {}

      const [x, y, width, height] = result.value.bbox

      return {
        left: `${x}%`,
        top: `${y}%`,
        width: `${width}%`,
        height: `${height}%`,
      }
    }

    return {
      previewUrl,
      result,
      error,
      isLoading,
      handleFileUpload,
      getBoundingBoxStyle,
    }
  },
}
</script>

<style scoped>
.bird-detection-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
}

.upload-section {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}

.upload-button {
  display: inline-block;
  padding: 12px 24px;
  background-color: #4caf50;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.upload-button:hover {
  background-color: #45a049;
}

.upload-button input {
  display: none;
}

.preview-container {
  margin-bottom: 30px;
  display: flex;
  justify-content: center;
}

.image-container {
  position: relative;
  max-width: 100%;
  display: inline-block;
}

.preview-image {
  max-width: 100%;
  max-height: 400px;
  border-radius: 4px;
}

.detection-box {
  position: absolute;
  border: 3px solid #ff4500;
  box-sizing: border-box;
  pointer-events: none;
}

.result-container {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 4px;
  margin-bottom: 20px;
}

.result-item {
  margin-bottom: 10px;
}

.error-message {
  color: #ff4500;
  text-align: center;
  margin-top: 10px;
}
</style>
