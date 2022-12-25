<template>
  <div class="d-flex justify-center">
    <v-col>
      <DragndropTableColumn
          column-name="Новое"
      />
    </v-col>
    <v-col>
      <DragndropTableColumn
          column-name="В работе"
      />
    </v-col>
    <v-col>
      <DragndropTableColumn
          column-name="Завершено"
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
  }
}
</script>

<style scoped>

</style>
