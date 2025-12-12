import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    routes: [
        {
            path: '/blogs',
            name: 'blogs',
            component: () => import('../views/BlogView.vue'),
        }
    ],
})
    
export default router
