<template>
  <div class="column">
    <h2 class="text-center">{{ columnName }}</h2>
    <Draggable
        @change="handleTicketMove"
        :list="tickets"
        :group="options"
        item-key="id"
    >
      <template #item="ticket">
        <div class="card">
          <div class="cardHeader d-flex justify-space-between">
            <h4>
              {{this.TICKET_NAME[ticket.element.type]}}
            </h4>
            <span class="text-grey-darken-1">
              id: {{ticket.element.id}}
            </span>
          </div>
          <div class="cardBody">

          </div>
        </div>
      </template>
    </Draggable>
  </div>
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
    return {
      TICKET_NAME: {
        1: 'Помощь',
        2: 'Консультация',
        3: 'Волонтерство',
      },
    }
  },
  methods: {
    handleTicketMove({added}) {
      if (added) {
        this.patchNewTicketStatusById({
          elementId: added.element.id,
          newStatus: STATUS_TUPLE[this.columnName]
        })
      }
    },
  },
}
</script>

<style scoped>
.column {
  padding: 10px;
  background-color: #FAFAFB;
  border: 3px solid #E2E2EA;
  border-radius: 26px;
}

.card {
  padding: 10px;
  margin-top: 14px;
  background-color: #fff;
  border-radius: 20px;
}

</style>
