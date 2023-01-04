<template>
  <v-app>
    <v-main>
      <HeaderComponent/>
      <v-row class="content">
        <v-col class="mt-16" cols="2">
          <v-row class="align-center">
            <v-img
                width="83px"
                height="83px"
                :src="require('@/assets/hand.png')"
            />
            ПРИЕМНАЯ <br> ОБРАЩЕНИЙ
          </v-row>
          <div class="btnGroup">
            <v-btn color="primary" class="mt-4" block>Все</v-btn>
            <v-btn color="primary" class="mt-4" block>Помощь</v-btn>
            <v-btn color="primary" class="mt-4" block>Консультации</v-btn>
            <v-btn color="primary" class="mt-4" block>Волонтерство</v-btn>
          </div>
        </v-col>

<!--        <v-spacer/>-->

        <v-col>
          <DragndropTable
              :tickets="tickets"
          />
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue'
import DragndropTable from '@/components/DragndropTable.vue';

export default {
  name: 'App',

  components: {
    HeaderComponent,
    DragndropTable,
  },
  data() {
    return {
      tickets: [],
    }
  },
  async mounted() {
    try {
      const ans = await fetch('http://127.0.0.1:8000/api/appeal', {method: 'GET'})
      this.tickets = await ans.json()
      console.log(this.tickets)
    } catch (e) {
      console.log(`Error during fetch in mount: ${e}`)
    }
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
</style>
