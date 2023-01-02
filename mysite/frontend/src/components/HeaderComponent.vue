<template>
  <div class="headerWrapper d-flex align-center justify-space-between">
    <v-text-field
        prepend-inner-icon="mdi-magnify"
        variant="solo"
        class="textInput"
        label="Поиск"
        hide-details="auto"
    />
    <div >
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
  margin-left: 20%;
  max-width: 800px;
}

.headerWrapper {
  margin-top: 20px;
}

</style>
