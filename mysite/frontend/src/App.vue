<template>
  <v-app class="containerCustom">
    <HeaderComponent/>
    <div v-if="currentPage==='dashBoard'" class="containerCustom mt-10">
      <v-row align="center" justify="space-between" no-gutters>
        <v-row align="center" no-gutters>
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
          <v-btn-toggle>
            <v-btn
                v-model="isMine"
                @click="toggleMine"
                variant="tonal"
                class="ml-10 setMinWidth customColorBtn"
            >
              Мои
            </v-btn>
          </v-btn-toggle>
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
            @click="redirectToStatistic"
            variant="text"
        >
          Статистика
        </v-btn>
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
      <v-row justify="space-between" no-gutters>
        <DatePicker class="inline-block h-full" v-model="date">
          <template v-slot="{ inputValue, togglePopover }">
            <div class="flex items-center">
              <button
                  class="p-2 bg-blue-100 border border-blue-200 hover:bg-blue-200 text-blue-600 rounded-l focus:bg-blue-500 focus:text-white focus:border-blue-500 focus:outline-none"
                  @click="togglePopover()"
              >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    class="w-8 h-8 fill-current"
                >
                  <path
                      d="M1 4c0-1.1.9-2 2-2h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V4zm2 2v12h14V6H3zm2-6h2v2H5V0zm8 0h2v2h-2V0zM5 9h2v2H5V9zm0 4h2v2H5v-2zm4-4h2v2H9V9zm0 4h2v2H9v-2zm4-4h2v2h-2V9zm0 4h2v2h-2v-2z"
                  ></path>
                </svg>
              </button>
              <input
                  :value="inputValue"
                  class="bg-white text-gray-700 w-full py-1 px-2 appearance-none border rounded-r focus:outline-none focus:border-blue-500"
                  readonly
              />
            </div>
          </template>
        </DatePicker>
        <div>
          <v-btn
              @click="redirectToStatistic"
              variant="text"
          >
            Статистика
          </v-btn>
          <v-btn variant="text" @click="redirectToDashboard">Обращения</v-btn>
        </div>
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
                <h3>{{ ticket.last_name }} {{ ticket.name }}</h3>
                <p class="ml-3">{{ HELP_OPTION_ARR[ticket.option - 1] }}</p>
                <p class="ml-3">{{ ticket.create_date }}</p>
                <p class="ml-3">{{ ticket.phone_number }}</p>
              </v-row>
            </v-expansion-panel-title>

            <v-expansion-panel-text>
              <v-row no-gutters>
                {{ ticket.notes }}
              </v-row>
              <v-btn class="mt-5" @click="moveTicketFromArchive(ticket)">Вернуть обращение в работу</v-btn>
            </v-expansion-panel-text>

          </v-expansion-panel>
        </v-expansion-panels>
      </div>
    </div>
    <div v-else-if="currentPage==='statistic'" class="containerCustom mt-10">
      <v-row justify="end">
        <v-btn variant="text" @click="redirectToDashboard">Обращения</v-btn>
        <v-btn @click="redirectToArchive" variant="text">Архив</v-btn>
      </v-row>
      <div class="mt-10">
        <StatisticComponent/>
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
import StatisticComponent from '@/components/StatisticComponent.vue';
import {mapActions, mapMutations, mapState} from 'vuex';
import {DatePicker} from 'v-calendar'
import 'v-calendar/dist/style.css';

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
    StatisticComponent,
    DatePicker
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
      isMine: false,
    }
  },
  methods: {
    ...mapActions(['fetchTickets', 'patchTicketStatusById', 'patchTicketNotes', 'getUser', 'getAllUsers', 'moveFromArchiveToNew']),
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
      this.patchTicketNotes({element: await res.json(), newNote: this.newTicket.notes})
      this.fetchTickets()
      this.isShowDialog = false
    },
    discardForm() {
      this.isShowDialog = false
      this.newTicket = {}
    },
    updateTickets() {
      this.fetchTickets()
    },
    moveTicketFromArchive(ticket) {
      this.moveFromArchiveToNew(ticket)
    },
    redirectToArchive() {
      this.currentPage = 'archive'
    },
    redirectToDashboard() {
      this.currentPage = 'dashBoard'
    },
    redirectToStatistic() {
      this.currentPage = 'statistic'
    },
    toggleMine() {
      this.isMine = !this.isMine
    }
  },
  computed: {
    ...mapState(['tickets', 'user']),
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
      if (!this.filterHelpType.length && !this.isMine) {
        return this.tickets
      }
      if (!this.filterHelpType.length && this.isMine) {
        return this.tickets.filter((ticket) => ticket.user === this.user.id)
      }
      return this.tickets.filter((ticket) => {
        if (this.filterHelpType.includes(this.helpType[ticket.type - 1])) {
          return ticket
        }
      })
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
    await this.getAllUsers()
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
