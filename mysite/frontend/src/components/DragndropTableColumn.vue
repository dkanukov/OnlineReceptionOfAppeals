<template>
  <h2 class="text-center">{{ columnName }}</h2>
  <Draggable
      :list="list"
      item-key="list.id"
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
    columnName: String,
    list: Array,
    listId: String,
  },
  data() {
    return {}
  },
}
</script>

<style scoped>

</style>
