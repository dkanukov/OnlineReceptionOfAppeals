<template>
  <div class="mt-10">
      <DatePicker v-model="dateRange" is-range>
        <template v-slot="{inputValue, inputEvents}">
          <v-row no-gutters>
            <v-col cols="2">
              <v-text-field
                  class="ml-4"
                  variant="outlined"
                  hide-details="auto"
                  :value="inputValue.start"
                  v-on="inputEvents.start"
              />
            </v-col>
            <v-col cols="2">
              <v-text-field
                  class="ml-4"
                  variant="outlined"
                  hide-details="auto"
                  :value="inputValue.end"
                  v-on="inputEvents.end"
              />
            </v-col>
          </v-row>
        </template>
      </DatePicker>
    <v-expansion-panels variant="popout" class="my-4" multiple>
      <v-expansion-panel
          class="my-2"
          v-for="ticket in archiveTickets"
          :key="ticket.id"
      >
        <v-expansion-panel-title>
          <v-row no-gutters align="center">
            <v-col>
              <h3>{{ ticket.last_name }} {{ ticket.name }}</h3>
            </v-col>
            <v-col>
              <p class="ml-3">{{ HELP_OPTION_ARR[ticket.option - 1] }}</p>
            </v-col>
            <v-col>
              <p class="ml-3">{{ticket.create_date }}</p>
            </v-col>
            <v-col>
              <p>Выполнил: {{findTicketDuty(ticket.user)}}</p>
            </v-col>
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
</template>

<script>
import {mapActions, mapState} from 'vuex';
import {DatePicker} from 'v-calendar';
import {format, isEqual, parse, isBefore, isAfter} from 'date-fns';
import 'v-calendar/dist/style.css';

export default {
  name: "ArchiveComponent",
  components: {DatePicker},
  data() {
    return {
      HELP_OPTION_ARR: [
        'SOS размещение',
        'Гуманитарная помощь',
        'Необходим адресный сбор',
        'Консультация психолога',
        'Консультация юриста',
        'Хочу в группу поддержки',
        'Хочу быть волонтером фонда'
      ],
      dateRange: {
        start: new Date(),
        end: new Date(),
      }
    }
  },
  methods: {
    ...mapActions(['moveFromArchiveToNew']),
    format,
    moveTicketFromArchive(ticket) {
      this.moveFromArchiveToNew(ticket)
    },
    findTicketDuty(userId) {
      const user = this.allUsers.find((user) => user.id === userId)
      if (user) {
        return `${user.last_name} ${user.first_name}`
      }
      return ''
    }
  },
  computed: {
    ...mapState(['tickets', 'allUsers']),
    archiveTickets() {
      if (!isEqual(this.dateRange.start, this.dateRange.end)) {
        return this.tickets.filter((ticket) => {
          const ticketParsedDate = parse(ticket.create_date, 'dd.MM.yyyy', new Date())
          return !isBefore(ticketParsedDate, this.dateRange.start) && !isAfter(ticketParsedDate, this.dateRange.end) && ticket.status === 'archive';
        })
      }
      return this.tickets.filter((ticket) => ticket.status === 'archive')
    }
  },
}
</script>

<style scoped>

</style>
