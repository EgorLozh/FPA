<template>
  <div class="search-input-container">
    <input 
      type="text" 
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      :placeholder="placeholder" 
      class="search-input"
    />
    <i class="search-icon">🔍</i>
  </div>
</template>

<script>
export default {
  name: 'SearchInput',
  props: {
    modelValue: String,
    placeholder: {
      type: String,
      default: 'Search...'
    }
  },
  emits: ['update:modelValue']
}
</script>

<style scoped>
.search-input-container {
  position: relative;
  margin-bottom: 15px;
  width: 100%;
}

.search-input {
  width: 100%;
  padding: 12px 40px 12px 15px;
  font-size: 16px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  transition: all 0.3s ease;
  background-color: white;
}

.search-input:hover {
  transform: translateY(-2px);
  border-color: #2193f2;
  box-shadow: 0 4px 12px rgba(33, 147, 242, 0.1);
  background-color: rgba(33, 147, 242, 0.02);
}

.search-input:focus {
  outline: none;
  transform: translateY(-2px);
  border-color: #2193f2;
  box-shadow: 0 4px 12px rgba(33, 147, 242, 0.15);
  background-color: rgba(33, 147, 242, 0.03);
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #666;
  pointer-events: none;
}
</style>
