<template>
  <h2 class="text-center">{{ columnName }}</h2>
  <Draggable
      :list="tickets"
      item-key="tickets.name"
      group="tickets"
  >
    <template
        #item="{element}"
    >
      <div>
        {{ element }}
      </div>
    </template>
  </Draggable>
</template>

<script>
import Draggable from 'vuedraggable'

export default {
  name: "DragndropTableColumn",
  components: {
    Draggable,
  },
  props: {
    tickets: Array,
    columnName: String,
  },
  data() {
    return {}
  },
}
</script>

<style scoped>

</style>
