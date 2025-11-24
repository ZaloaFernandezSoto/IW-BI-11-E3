import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { VueFire } from 'vuefire'
import { firebaseApp } from './firebase'

const app = createApp(App)

app.use(VueFire, {
  // Importamos la app de firebase para que Vuefire la use
  firebaseApp,
  modules: [],
})

app.mount('#app')