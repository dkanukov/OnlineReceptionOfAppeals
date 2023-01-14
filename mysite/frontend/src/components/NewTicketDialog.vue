<template>
  <v-dialog v-model="isShowDialog" :ClickOutside="() => console.log(1)">
    <v-card>
      123
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "NewTicketDialog",
  props: {
    isShow: Boolean,
  },
  computed: {
    isShowDialog() {
      return Boolean(this.isShow)
    }
  },
}
</script>

<style scoped>

</style>
