import { createRouter, createWebHistory } from 'vue-router';
import DashboardView from '@/views/DashboardView.vue';
import EmployeeRatingView from '@/views/EmployeeRatingView.vue';
import Home from '@/views/Home.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView
  },
  {
    path: '/employee-rating',
    name: 'EmployeeRating',
    component: EmployeeRatingView
  },
  {
    path: '/employee/:id',
    name: 'Employee',
    component: () => import('@/components/EmployeeDetails.vue'),
    props: route => ({ id: Number(route.params.id) })
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
