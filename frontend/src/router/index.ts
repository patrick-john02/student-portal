import { createRouter, createWebHistory, type RouteRecordRaw } from "vue-router";

const Login = () => import("@/pages/Login.vue");

const routes: RouteRecordRaw[] = [
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/",
    redirect: "/login",
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
