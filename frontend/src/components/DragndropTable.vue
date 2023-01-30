<template>
  <v-row>
    <v-col cols="4">
      <DragndropTableColumn
          column-name="Новое"
          :options="{
            name: 'new',
            put: ['inProgress', 'closed']
          }"
          :tickets="tickets.filter((ticket) => ticket.status === 'new')"
      />
    </v-col>
    <v-col cols="4">
      <DragndropTableColumn
          column-name="В работе"
          :options="{
            name: 'inProgress',
            put: ['new', 'closed']
          }"
          :tickets="tickets.filter((ticket) => ticket.status === 'work')"
      />
    </v-col>
    <v-col cols="4">
      <DragndropTableColumn
          column-name="Завершено"
          :options="{
            name: 'closed',
            put: ['inProgress', 'new']
          }"
          :tickets="tickets.filter((ticket) => ticket.status === 'done')"
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
  },
  computed: {},
}
</script>

<style scoped>

</style>
