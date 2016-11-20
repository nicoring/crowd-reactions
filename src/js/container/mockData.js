export default {
  data: () => {
    var timeSeries = []
    for(var i=0; i<163; i++){
      timeSeries.push(i)
    }

    var val = []
    for(var i=0; i<163; i++){
      val.push(Math.random() * 200 + i)
    }

     var val2 = []
    for(var i=0; i<163; i++){
      val2.push(Math.random() * 200 + i)
    }

    let graphs = [
      {
        type: 'line',
        title: 'Development of emotions',
        data: [
          {
            data: val,
            name: "Happiness"
          },
          {
            data: val2,
            name: "Neutral"
          }
        ],
        timeSeries: timeSeries
      },
      {
        type: 'pie',
        title: 'Age Distribution',
        data: [
          ['10-30', 0.20],
          ['30-35', 0.50],
          ['35-45', 0.25]
        ]
      }
    ]

      return graphs
  }
}