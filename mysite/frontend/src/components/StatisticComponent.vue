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
  <div class="mt-10">
    <h2 class="mb-4">Текущая статистика по статусам</h2>
    <v-row class="w-50">
      <v-col>
        <h1 class="customColor">{{allStatistic.statusStatistic.new}}</h1>
        <p>Новые</p>
      </v-col>
      <v-col>
        <h1 class="customColor">{{allStatistic.statusStatistic.work}}</h1>
        <p>В работе</p>
      </v-col>
      <v-col>
        <h1 class="customColor">{{allStatistic.statusStatistic.done}}</h1>
        <p>Выполнены</p>
      </v-col>
      <v-col>
        <h1 class="customColor">{{allStatistic.statusStatistic.archive}}</h1>
        <p>В архиве</p>
      </v-col>
      <v-col>
        <h1>{{allStatistic.total}}</h1>
        <p>Всего</p>
      </v-col>
    </v-row>
  </div>
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
.customColor {
  color: #60C1CA;
}
</style>
