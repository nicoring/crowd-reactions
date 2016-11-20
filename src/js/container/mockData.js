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
        title: 'Line Graph',
        data: [
          {
            data: val,
            name: "Value 1"
          },
          {
            data: val2,
            name: "Other Line Graph"
          }
        ],
        timeSeries: timeSeries
      },
      {
        type: 'line',
        title: 'Line Graphasdf',
        data: [
          {
            data: val,
            name: "Value 1"
          },
          {
            data: val2,
            name: "Other Line Graph"
          }
        ],
        timeSeries: timeSeries
      }
    ]

      return graphs
  }
}