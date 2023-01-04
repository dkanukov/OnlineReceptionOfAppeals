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
    }
  },
  data() {
    return {}
  },
  methods: {
    handleTicketMove({added}) {
      // TODO: сделать словарь с русского названия столбца на англ +
      // написать экшен который будет патчить +
      // мутация для локального изменения статуса
      console.log(added, this.columnName)
    }
  },
}
</script>

<style scoped>

</style>
