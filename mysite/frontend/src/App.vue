<template>
  <v-app>
    <v-main>
      <HeaderComponent/>
      <v-row class="content">
        <v-col class="mt-16" cols="2">
          <v-row class="align-center">
            <v-img
                width="83px"
                height="83px"
                :src="require('@/assets/hand.png')"
            />
            ПРИЕМНАЯ <br> ОБРАЩЕНИЙ
          </v-row>
          <div class="btnGroup">
            <v-btn
                @click="handleNewTicketBtnClick"
                color="success"
                prepend-icon="mdi-plus"
                class="mt-4"
                block
            >Новое обращение</v-btn>
            <v-btn color="primary" class="mt-4" block>Все</v-btn>
            <v-btn color="primary" class="mt-4" block>Помощь</v-btn>
            <v-btn color="primary" class="mt-4" block>Консультации</v-btn>
            <v-btn color="primary" class="mt-4" block>Волонтерство</v-btn>
          </div>
        </v-col>

<!--        <v-spacer/>-->

        <v-col>
          <DragndropTable
              :tickets="this.tickets"
              :patchNewTicketStatusById="this.patchNewTicketStatusById"
          />
        </v-col>
      </v-row>
    </v-main>
    <NewTicketDialog
        :isShow="this.isShowNewTicketDialog"
    />
  </v-app>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue'
import DragndropTable from '@/components/DragndropTable.vue';
import NewTicketDialog from '@/components/NewTicketDialog.vue';
import {mapActions, mapState, mapMutations} from 'vuex';

export default {
  name: 'App',

  components: {
    HeaderComponent,
    DragndropTable,
    NewTicketDialog,
  },
  data() {
    return {}
  },
  methods: {
    ...mapActions(['fetchTickets', 'patchNewTicketStatusById']),
    ...mapMutations(['toggleIsShowNewTicketDialog']),
    handleNewTicketBtnClick() {
      this.toggleIsShowNewTicketDialog()
    }
  },
  computed: {
    ...mapState(['tickets', 'isShowNewTicketDialog'])
  },
  async created() {
    this.fetchTickets().then(() => {
      console.log(this.tickets)
    })

  }
}
</script>

<style scoped>
.content {
  padding: 20px;
  margin-top: 10px;
}

.btnGroup {
  margin-top: 70px;
}
</style>
