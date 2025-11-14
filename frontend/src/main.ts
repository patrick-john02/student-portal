import { createApp } from "vue";
import { createPinia } from "pinia";
import { VueQueryPlugin, type VueQueryPluginOptions } from "@tanstack/vue-query";

import App from "./App.vue";
import router from "./router";
import "./style.css";

const pinia = createPinia();

const vueQueryOptions: VueQueryPluginOptions = {
  queryClientConfig: {
    defaultOptions: {
      queries: {
        retry: 1,
        refetchOnWindowFocus: false,
        staleTime: 1000 * 60 * 2, // 2 min
      },
    },
  },
};

const app = createApp(App);

app.use(pinia);
app.use(router);
app.use(VueQueryPlugin, vueQueryOptions);

app.mount("#app");


//types -> services -> composables -> vue