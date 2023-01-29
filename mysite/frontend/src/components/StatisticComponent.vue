<template>
  <v-row justify="end" no-gutters class="mb-10" align="center">
    <v-btn-toggle v-model="statType">
      <v-btn value="all">За все время</v-btn>
      <v-btn value="month">За месяц</v-btn>
    </v-btn-toggle>
  </v-row>
  <div v-if="statType==='all'">
    <div>
      <v-row justify="space-between" align="center">
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
      <v-row class="w-50" no-gutters>
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
          <h1 class="customSize">{{allStatistic.total}}</h1>
          <p>Всего</p>
        </v-col>
      </v-row>
    </div>
  </div>
  <div v-else>
    <v-row class="mb-16" no-gutters justify="space-evenly">
      <v-btn
          variant="outlined"
          icon
          color="info"
          @click="handlePrevClick"
      >
        <v-icon>mdi-arrow-left-bold</v-icon>
      </v-btn>
      <h2>{{format(statDate, 'yyyy.MM')}}</h2>
      <v-btn
          :disabled="isNextDisabled"
          variant="outlined"
          icon
          color="info"
          @click="handleNextClick"
      >
        <v-icon>mdi-arrow-right-bold</v-icon>
      </v-btn>
    </v-row>
    <v-row justify="space-between" align="center">
      <div style="position: relative; height:40vh; width:40vw;">
        <Pie
            :data="monthDataPie"
            :options="optionPieMonth"
        />
      </div>
      <div style="position: relative; height:40vh; width:40vw;">
        <Bar
            :data="monthDataBar"
            :options="optionBarMonth"
        />
      </div>
    </v-row>
  </div>
</template>

<script>
import {Chart as ChartJS, ArcElement, Tooltip, Legend, Title, CategoryScale, LinearScale, BarElement} from 'chart.js'
import {Pie, Bar} from 'vue-chartjs';
import {mapActions, mapState} from 'vuex';
import {addMonths, format, getMonth, getYear, isEqual, setMilliseconds, subMonths} from 'date-fns';

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
            padding: {
              bottom: 30,
            },
            color: '#000000'
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
      optionPieMonth: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: {
            display: true,
            align: 'start',
            text: 'Статистика обращений за месяц',
            font: {
              size: 20
            },
            padding: {
              bottom: 30,
            },
            color: '#000000'
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
            text: 'Статистика обращений за все время',
            font: {
              size: 20
            },
            padding: {
              bottom: 30,
            },
            color: '#000000'
          },
          tooltip: {
            displayColors: false
          }
        }
      },
      optionBarMonth: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false,
          },
          title: {
            display: true,
            align: 'start',
            text: 'Статистика обращений за месяц',
            font: {
              size: 20
            },
            padding: {
              bottom: 30,
            },
            color: '#000000'
          },
          tooltip: {
            displayColors: false
          }
        }
      },
      statType: 'month',
      statDate: new Date(),
      isNextDisabled: true,
    }
  },
  methods: {
    format,
    ...mapActions(['fetchAllStatistic', 'fetchMonthStatistic', 'fetchMonthUserStatistic', 'fetchMonthStatistic']),
    handlePrevClick() {
      this.statDate = subMonths(this.statDate, 1)
      this.isNextDisabled = false
      const date = {
        year: getYear(this.statDate),
        month: getMonth(this.statDate) + 1
      }
      this.fetchMonthStatistic(date)
      this.fetchMonthUserStatistic(date)
    },
    handleNextClick() {
      this.statDate = addMonths(this.statDate, 1)
      if (isEqual(setMilliseconds(this.statDate, 1), setMilliseconds(new Date(), 1))) {
        this.isNextDisabled = true
      }
      const date = {
        year: getYear(this.statDate),
        month: getMonth(this.statDate) + 1
      }
      this.fetchMonthStatistic(date)
      this.fetchMonthUserStatistic(date)
    }
  },
  computed: {
    ...mapState(['allStatistic', 'allUserStatistic', 'monthUserStatistic', 'monthStatistic', 'allUsers']),
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
        labels: this.allUsers.map((user) => `${user.last_name} ${user.first_name}`),
        datasets: [{
          backgroundColor: '#82C9EE',
          data: Object.values(this.allUserStatistic).map((value) => value)
        }]
      }
    },
    monthDataPie() {
      return {
        labels: ['SOS размещение', 'Гуманитарная помощь', 'Необходим адресный сбор', 'Koнсультация психолога', 'Консультация юриста', 'Хочу в группу поддержки', 'Хочу быть волонтером фонда'],
        datasets: [{
          data: Object.values(this.monthStatistic).map((value) => value),
          backgroundColor: ['#60C1CA', '#82C9EE', '#24527E', '#A0284D', '#DE5C64', '#EFAB63', '#FFD677'],
        }]
      }
    },
    monthDataBar() {
      return {
        labels: this.allUsers.map((user) => `${user.last_name} ${user.first_name}`),
        datasets: [{
          backgroundColor: '#82C9EE',
          data: Object.values(this.monthUserStatistic).map((value) => value),
        }]
      }
    }
  },
  watch: {
    statType: {
      async handler() {
        const date = {
          year: getYear(this.statDate),
          month: getMonth(this.statDate) + 1
        }
        if (this.statType === 'month') {
          this.fetchMonthStatistic(date)
          this.fetchMonthUserStatistic(date)
        }
      },
      immediate: true
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
  font-size: 60px;
}

.customSize {
  font-size: 60px;
}
</style>
