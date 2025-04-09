import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ContactView from '@/views/ContactView.vue'
import AboutView from '../views/AboutView.vue'
import PlantadviceView from '@/views/PlantadviceView.vue'
import BirdView from '@/views/BirdView.vue'
import PlantDetailView from '@/views/PlantDetailView.vue'
import WelcomeView from '@/views/ WelcomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'welcome',
      component: WelcomeView,
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
    {
      path: '/contact',
      name: 'contact',
      component: ContactView,
    },
    {
      path: '/plantadvice',
      name: 'plantadvice',
      component: PlantadviceView,
    },
    {
      path: '/bird',
      name: 'bird',
      component: BirdView,
    },
    {
      path: '/plant/:plantName',
      name: 'PlantDetail',
      component: PlantDetailView,
      props: true,
    },
  ],
})

export default router
