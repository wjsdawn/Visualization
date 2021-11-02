import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import VueAxios from "vue-axios";
// import './assets/scss/style.scss'

axios.defaults.baseURL = 'http://127.0.0.1:5000/';
createApp(App).use(store).use(VueAxios,axios).use(router).mount('#app')
