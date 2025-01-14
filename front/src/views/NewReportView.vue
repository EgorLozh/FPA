<template>
  <div class="new-report-container">
    <h2>New Report</h2>
    
    <div class="upload-section">
      <div class="upload-box" @click="triggerFileUpload" @drop.prevent="handleDrop" @dragover.prevent>
        <input type="file" ref="fileInput" @change="handleFileChange" accept="audio/*,video/*" style="display: none">
        <div class="upload-content">
          <i class="fas fa-cloud-upload-alt"></i>
          <p>Click or drag to upload audio/video file</p>
          <span v-if="selectedFile">Selected: {{ selectedFile.name }}</span>
        </div>
      </div>

      <div class="script-section">
        <h3>Script</h3>
        <textarea v-model="script" placeholder="Enter the expected script here..."></textarea>
      </div>

      <div class="employee-section">
        <h3>Select Employee</h3>
        <button class="select-employee-button" @click="showModal = true">
          {{ selectedEmployee ? selectedEmployee.name : 'Choose Employee' }}
        </button>
      </div>

      <button class="analyze-button" @click="analyzeAndSend" :disabled="!isFormValid">
        Analyze and Send
      </button>
    </div>

    <EmployeeSearchModal
      :show="showModal"
      :employees="employees"
      :departments="departments"
      @close="showModal = false"
      @select="selectEmployee"
    />
  </div>
</template>

<script>
import EmployeeSearchModal from '@/components/EmployeeSearchModal.vue'

export default {
  name: 'NewReportView',
  components: {
    EmployeeSearchModal
  },
  props: {
    employees: Array,
    departments: Array,
  },
  data() {
    return {
      selectedFile: null,
      script: '',
      searchQuery: '',
      showEmployeeList: false,
      selectedEmployee: null,
      showModal: false
    }
  },
  computed: {
    isFormValid() {
      return this.selectedFile && this.script && this.selectedEmployee
    }
  },
  methods: {
    triggerFileUpload() {
      this.$refs.fileInput.click()
    },
    handleFileChange(event) {
      const file = event.target.files[0]
      if (file && (file.type.startsWith('audio/') || file.type.startsWith('video/'))) {
        this.selectedFile = file
      } else {
        alert('Please select an audio or video file')
      }
    },
    handleDrop(event) {
      const file = event.dataTransfer.files[0]
      if (file && (file.type.startsWith('audio/') || file.type.startsWith('video/'))) {
        this.selectedFile = file
      } else {
        alert('Please drop an audio or video file')
      }
    },
    selectEmployee(employee) {
      this.selectedEmployee = employee;
    },
    analyzeAndSend() {
      if (this.isFormValid) {
        // Here you would implement the actual file upload and analysis
        console.log('Analyzing report...', {
          file: this.selectedFile,
          script: this.script,
          employee: this.selectedEmployee
        })
        this.$router.push('/')
      }
    }
  }
}
</script>

<style scoped>
.new-report-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}

.upload-section {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.upload-box {
  border: 2px dashed #2193f2;
  border-radius: 8px;
  padding: 40px;
  text-align: center;
  cursor: pointer;
  transition: background-color 0.3s;
}

.upload-box:hover {
  background-color: rgba(33, 147, 242, 0.1);
}

.script-section textarea {
  width: 100%;
  height: 150px;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: vertical;
}

.search-box {
  position: relative;
}

.search-box input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.employee-list {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  max-height: 200px;
  overflow-y: auto;
  background: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  z-index: 1000;
}

.employee-item {
  padding: 8px;
  cursor: pointer;
}

.employee-item:hover {
  background-color: #f0f0f0;
}

.analyze-button {
  background-color: #2193f2;
  color: white;
  padding: 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.analyze-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.selected-employee {
  margin-top: 8px;
  padding: 8px;
  background-color: #e3f2fd;
  border-radius: 4px;
}

.select-employee-button {
  width: 100%;
  padding: 12px;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  text-align: left;
  transition: background-color 0.3s;
}

.select-employee-button:hover {
  background-color: #f5f5f5;
}
</style>