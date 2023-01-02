<template>
  <div class="d-flex justify-center">
    <v-col>
      <DragndropTableColumn
          column-name="Новое"
          list-id="1"
          :list="list1"
      />
    </v-col>
    <v-col>
      <DragndropTableColumn
          column-name="В работе"
          list-id="2"
          :list="list2"
      />
    </v-col>
    <v-col>
      <DragndropTableColumn
          column-name="Завершено"
          list-id="3"
          :list="list3"
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
  data() {
    return {
      list1: [
        {
          id: 1
        }
      ],
      list2: [
        {
          id: 2
        }
      ],
      list3: [
        {
          id: 3
        }
      ]
    }
  },
}
</script>

<style scoped>

</style>
