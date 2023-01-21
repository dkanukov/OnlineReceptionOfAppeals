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
        <div @click="whenTicketClick(ticket.element)" class="card">
          <div class="cardHeader d-flex justify-space-between">
            <h4>
              {{this.TICKET_NAME[ticket.element.type]}}
              <span class="ticketOption">
                ({{this.HELP_OPTION[ticket.element.option - 1]}})
              </span>
            </h4>
            <p class="text-grey-darken-1">
              id: {{ticket.element.id}}
            </p>
          </div>
<!--          TODO: починить для длинных строк-->
          <div v-if="ticket.element.notes" class="text-truncate">
            {{ticket.element.notes}}
          </div>
        </div>
      </template>
    </Draggable>
  </div>
  <v-dialog class="dialog" v-model="isShowDialog">
    <v-card>
      <v-container>
        <v-card-title>
          <p>
            (id: {{this.selectedTicket.id}})
            {{this.HELP_OPTION[this.selectedTicket.type - 1]}}
          </p>
          <p class="text-grey-darken-1">
            {{this.selectedTicket.name}}
            {{this.selectedTicket.last_name}}
          </p>
          <v-btn @click="deleteTicket">Удалить</v-btn>
        </v-card-title>
        <v-card-text>
          <v-textarea
              auto-grow
              label="Заметки"
              v-model="selectedTicketNotes"
          />
        </v-card-text>
        <v-card-actions>
          <v-btn-group class="d-flex justify-end">
            <v-btn @click="sendForm" color="success">Сохранить</v-btn>
            <v-btn color="error">Отменить</v-btn>
          </v-btn-group>
        </v-card-actions>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
import Draggable from 'vuedraggable'
import {mapActions} from 'vuex';

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
      put: Array
    },
  },
  data() {
    return {
      TICKET_NAME: {
        1: 'Помощь',
        2: 'Консультация',
        3: 'Волонтерство',
      },
      HELP_OPTION: [
        'SOS размещение',
        'Гуманитарная помощь',
        'Необходим адресный сбор',
        'Консультация психолога',
        'Консультация юриста',
        'Хочу в группу поддержки',
        'Хочу быть волонтером фонда',
      ],
      isShowDialog: false,
      selectedTicket: null,
      selectedTicketNotes: ''
    }
  },
  methods: {
    ...mapActions(['deleteTicketById', 'patchTicketNotes', 'patchTicketStatusById']),
    handleTicketMove({added}) {
      if (added) {
        this.patchTicketStatusById({
          elementId: added.element.id,
          newStatus: STATUS_TUPLE[this.columnName]
        })
      }
    },
    whenTicketClick(ticket) {
      this.selectedTicket = ticket
      this.selectedTicketNotes = this.selectedTicket.notes
      this.isShowDialog = true
    },
    deleteTicket() {
      this.deleteTicketById(this.selectedTicket.id)
      this.isShowDialog = false
    },
    async sendForm() {
      this.patchTicketNotes(this.selectedTicket, this.selectedTicketNotes)
        this.selectedTicket.notes = this.selectedTicketNotes
      },
    }
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
  cursor: pointer;
  padding: 10px;
  margin-top: 14px;
  background-color: #fff;
  border-radius: 20px;
}

.dialog {
  width: 50vw;
}

.ticketOption {
  color: #171725;
  font-weight: 400;
  font-size: 15px;
  line-height: 36px;
}
</style>


//.cardText {
//  word-wrap: break-word;
//  text-overflow:ellipsis;
//  overflow:hidden;
//  display: -webkit-box !important;
//  -webkit-line-clamp: 3;
//  -webkit-box-orient: vertical;
//  white-space: normal;
//}
