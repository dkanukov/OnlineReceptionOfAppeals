<template>
  <div class="d-flex justify-center">
    <v-col>
      <DragndropTableColumn
          column-name="Новое"
          :options="{
            name: 'new',
            put: ['inProgress', 'closed']
          }"
          :tickets="tickets"
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
      newTicketsProp: [
        {name: "John", id: 1},
      ],
      inProgressTickets: [],
      closedTickets: [],
    }
  },
  computed: {}
}
</script>

<style scoped>

</style>
