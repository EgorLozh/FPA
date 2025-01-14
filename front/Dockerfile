# Используем официальный образ Node.js версии 18 или выше
FROM node:18 as build-stage

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем исходный код приложения
COPY . .

# Собираем приложение
RUN npm run build

# Используем легковесный образ Nginx для serving статических файлов
FROM nginx:alpine as production-stage

# Копируем собранные файлы из предыдущего этапа
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Открываем порт 80
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]