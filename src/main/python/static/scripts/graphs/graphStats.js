


fetch('/api/activities_per_type')
.then(async r=>{
    let datos = await(r.json())

    Highcharts.chart('activitiesPerType', {
    chart: { type: 'pie' },
    title: { text: 'Actividades según tipo' },
    series: [{
      name: 'Actividades',
      data: datos.map(d => ({ name: d.tipo, y: d.count }))
    }]
  });
})


fetch('/api/members_by_day')
.then(async r=>{
    let data = await (r.json())

    Highcharts.chart('membersPerDay', {
      chart: {
        type: 'line'
      },
      title: {
        text: 'Miembros registrados por dia'
      },
      xAxis: {
        type: 'datetime',
        title: {
          text: 'Fecha'
        }
      },
      yAxis: {
        title: {
          text: 'Miembros'
        }
      },
      tooltip: {
        xDateFormat: '%d/%m/%Y',
        shared: true
      },
      series: [{
        name: 'Miembros',
        data: data,
        color: '#FF9900'
      }],
      legend: {
        enabled: true
      },
      responsive: {
        rules: [{
          condition: {
            maxWidth: 500
          },
          chartOptions: {
            legend: {
              layout: 'horizontal',
              align: 'center',
              verticalAlign: 'bottom'
            }
          }
        }]
      }
    });

})