import { createRouter, createWebHistory } from 'vue-router'

// --- Import pages ---
// import Home from '@/views/Home.vue'
// import About from '@/views/About.vue'

// --- Define routes ---
const routes = [
//   { path: '/', name: 'home', component: Home },
//   { path: '/about', name: 'about', component: About },
]

// --- Create router instance ---
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
