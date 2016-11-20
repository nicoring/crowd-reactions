export default (data) => {
  let graphs = []

  var emoDev = extractEmotions(data.data)
  graphs.push(emoDev)

  console.log(graphs)
  return graphs
}

function extractGender(data){
  let gender = data.map( (timeframe) => {
    if(timeframe.faces.length == 0)
      return timeframe.faces
    let aggGender = timeframe.emotions.reduce( (prev, curr) => {
          if(typeof prev.gender == "string")
            prev.gender = [prev.gender]
          var sex = prev.gender
          sex.push(curr.gender)
          return {gender: sex}
        })
    return aggGender
  })

  return {
    type: 'pie',
    title: 'Gender Distribution',
    data: [
      ['male', gender.male],
      ['female', gender.female],
    ]
  }
}

function extractEmotions(data){
  let emotions = data.map( (timeframe) => {
    if(timeframe.emotions.length == 0)
      return timeframe.emotions
    let aggEmotions = timeframe.emotions.reduce( (prev, curr) => {
          var emo = {}
          for(var key in prev){
            if(prev[key] && curr[key])
              emo[key] = prev[key] + curr[key]
          }
          return emo
        })
    return aggEmotions
  })

  let ems = {}
  for(var i=0; i<emotions.length; i++){
    for(var emo in emotions[i]){
      try{
      ems[emo].push(emotions[i][emo])
      }catch(err)
      {ems[emo] = [emotions[i][emo]]}
    }
    if(Object.keys(emotions[i]).length == 0){
      for(var emo in ems){
        ems[emo].push(0)
      }
    }
  }

  return {
    type: 'line',
    title: 'Emotional Development',
    data: Object.keys(ems).map( key => {
      return {
        name: key,
        data: ems[key],
      }
    })
  }
}