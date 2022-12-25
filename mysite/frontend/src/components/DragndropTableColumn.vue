<template>
<div>
  <h2 class="text-center">{{columnName}}</h2>
  <Draggable>
    <DraggableTicket/>
  </Draggable>
</div>
</template>

<script>
import Draggable from 'vuedraggable'
import DraggableTicket from '@/components/DraggableTicket.vue';
export default {
  name: "DragndropTableColumn",
  components: {
    DraggableTicket,
    Draggable,
  },
  props: {
    columnName: String,
  }
}
</script>

<style scoped>

</style>
