<template>
  <v-app-bar>
    <v-text-field
        prepend-inner-icon="mdi-magnify"
        variant="solo"
        class="textInput"
        label="Поиск"
        hide-details="auto"
    />
    <template
        v-slot:append
    >
      <v-btn
          icon="mdi-exit-to-app"
      />
      <v-avatar color="surface-variant" size="50">
        <span class="text-h5">NC</span>
      </v-avatar>
    </template>
  </v-app-bar>
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

</style>
