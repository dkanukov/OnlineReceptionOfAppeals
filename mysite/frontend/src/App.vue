<template>
  <v-app>
    <v-main>
      <HeaderComponent/>
    </v-main>
  </v-app>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent';

export default {
  name: 'App',

  components: {
    HeaderComponent,
  },

  data() {
    return {
    }
  },
}
</script>
