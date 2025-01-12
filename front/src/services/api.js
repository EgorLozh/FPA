import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const api = {
    // Workers
    async getWorkers() {
        const response = await fetch('/api/workers');
        if (!response.ok) throw new Error('Failed to fetch workers');
        return response.json();
    },
    
    async getWorkerById(id) {
        const response = await axios.get(`${API_URL}/worker/${id}`);
        return response.data;
    },

    // Departments
    async getDepartments() {
        const response = await fetch('/api/departments');
        if (!response.ok) throw new Error('Failed to fetch departments');
        return response.json();
    },

    // Scripts
    async getScripts() {
        const response = await axios.get(`${API_URL}/script`);
        return response.data;
    },

    // Reports
    async getReports() {
        const response = await axios.get(`${API_URL}/report`);
        return response.data;
    },

    // Requests
    async getRequests() {
        const response = await axios.get(`${API_URL}/request`);
        return response.data;
    },
};
