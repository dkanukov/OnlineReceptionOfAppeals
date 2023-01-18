<template>
  <div class="headerWrapper d-flex align-center justify-space-around">
    <div class="align-center">
      <div class="logo">
        <v-img
            width="83px"
            height="83px"
            :src="require('@/assets/hand.png')"
        />
        <p>ПРИЕМНАЯ ОБРАЩЕНИЙ</p>
      </div>
    </div>
    <v-text-field
        prepend-inner-icon="mdi-magnify"
        variant="solo"
        class="textInput"
        label="Поиск"
        hide-details="auto"
    />
    <div>
      <v-avatar color="surface-variant" size="50">
        <span class="text-h5">NC</span>
      </v-avatar>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeaderComponent',
  data() {
    return {}
  },
}
</script>

<style scoped>

.textInput {
  max-width: 800px;
}

.headerWrapper {
  display: flex;
  align-content: center;
  margin-top: 20px;
}

.logo {
  display: flex;
  align-content: center;
}

</style>
