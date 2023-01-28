<template>
<!--  <v-row class="mb-5" align="center" justify="space-between">-->
<!--    <v-btn size="x-large" icon="mdi-arrow-left-bold" variant="text"/>-->
<!--    <h3>Текущий месяц</h3>-->
<!--    <v-btn size="x-large" icon="mdi-arrow-right-bold" variant="text"/>-->
<!--  </v-row>-->
  <v-row justify="space-between" align="center">
    <div style="position: relative; height:40vh; width:40vw;">
      <Pie
          :data="allDataPie"
          :options="optionPie"
      />
    </div>
    <div style="position: relative; height:40vh; width:40vw;">
      <Bar
          :data="monthDataBar"
          :options="optionBar"
      />
    </div>
  </v-row>
  <div>
    <h2>Текущая статистика по статусам:</h2>
    <v-row no-gutters>
<!--        <h3>Новые: {{allStatistic.statusStatistic.new}}</h3>-->
    </v-row>
    <v-row no-gutters>
      <h3>В работе:</h3>
    </v-row>
    <v-row no-gutters>
      <h3>Выполнены:</h3>
    </v-row>
    <v-row no-gutters>
      <h3>В архиве: </h3>
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
            text: 'Статистика обращений за все время',
            font: {
              size: 20
            }
          },
          legend: {
            display: true,
            position: 'left'
          }
        }
      },
      monthDataBar: {
        labels: ['Сотрудник1', 'Сотрудник2', 'Сотрудник3'],
        datasets: [{
          backgroundColor: '#f87979',
          data: [40, 20, 12]
        }]
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
            text: 'Статистика по сотрудникам за все время',
            font: {
              size: 20
            }
          }
        }
      }
    }
  },
  methods: {
    ...mapActions(['fetchAllStatistic'])
  },
  computed: {
    ...mapState(['allStatistic']),
    allDataPie() {
      return {
        labels: ['SOS размещение', 'Гуманитарная помощь', 'Необходим адресный сбор', 'Koнсультация психолога', 'Консультация юриста', 'Хочу в группу поддержки', 'Хочу быть волонтером фонда'],
        datasets: [{
          data: this.allStatistic.optionStatistic,
          backgroundColor: ['#60C1CA', '#82C9EE', '#24527E', '#A0284D', '#DE5C64', '#EFAB63', '#EFAB63'],
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
