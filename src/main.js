import { createApp } from 'vue'
// import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import Home from './views/index';
import VueAxios from "vue-axios";
import './assets/scss/style.scss';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

axios.defaults.baseURL = 'http://127.0.0.1:5000/';
createApp(Home).use(ElementPlus).use(VueAxios,axios).use(store).use(router).mount('#app')
