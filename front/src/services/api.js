import axios from 'axios';

const API_URL = 'http://localhost/api';

export const api = {
  // Workers
  async getWorkers(params = {}) {
    try {
      const response = await axios.get(`${API_URL}/worker/`, { params });
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch workers: ' + error.message);
    }
  },

  async getWorkerById(id) {
    try {
      const response = await axios.get(`${API_URL}/worker/${id}`);
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch worker by ID: ' + error.message);
    }
  },

  // Departments
  async getDepartments() {
    try {
      const response = await axios.get(`${API_URL}/department/`);
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch departments: ' + error.message);
    }
  },

  // Scripts
  async getScripts(params = {}) {
    try {
      const response = await axios.get(`${API_URL}/script/`, { params });
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch scripts: ' + error.message);
    }
  },

  // Reports
  async getReports() {
    try {
      const response = await axios.get(`${API_URL}/report/report`);
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch reports: ' + error.message);
    }
  },

  // Requests
  async getRequests() {
    try {
      const response = await axios.get(`${API_URL}/request/`);
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch requests: ' + error.message);
    }
  },

  // Create Department
  async createDepartment(data) {
    try {
      const response = await axios.post(`${API_URL}/department/`, data);
      return response.data;
    } catch (error) {
      throw new Error('Failed to create department: ' + error.message);
    }
  },

  // Create Request
  async createRequest(data) {
    try {
      const response = await axios.post(`${API_URL}/request/`, data);
      return response.data;
    } catch (error) {
      throw new Error('Failed to create request: ' + error.message);
    }
  },
};