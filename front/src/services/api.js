import axios from 'axios';

const API_URL = 'http://localhost:8080/api'; // Замените на ваш базовый URL API

export const api = {
    // Получение списка сотрудников
    async getEmployees() {
        const response = await axios.get(`${API_URL}/employees`);
        return response.data;
    },

    // Получение списка магазинов
    async getStores() {
        const response = await axios.get(`${API_URL}/stores`);
        return response.data;
    },

    // Получение конкретного сотрудника по ID
    async getEmployeeById(id) {
        const response = await axios.get(`${API_URL}/employees/${id}`);
        return response.data;
    },

    // Добавление нового сотрудника
    async createEmployee(employeeData) {
        const response = await axios.post(`${API_URL}/employees`, employeeData);
        return response.data;
    },

    // Обновление данных сотрудника
    async updateEmployee(id, employeeData) {
        const response = await axios.put(`${API_URL}/employees/${id}`, employeeData);
        return response.data;
    },

    // Удаление сотрудника
    async deleteEmployee(id) {
        await axios.delete(`${API_URL}/employees/${id}`);
    }
};
