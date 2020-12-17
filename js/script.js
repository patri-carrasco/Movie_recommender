Chart.defaults.global.defaultFontColor = '#fff'
Chart.defaults.global.elements.line.borderWidth = 1
Chart.defaults.global.elements.rectangle.borderWidth = 1
Chart.defaults.scale.gridLines.color = '#444'
Chart.defaults.scale.ticks.display = false

console.log('ping')
fetch('http://localhost:5000/data')
    .then(response => response.json())
    .then(data => printCharts(data))
    .catch(error => console.log(error))

function printCharts(data) {

  document.body.classList.add('running')

  byGenre(data.by_genre, 'byGenre')
  byYear(data.by_year, 'byYear')
}

function byGenre(res, id) {
  // const res = data.filter(item => item.total)

  const data = {
      labels: res.map(item => item.genre),
      datasets: [{
          data: res.map(item => item.total),
          backgroundColor: styles.color.alphas,
          borderColor: styles.color.solids
      }]
  }


  const options = {
    legend: {
        display: false
      },
      scales: {
          yAxes: [{
              gridLines: {
                  display: false
              },
              ticks: {
                  display: true
              }
          }]
      }
  }
  new Chart(id, { type: 'bar', data, options })

}

function byYear(res, id) {
    // const res = data.filter(item => item.total)
  
    const data = {
        labels: res.map(item => item.year),
        datasets: [{
            data: res.map(item => item.total),
            backgroundColor: styles.color.alphas,
            borderColor: styles.color.solids
        }]
    }
  
  
    const options = {
      legend: {
          display: false
        },
        scales: {
            yAxes: [{
                gridLines: {
                    display: false
                },
                ticks: {
                    display: true
                }
            }]
        }
    }
    new Chart(id, { type: 'bar', data, options })
  
  }