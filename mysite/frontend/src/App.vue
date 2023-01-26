<template>
  <v-app class="containerCustom">
    <HeaderComponent/>
    <div v-if="currentPage==='dashBoard'" class="containerCustom mt-10">
      <v-row align="center" justify="space-between">
        <v-row align="center">
          <v-btn
              variant="tonal"
              @click="handleNewTicketBtnClick"
              prepend-icon="mdi-plus"
              class="setMinWidth customColorBtn height100"
          >Новое обращение
          </v-btn>
          <v-btn
              @click="updateTickets"
              variant="tonal"
              class="ml-4 setMinWidth customColorBtn"
          >
            <v-icon icon="mdi-cached"></v-icon>
          </v-btn>
          <v-autocomplete
              class="ml-4"
              v-model="filterHelpType"
              density="comfortable"
              hide-details="auto"
              multiple
              label="Тип заявки"
              :items="helpType"
              variant="solo"
              style="max-width: 400px"
          ></v-autocomplete>
        </v-row>
        <v-btn
            @click="redirectToArchive"
            variant="text"
        >
          Архив
        </v-btn>
      </v-row>
      <v-row class="mt-10">
        <DragndropTable
            :tickets="this.filteredTickets"
        />
      </v-row>
    </div>
    <div v-else-if="currentPage==='archive'" class="containerCustom mt-10">
      <v-row justify="end">
        <v-btn variant="text" @click="redirectToDashboard">Обращения</v-btn>
      </v-row>
      <div class="mt-10">
        <v-expansion-panels variant="popout" class="my-4" multiple>
          <v-expansion-panel
              class="my-2"
              v-for="ticket in archiveTickets"
              :key="ticket.id"
          >
            <v-expansion-panel-title>
              <v-row no-gutters align="center">
                <h3>{{ticket.last_name}} {{ticket.name}}</h3>
                <p class="ml-3">{{HELP_OPTION_ARR[ticket.option - 1]}}</p>
                <p class="ml-3">{{ticket.create_date}}</p>
                <p class="ml-3">{{ticket.phone_number}}</p>
              </v-row>
            </v-expansion-panel-title>

            <v-expansion-panel-text>
              <v-row no-gutters>
                {{ticket.notes}}
              </v-row>
            </v-expansion-panel-text>

          </v-expansion-panel>
        </v-expansion-panels>
      </div>
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
      HELP_OPTION: {
        'SOS размещение': 1,
        'Гуманитарная помощь': 2,
        'Необходим адресный сбор': 3,
        'Консультация психолога': 4,
        'Консультация юриста': 5,
        'Хочу в группу поддержки': 6,
      },
      HELP_OPTION_ARR: [
        'SOS размещение',
        'Гуманитарная помощь',
        'Необходим адресный сбор',
        'Консультация психолога',
        'Консультация юриста',
        'Хочу в группу поддержки',
        'Хочу быть волонтером фонда'
      ],
      filterHelpType: [],
      currentPage: 'dashBoard',
      panel: [],
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
      this.patchTicketNotes({element: res.json(), newNote: this.newTicket.notes})
    },
    discardForm() {
      this.isShowDialog = false
      this.newTicket = {}
    },
    updateTickets() {
      console.log('upd')
      this.fetchTickets()
    },
    redirectToArchive() {
      this.currentPage = 'archive'
    },
    redirectToDashboard() {
      this.currentPage = 'dashBoard'
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
    },
    archiveTickets() {
      return this.tickets.filter((ticket) => ticket.status === 'archive')
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
  background-color: #F5F5F5;
  padding: 10px 20px;
}

.dialog {
  width: 40vw;
}

.customColorBtn {
  background-color: #DFEAF6;
  color: #004DD7;
  font-weight: bold;
}

.fixRowHeight {
  height: 50px !important;
}
</style>
