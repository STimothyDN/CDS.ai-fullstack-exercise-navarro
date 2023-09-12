<!-- using  script setup (composition api) -->
<!-- https://vuejs.org/api/sfc-script-setup.html -->
<script setup>
import { onMounted, ref } from 'vue'
import barChart from '@/components/barChart.vue'
import boxPlot from '@/components/boxPlot.vue'
import percentBarChart from './components/percentBarChart.vue'

// creating a reactive variable
// https://vuejs.org/api/reactivity-core.html#ref
let censusData = ref([])
let summStats = ref({})

// using the mounted lifecycle hook to fetch our data
// https://vuejs.org/api/composition-api-lifecycle.html
onMounted(async () => {
  censusData.value = await fetch('http://localhost:8000/census').then((census) => census.json())
  summStats.value = await fetch('http://localhost:8000/summary-stats').then((summ) =>
    summ.json()
  )
})
</script>

<template>
  <!-- As a heading -->
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-md">
        <a class="navbar-brand" href="#">CDS.ai Full Stack Exercise</a>
      </div>
    </nav>
    <div class="container">
      <p class="lead text-center">
        <small>Census data text</small>
      </p>
      <div v-if="censusData.length">
        <div class="row">
          <div class="col-6">
            <barChart :censusData="censusData" :category="'education_level'" />
          </div>
          <div class="col-6">
            <barChart :censusData="censusData" :category="'race'" />
          </div>
        </div>
      </div>
      <div v-else class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <div v-if="summStats.age">
        <p class="lead text-center">
          <small>Summary Statistics</small>
        </p>
        <div class="row">
          <div class="col-6">
            <boxPlot :summStats="summStats.age" />
          </div>
          <div class="col-6">
            <percentBarChart :summStats="summStats" :category="'sex'" />
          </div>
        </div>
        <div class="row">
          <div class="col-6">
            <percentBarChart :summStats="summStats" :category="'education_level'" />
          </div>
          <div class="col-6">
            <percentBarChart :summStats="summStats" :category="'race'" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.navbar {
  margin-bottom: 1rem;
}
</style>
