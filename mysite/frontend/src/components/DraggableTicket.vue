<template #item>
  <h2>{{ticket}}</h2>
</template>

<script>
export default {
  name: "DraggableTicket",
  props: {
    ticket: Object,
  },
}
</script>

<style scoped>

</style>
