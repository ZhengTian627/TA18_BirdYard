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
        <img :src="previewUrl" alt="预览图片" class="preview-image" ref="previewImage" />
        <div v-if="result" class="detection-box" :style="getBoundingBoxStyle()"></div>
      </div>
    </div>

    <div v-if="result" class="result-container">
      <h2>识别结果</h2>
      <div class="result-item"><strong>鸟类名称:</strong> {{ result.class_name }}</div>
      <div class="result-item">
        <strong>置信度:</strong> {{ (result.confidence * 100).toFixed(2) }}%
      </div>
      <div class="result-item"><strong>类别ID:</strong> {{ result.class_id }}</div>
    </div>

    <div v-if="error" class="error-message">
      {{ error }}
    </div>
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
