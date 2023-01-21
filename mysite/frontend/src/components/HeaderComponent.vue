<template>
  <div class="headerWrapper d-flex align-center justify-space-between ml">
    <div class="align-center">
      <div class="logo">
        <v-img
            width="83px"
            height="83px"
            :src="require('@/assets/hand.png')"
        />
        <h3 class="ml-2">ПРИЕМНАЯ ОБРАЩЕНИЙ</h3>
      </div>
    </div>
    <div class="d-flex align-center">
      <p class="mr-5" v-if="user">{{user.last_name}} {{user.first_name}}</p>
      <v-avatar color="surface-variant" size="50">
        <span class="text-h5">NC</span>
      </v-avatar>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
  name: 'HeaderComponent',
  data() {
    return {}
  },
  computed: {
    ...mapState(['user']),
  },
}
</script>

<style scoped>

.headerWrapper {
  display: flex;
  align-content: center;
  margin-top: 20px;
}

.logo {
  display: flex;
  align-items: center;
}

</style>
