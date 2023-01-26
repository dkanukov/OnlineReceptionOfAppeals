<template>
  <div class="column">
    <h3 style="color: #696974" class="text-left ml-2">{{ columnName }}</h3>
    <Draggable
        @change="handleTicketMove"
        :list="tickets"
        :group="options"
        item-key="id"
    >
      <template #item="ticket">
        <div @click="whenTicketClick(ticket.element)" :class="['card', ticket.element.flag ? 'cardFlagBorder' : '']">
          <div class="cardHeader d-flex justify-space-between">
            <h4>
              {{this.HELP_OPTION[ticket.element.option - 1]}}
            </h4>
            <p class="text-grey-darken-1">
              id: {{ticket.element.id}}
            </p>
          </div>
          <div class="text-truncate text-grey-darken-1 text-sm-subtitle-1 mdi-clock-">
            {{ticket.element.last_name}} {{ticket.element.name}}
          </div>
          <div class="ticketTIme text-grey-darken-1 text-sm-subtitle-2">
            <p>
              <v-icon icon="mdi-calendar-clock-outline" style="width: 16px; height: 16px"></v-icon>
              {{ticket.element.create_date}}
            </p>
          </div>
        </div>
      </template>
    </Draggable>
  </div>
  <v-dialog class="dialog" v-model="isShowDialog">
    <v-card>
      <v-container>
        <v-card-title class="pt-0">
          <div class="d-flex justify-space-between align-center">
            <p class="d-flex align-center fixMargin">
              (id: {{this.selectedTicket.id}})
              {{this.HELP_OPTION[this.selectedTicket.type - 1]}}
              <v-checkbox
                  @click="clickOnFlag"
                  v-model="this.selectedTicket.flag"
                  color="indigo"
                  hide-details
              ></v-checkbox>
            </p>
            <v-btn color="error" @click="deleteTicket">
              <v-icon icon="mdi-trash-can-outline"/>
            </v-btn>
          </div>
          <p class="text-grey-darken-1 ">
            {{this.selectedTicket.name}}
            {{this.selectedTicket.last_name}}
            <a class="phoneNumber ml-5" :href="`tel:${this.selectedTicket.phone_number}`">{{this.selectedTicket.phone_number}}</a>
          </p>
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
            <v-btn @click="discardForm">Отменить</v-btn>
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
    ...mapActions(['deleteTicketById', 'patchTicketNotes', 'patchTicketStatusById', 'pathTicketFlag']),
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
      this.deleteTicketById(this.selectedTicket)
      this.isShowDialog = false
    },
    async sendForm() {
      this.patchTicketNotes({element: this.selectedTicket, newNote: this.selectedTicketNotes})
      this.selectedTicket.notes = this.selectedTicketNotes
      },
    discardForm() {
      this.isShowDialog = false
    },
    clickOnFlag() {
      this.pathTicketFlag(this.selectedTicket)
    }
  }
}
</script>

<style scoped>
.column {
  padding: 10px;
  background-color: #F5F5F5;
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

.phoneNumber {
  text-decoration: none;
}

.cardFlagBorder {
  outline: 1px solid #004dd752;
}
</style>

