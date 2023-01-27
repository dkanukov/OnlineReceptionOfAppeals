<template>
<!--  <v-row class="mb-5" align="center" justify="space-between">-->
<!--    <v-btn size="x-large" icon="mdi-arrow-left-bold" variant="text"/>-->
<!--    <h3>Текущий месяц</h3>-->
<!--    <v-btn size="x-large" icon="mdi-arrow-right-bold" variant="text"/>-->
<!--  </v-row>-->
  <v-row justify="space-between" align="center">
    <div style="position: relative; height:40vh; width:40vw;">
      <Pie
          :data="monthDataPie"
          :options="monthOptionPie"
      />
    </div>
    <div style="position: relative; height:40vh; width:40vw;">
      <Bar
          :data="monthDataBar"
          :options="monthOptionBar"
      />
    </div>
  </v-row>
</template>

<script>
import {Chart as ChartJS, ArcElement, Tooltip, Legend, Title, CategoryScale, LinearScale, BarElement} from 'chart.js'
import {Pie, Bar} from 'vue-chartjs';
import {mapActions} from 'vuex';

ChartJS.register(ArcElement, Tooltip, Legend, Title, CategoryScale, LinearScale, BarElement)

export default {
  name: "StatisticComponent",
  components: {
    Pie,
    Bar,
  },
  data() {
    return {
      monthDataPie: {
        labels: ['SOS размещение', 'Гуманитарная помощь', 'Необходим адресный сбор', 'Koнсультация психолога', 'Консультация юриста', 'Хочу в группу поддержки', 'Хочу быть волонтером фонда'],
        datasets: [{
          data: [40, 20, 80, 10, 5, 15, 20],
          backgroundColor: ['#60C1CA', '#82C9EE', '#24527E', '#A0284D', '#DE5C64', '#EFAB63', '#EFAB63'],
        }]
      },
      monthOptionPie: {
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
      monthOptionBar: {
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
    ...mapActions(['fetchStatistic'])
  },
  async mounted() {
    await this.fetchStatistic()
  }
}
</script>

<style scoped>

</style>
