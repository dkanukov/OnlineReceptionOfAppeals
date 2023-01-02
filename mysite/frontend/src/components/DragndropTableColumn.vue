<template>
  <h2 class="text-center">{{ columnName }}</h2>
  <Draggable
      :list="list"
  >
    <template
        #item="{element}"
    >
      {{ element }}
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
    columnName: String,
    list: Array
  },
  data() {
    return {}
  },
}
</script>

<style scoped>

</style>
