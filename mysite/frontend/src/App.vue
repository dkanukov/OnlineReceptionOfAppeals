<template>
  <v-app>
    <v-main>
      <HeaderComponent/>
      <v-row class="content">
        <v-col cols="2">
          <div class="btnGroup">
            <v-btn
                @click="handleNewTicketBtnClick"
                color="success"
                prepend-icon="mdi-plus"
                class="mt-4"
                block
            >Новое обращение
            </v-btn>
          </div>
        </v-col>

        <v-col>
          <DragndropTable
              :tickets="this.tickets"
              :patchNewTicketStatusById="this.patchNewTicketStatusById"
          />
        </v-col>
      </v-row>
    </v-main>
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
      ]
    }
  },
  methods: {
    ...mapActions(['fetchTickets', 'patchNewTicketStatusById']),
    ...mapMutations([]),
    handleNewTicketBtnClick() {
      this.isShowDialog = true
    },
    async sendForm() {
      console.log(JSON.stringify({
        'name': this.newTicket.name,
        'last_name': this.newTicket.surname,
        'phone_number': this.newTicket.phoneNumber,
        'type': HELP_TYPE[this.newTicket.helpType],
        'option': this.newTicket.helpOption === '' ? 7 : HELP_OPTION[this.newTicket.helpOption],
      }))
      // TODO: запрос не отправляется 400 + добавить валидацию формы, без токена 403
      const res = await fetch('http://127.0.0.1:8000/api/appeal', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: {
          'name': this.newTicket.name,
          'last_name': this.newTicket.surname,
          'phone_number': this.newTicket.phoneNumber,
          'type': HELP_TYPE[this.newTicket.helpType],
          'option': this.newTicket.helpOption === '' ? 7 : HELP_OPTION[this.newTicket.helpOption],
        }

      })
      console.log(res)
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
    }
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

.dialog {
  width: 40vw;
}
</style>
