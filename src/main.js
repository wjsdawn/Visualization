import { createApp } from 'vue'
// import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import Home from './views/Home';
import VueAxios from "vue-axios";
import './assets/scss/style.scss';
import dataV from '@jiaminghi/data-view';

axios.defaults.baseURL = 'http://127.0.0.1:5000/';
createApp(Home).use(dataV).use(VueAxios,axios).use(store).use(router).mount('#app')
