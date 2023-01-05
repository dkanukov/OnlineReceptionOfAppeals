<template>
  <div class="d-flex justify-center">
    <v-col>
      <DragndropTableColumn
          column-name="Новое"
          :options="{
            name: 'new',
            put: ['inProgress', 'closed']
          }"
          :tickets="newTickets"
      />
    </v-col>
    <v-col>
      <DragndropTableColumn
          column-name="В работе"
          :options="{
            name: 'inProgress',
            put: ['new', 'closed']
          }"
          :tickets="inProgressTickets"
      />
    </v-col>
    <v-col>
      <DragndropTableColumn
          column-name="Завершено"
          :options="{
            name: 'closed',
            put: ['inProgress', 'new']
          }"
          :tickets="closedTickets"
      />
    </v-col>
  </div>
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
