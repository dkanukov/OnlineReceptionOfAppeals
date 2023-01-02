<template>
  <div class="d-flex justify-center">
    <v-col>
      <DragndropTableColumn
          column-name="Новое"
          :tickets="newTicketsProp"
      />
    </v-col>
    <v-col>
      <DragndropTableColumn
          column-name="В работе"
          :tickets="inProgressTickets"
      />
    </v-col>
    <v-col>
      <DragndropTableColumn
          column-name="Завершено"
          :tickets="[]"
      />
    </v-col>
  </div>
</template>

<script>
import DragndropTableColumn from '@/components/DragndropTableColumn.vue';
export default {
  name: "DragndropTable",
  components:{
    DragndropTableColumn,
  },
  props: {
    tickets: Array,
  },
  data() {
    return {
      newTicketsProp: [
        { name: "John", id: 1 },
      ],
      inProgressTickets: []
    }
  },
  computed: {
    sortNewTickets() {
      if (this.tickets) {
        return this.tickets.filter((ticket) => ticket.status === 'new') || []
      }
      return []
    },
    sortInProgressTickets() {
      if (this.tickets) {
        return this.tickets.filter((ticket) => ticket.status === 'inProgress')
      }
      return []
    }
  }
}
</script>

<style scoped>

</style>
