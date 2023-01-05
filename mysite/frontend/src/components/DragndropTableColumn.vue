<template>
  <h2 class="text-center">{{ columnName }}</h2>
  <Draggable
      @change="handleTicketMove"
      :list="tickets"
      :group="options"
      item-key="tickets.name"
  >
    <template
        #item="{element}"
    >
      <div
          :data-status="options.name"
      >
        {{ element }}
      </div>
    </template>
  </Draggable>
</template>

<script>
import Draggable from 'vuedraggable'
const STATUS_TUPLE = {
  'Новое': 'new',
  'В работе': 'work',
  'Завершено': 'done'
}

export default {
  name: "DragndropTableColumn",
  components: {
    Draggable,
  },
  props: {
    tickets: Array,
    columnName: String,
    options: {
      name: String,
      pur: Array
    },
    patchNewTicketStatusById: Function
  },
  data() {
    return {}
  },
  methods: {
    handleTicketMove({added}) {
      if (added) {
        this.patchNewTicketStatusById({
          elementId: added.element.id,
          newStatus: STATUS_TUPLE[this.columnName]
        })
      }
    }
  },
}
</script>

<style scoped>

</style>
