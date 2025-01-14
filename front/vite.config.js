import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  server: {
    proxy: {
      // Прокси для всех запросов, начинающихся с /api
      '/api': {
        target: 'http://localhost', // Ваш бэкенд-сервер
        changeOrigin: true, // Меняет origin на целевой сервер
        rewrite: (path) => path.replace(/^\/api/, ''), // Убирает /api из пути
        rewrite: (path) => path.replace(5173, ''),
      },
    },
  },
});