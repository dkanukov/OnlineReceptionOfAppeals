import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import store from '@/store';
import { SetupCalendar } from 'v-calendar'

loadFonts()

createApp(App)
	.use(vuetify)
	.use(store)
	.use(SetupCalendar, {})
	.mount('#app')
