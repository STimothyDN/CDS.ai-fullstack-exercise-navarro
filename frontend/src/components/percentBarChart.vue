<script setup>
import { ref, onMounted } from 'vue'
import { Chart } from 'chart.js/auto'

// defining a prop on the component
// this allows us to get the summStats object transmitted down
// from our parent, App.vue
// https://vuejs.org/guide/components/props.html
const props = defineProps({
  summStats: {
    required: true,
    type: Object
  },
  category: {
    required: true,
    type: String
  }
})

// using a template ref instead of the DOM element
// https://vuejs.org/guide/essentials/template-refs.html
const chartCanvas = ref(null)

// using the onMounted lifecycle hook
// this way we don't try and build the chart until the DOM has rendered
// https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram
onMounted(() => {
  // get the categories from the data
  const categories = props.summStats[props.category].reduce((acc, datum) => {
    if (!acc.includes(datum[props.category])) {
      acc.push(datum[props.category])
    }
    return acc
  }, [])

  // // generate a dataset for the categories
  // // using a chartjs bar chart
  // // dataset definition here
  // // https://www.chartjs.org/docs/latest/charts/bar.html
  const dataset = {
    label: props.category,
    data: props.summStats[props.category].map((datum) => {
      return {
        x: datum[props.category],
        y: datum.over_50k * 100
      }
    })
  }
  console.log(dataset)

  // draw bar chart
  // https://www.chartjs.org/docs/latest/charts/bar.html
  new Chart(chartCanvas.value, {
    type: 'bar',
    data: {
      labels: categories,
      datasets: [dataset]
    },
    options: {
      scales: {
        y: {
          title: {
            display: true,
            text: 'Percent'
          }
        }
      },
      plugins: {
        tooltip: {
          callbacks: {
            label: function(context) {
              let label = context.dataset.label || '';

              if (label) {
                  label += ': ';
              }
              if (context.parsed.y !== null) {
                  label += `${context.parsed.y.toFixed(2)}%`
              }
              return label;

            }
          }
        },
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
    <h5 class="display-7 text-center">Percentage Making Over 50k Per Year By {{ props.category }}</h5>
    <canvas id="percentBarChartHolder" ref="chartCanvas"></canvas>
  </div>
</template>
