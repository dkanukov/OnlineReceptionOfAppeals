<template>
  <div>
    <v-row justify="space-evenly" align="center">
      <div style="position: relative; height:40vh; width:40vw;">
        <Pie
            :data="allDataPie"
            :options="optionPie"
        />
      </div>
      <div style="position: relative; height:40vh; width:40vw;">
        <Bar
            :data="allDataBar"
            :options="optionBar"
        />
      </div>
    </v-row>
  </div>
  <v-row class="mt-10">
    <v-col>
      <h2>Текущая статистика по статусам:</h2>
      <v-row no-gutters>
        <h3>Новые: {{allStatistic.statusStatistic.new}}</h3>
      </v-row>
      <v-row no-gutters>
        <h3>В работе: {{allStatistic.statusStatistic.work}}</h3>
      </v-row>
      <v-row no-gutters>
        <h3>Выполнены: {{allStatistic.statusStatistic.done}}</h3>
      </v-row>
      <v-row no-gutters>
        <h3>В архиве: {{allStatistic.statusStatistic.archive}}</h3>
      </v-row>
      <v-row no-gutters>
        <h2>Всего: {{allStatistic.total}}</h2>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
import {Chart as ChartJS, ArcElement, Tooltip, Legend, Title, CategoryScale, LinearScale, BarElement} from 'chart.js'
import {Pie, Bar} from 'vue-chartjs';
import {mapActions, mapState} from 'vuex';

ChartJS.register(ArcElement, Tooltip, Legend, Title, CategoryScale, LinearScale, BarElement)

export default {
  name: "StatisticComponent",
  components: {
    Pie,
    Bar,
  },
  data() {
    return {
      optionPie: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: {
            display: true,
            align: 'start',
            text: 'Статистика обращений за все время',
            font: {
              size: 20
            },
          },
          legend: {
            display: true,
            position: 'left',
            labels: {
              font: {
                size: 16,
              }
            }
          },
          tooltip: {
            displayColors: false
          }
        }
      },
      optionBar: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false,
          },
          title: {
            display: true,
            align: 'start',
            text: 'Статистика по сотрудникам за все время',
            font: {
              size: 20
            },
          },
          tooltip: {
            displayColors: false
          }
        }
      }
    }
  },
  methods: {
    ...mapActions(['fetchAllStatistic'])
  },
  computed: {
    ...mapState(['allStatistic', 'allUserStatistic']),
    allDataPie() {
      return {
        labels: ['SOS размещение', 'Гуманитарная помощь', 'Необходим адресный сбор', 'Koнсультация психолога', 'Консультация юриста', 'Хочу в группу поддержки', 'Хочу быть волонтером фонда'],
        datasets: [{
          data: this.allStatistic.optionStatistic,
          backgroundColor: ['#60C1CA', '#82C9EE', '#24527E', '#A0284D', '#DE5C64', '#EFAB63', '#FFD677'],
        }]
      }
    },
    allDataBar() {
      return {
        labels: this.allUserStatistic.map((user) => user.userName),
        datasets: [{
          backgroundColor: '#82C9EE',
          data: this.allUserStatistic.map((user) => user.total)
        }]
      }
    }
  },
  async mounted() {
    await this.fetchAllStatistic()
  }
}
</script>

<style scoped>

</style>
