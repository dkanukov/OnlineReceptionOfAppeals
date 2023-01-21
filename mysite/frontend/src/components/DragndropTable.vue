<template>
  <v-row>
    <v-col cols="4">
      <DragndropTableColumn
          column-name="Новое"
          :options="{
            name: 'new',
            put: ['inProgress', 'closed']
          }"
          :tickets="newTickets"
      />
    </v-col>
    <v-col cols="4">
      <DragndropTableColumn
          column-name="В работе"
          :options="{
            name: 'inProgress',
            put: ['new', 'closed']
          }"
          :tickets="inProgressTickets"
      />
    </v-col>
    <v-col cols="4">
      <DragndropTableColumn
          column-name="Завершено"
          :options="{
            name: 'closed',
            put: ['inProgress', 'new']
          }"
          :tickets="closedTickets"
      />
    </v-col>
  </v-row>
</template>

<script>
import DragndropTableColumn from '@/components/DragndropTableColumn.vue';

export default {
  name: "DragndropTable",
  components: {
    DragndropTableColumn,
  },
  props: {
    tickets: Array,
    patchTicketStatusById: Function,
  },
  data() {
    return {
      newTickets: this.tickets.filter((ticket) => ticket.status === 'new'),
      inProgressTickets: this.tickets.filter((ticket) => ticket.status === 'work'),
      closedTickets: this.tickets.filter((ticket) => ticket.status === 'done'),
    }
  },
  computed: {},
  watch: {
    tickets() {
      this.newTickets = this.tickets.filter((ticket) => ticket.status === 'new')
      this.inProgressTickets = this.tickets.filter((ticket) => ticket.status === 'work')
      this.closedTickets = this.tickets.filter((ticket) => ticket.status === 'done')
    },
  },
}
</script>

<style scoped>

</style>
