<template>
  <div class="headerWrapper d-flex align-center justify-space-between ml">
    <div class="align-center">
      <div class="logo">
        <v-img
            width="70px"
            height="70px"
            :src="require('@/assets/hand.png')"
        />
        <h2 class="ml-2 align-self-center">ПРИЕМНАЯ ОБРАЩЕНИЙ</h2>
      </div>
    </div>
    <div class="d-flex align-center">
      <h3 class="mr-5" v-if="user">{{user.last_name}} {{user.first_name}}</h3>
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
