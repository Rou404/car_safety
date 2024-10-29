
// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import './styles/index.css'
import axios from 'axios'
import { DaisyUI } from 'daisyui'
import 'daisyui/dist/full.css'

const app = createApp(App)
app.config.globalProperties.$axios = axios
app.use(DaisyUI)
app.mount('#app')
