<script setup>
import { ref, onMounted } from 'vue'
import { Chart } from 'chart.js/auto'
import { BoxPlotChart } from "@sgratzl/chartjs-chart-boxplot"

// defining a prop on the component
// this allows us to get the summStats object transmitted down
// from our parent, App.vue
// https://vuejs.org/guide/components/props.html
const props = defineProps({
  summStats: {
    required: true,
    type: Object
  },
})

// using a template ref instead of the DOM element
// https://vuejs.org/guide/essentials/template-refs.html
const chartCanvas = ref(null)

// using the onMounted lifecycle hook
// this way we don't try and build the chart until the DOM has rendered
// https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram
onMounted(() => {
  // draw box plot
  // https://github.com/sgratzl/chartjs-chart-boxplot
  new BoxPlotChart(chartCanvas.value, {
    type: 'boxplot',
    data: {
      labels: [""],
      datasets: [{
        label: "Age",
        data: [
          {
            min: props.summStats.min,
            q1: props.summStats['25%'],
            median: props.summStats['50%'],
            q3: props.summStats['75%'],
            max: props.summStats.max,
            mean: props.summStats.mean,
            outliers: props.summStats.outliers || []
          }
        ]
      }]
    },
    options: {
      scales: {
        y: {
          title: {
            display: true,
            text: 'Age in Years'
          }
        }
      },
      plugins: {
        legend: {
          display: false
        }
      }
    }
  })
})
</script>
<template>
  <div>
    <h5 class="display-7 text-center">Age Summary Statistics</h5>
    <canvas id="boxPlotHolder" ref="chartCanvas"></canvas>
  </div>
</template>
