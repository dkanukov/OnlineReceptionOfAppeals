<template>
  <v-app class="containerCustom">
    <HeaderComponent/>
    <div class="containerCustom">
      <v-row class="mb-15">
        <v-col class="v-col-2 v-col-md-3">
          <v-btn
              @click="handleNewTicketBtnClick"
              color="success"
              prepend-icon="mdi-plus"
              class="mt-4 setMinWidth"
              block
          >Новое обращение
          </v-btn>
        </v-col>
        <v-col cols="3">
          <v-autocomplete
              v-model="filterHelpType"
              multiple
              label="Тип заявки"
              :items="helpType"
              variant="solo"
          ></v-autocomplete>
        </v-col>
      </v-row>
      <v-row>
        <DragndropTable
            :tickets="this.filteredTickets"
        />
      </v-row>
    </div>
    <v-dialog class="dialog" v-model="isShowDialog">
      <v-card>
        <v-container>
          <v-card-title>
            Создание нового обращения
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col>
                <v-text-field
                    label="Введите имя"
                    type=""
                    required
                    v-model="newTicket.name"
                />
              </v-col>
              <v-col>
                <v-text-field
                    label="Введите фамилию"
                    required
                    v-model="newTicket.surname"
                />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                    label="Номер телефона"
                    v-model="newTicket.phoneNumber"
                />
              </v-col>
              <v-col>
                <v-select
                    label="Требуемый тип помощи"
                    v-model="newTicket.helpType"
                    :items="helpType"
                />
              </v-col>
            </v-row>
            <v-row v-if="isShowNewTicketOption">
              <v-col>
                <v-select
                    label="Выберите опцию"
                    :items="newTicketOptionRelatedOnType"
                    v-model="newTicket.helpOption"
                />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-textarea
                    label="Заметка"
                    v-model="newTicket.notes"
                />
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-btn-group class="d-flex justify-end">
              <v-btn @click="sendForm" color="success">Сохранить</v-btn>
              <v-btn @click="discardForm" color="error">Отменить</v-btn>
            </v-btn-group>
          </v-card-actions>
        </v-container>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue'
import DragndropTable from '@/components/DragndropTable.vue';
import {mapActions, mapState, mapMutations} from 'vuex';

const HELP_TYPE = {
  'Помощь': 1,
  'Консультация': 2,
  'Волонтерство': 3,
}
const HELP_OPTION = {
  'SOS размещение': 1,
  'Гуманитарная помощь': 2,
  'Необходим адресный сбор': 3,
  'Консультация психолога': 4,
  'Консультация юриста': 5,
  'Хочу в группу поддержки': 6,
}
export default {
  name: 'App',
  components: {
    HeaderComponent,
    DragndropTable,
  },
  data() {
    return {
      isShowDialog: false,
      newTicket: {
        name: '',
        surname: '',
        phoneNumber: null,
        notes: '',
        helpType: '',
        helpOption: ''
      },
      helpType: [
        'Помощь', 'Консультация', 'Волонтерство',
      ],
      filterHelpType: [],
    }
  },
  methods: {
    ...mapActions(['fetchTickets', 'patchTicketStatusById', 'patchTicketNotes', 'getUser']),
    ...mapMutations([]),
    handleNewTicketBtnClick() {
      this.isShowDialog = true
    },
    async sendForm() {
      const cookie = document.cookie
      const res = await fetch('http://127.0.0.1:8000/api/appeal', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
        },
        body: JSON.stringify({
          'name': this.newTicket.name,
          'last_name': this.newTicket.surname,
          'phone_number': this.newTicket.phoneNumber,
          'type': HELP_TYPE[this.newTicket.helpType],
          'option': this.newTicket.helpOption === '' ? 7 : HELP_OPTION[this.newTicket.helpOption],
        })
      })
      this.patchTicketNotes(res.json(), this.newTicket.notes)
    },
    discardForm() {
      this.isShowDialog = false
      this.newTicket = {}
    }
  },
  computed: {
    ...mapState(['tickets']),
    isShowNewTicketOption() {
      return this.newTicket.helpType === 'Помощь' || this.newTicket.helpType === 'Консультация'
    },
    newTicketOptionRelatedOnType() {
      if (this.newTicket.helpType === 'Помощь') {
        return [
          'SOS размещение',
          'Гуманитарная помощь',
          'Необходим адресный сбор',
        ]
      } else {
        return [
          'Koнсультация психолога',
          'Консультация юриста',
          'Хочу в группу поддержки',
        ]
      }
    },
    filteredTickets() {
      if (!this.filterHelpType.length) {
        return this.tickets
      }
      const filteredTickets = this.tickets.filter((ticket) => {
        if (this.filterHelpType.includes(this.helpType[ticket.type - 1])) {
          return ticket
        }
      })
      return filteredTickets
    }
  },
  async created() {
    this.fetchTickets().then(() => {
      console.log(this.tickets)
    })
    await this.getUser()
  }
}
</script>

<style scoped>
.containerCustom {
  padding: 20px;
}

.dialog {
  width: 40vw;
}

.fixRowHeight {
  height: 50px !important;
}
</style>
