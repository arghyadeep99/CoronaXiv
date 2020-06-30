import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'

import Paginate from 'vuejs-paginate'
Vue.component('paginate', Paginate)

import ToggleButton from 'vue-js-toggle-button'
Vue.use(ToggleButton)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
