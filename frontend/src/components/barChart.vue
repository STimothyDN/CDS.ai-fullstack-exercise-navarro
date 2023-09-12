<script setup>
import { ref, onMounted } from 'vue'
import { Chart } from 'chart.js/auto'

// function to format strings into a more display friendly format
function formatString(category){
  return category.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

// function to generate a random RGB color
function getRandomColor(){
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);
  return `rgb(${r},${g},${b})`;
}

// defining a prop on the component
// this allows us to get the censusData object transmitted down
// from our parent, App.vue
// https://vuejs.org/guide/components/props.html
const props = defineProps({
  censusData: {
    required: true,
    type: Array
  },
  category: {
    required: true,
    type: String
  }
})

// defining order for education levels to be sorted by
const educationOrder = [
  "Did not complete high school",
  "High school",
  "Some college",
  "Associates",
  "Bachelors",
  "Masters",
  "Professional school",
  "Doctorate"
];

// using a template ref instead of the DOM element
// https://vuejs.org/guide/essentials/template-refs.html
const chartCanvas = ref(null)

// using the onMounted lifecycle hook
// this way we don't try and build the chart until the DOM has rendered
// https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram
onMounted(() => {
  // if category is education level, sorts data by defined order
  if (props.category === "education_level") {
    props.censusData.sort((a, b) => {
      return educationOrder.indexOf(a.education_level) - educationOrder.indexOf(b.education_level);
    });
  }

  // get the categories from the data
  const categories = props.censusData.reduce((acc, datum) => {
    const formattedString = formatString(datum[props.category]);
    if (!acc.includes(formattedString)) {
      acc.push(formattedString)
    }
    return acc
  }, [])

  // generate a dataset for the categories
  // using a chartjs bar chart
  // dataset definition here
  // https://www.chartjs.org/docs/latest/charts/bar.html
  const dataset = {
    label: formatString(props.category),
    data: categories.map((category) => {
      return props.censusData.filter((datum) => datum[props.category] === category).length
    }),
    backgroundColor: categories.map(() => getRandomColor())
  }

  // draw bar chart
  // https://www.chartjs.org/docs/latest/charts/bar.html
  new Chart(chartCanvas.value, {
    type: 'bar',
    data: {
      labels: categories,
      datasets: [dataset]
    },
    options: {
      indexAxis: 'y'
    }
  })
})
</script>
<template>
  <div>
    <h5 class="display-7 text-center">Census Data By {{ formatString(props.category) }}</h5>
    <canvas id="barChartHolder" ref="chartCanvas"></canvas>
  </div>
</template>
