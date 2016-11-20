export default (data) => {
  let graphs = []

  var emoDev = extractEmotions(data.data)
  graphs.push(emoDev)

  var genderDist = extractGender(data.data)
  graphs.push(genderDist)
  console.log(genderDist)

  graphs.push(extractPeople(data.data))
  graphs.push(extractAges(data.data))

  return graphs
}

function extractGender(data){
  let gender = data.map( (timeframe) => {
      if(timeframe.faces.length == 0)
        return timeframe.faces
      let aggGender = timeframe.faces.reduce( (prev, curr) => {
          // console.log(prev.gender, curr.gender)
          if(typeof prev.gender == "string")
            prev.gender = [prev.gender]
          var sex = prev.gender
          sex.push(curr.gender)
          return {gender: sex}
      })
      if(typeof aggGender.gender == "string"){
        aggGender = {
          gender: [aggGender.gender]
        }
      }
      return aggGender
  })
  gender = gender.reduce( (prev, curr) => {
    return {
      gender: prev.gender.concat(curr.gender)
    }
  })
  var maleCount = 0;
  var femaleCount = 0;

  for(var i=0; i<gender.gender.length; i++){
    if(gender.gender[i] == "male")
      maleCount++
    else
      femaleCount++
  }
  return {
    type: 'pie',
    title: 'Gender Distribution',
    data: [
      ['male', maleCount, 'blue'],
      ['female', femaleCount, 'red'],
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
              emo[key] = prev[key] / timeframe.count + curr[key] / timeframe.count
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
        data: combineTimeValue( extracTimestamps(data), ems[key]),
      }
    }),
    // timeSeries: extracTimestamps(data)
  }
}


function extractPeople(data){
  let people = data.map( (timeframe) => {
    return [parseFloat(timeframe.timestamp), timeframe.count]
  })

  return {
    type: 'line',
    title: 'Number of People',
    data: [{
        name: "peopleCount",
        data: people,
      }
    ]
  }
}

function combineTimeValue(timestamps, values){
  let comb = []
  for(var i=0; i<timestamps.length; i++){
    comb.push([timestamps[i], values[i]])
  }
  return comb
}

function extracTimestamps(data){
  let timestamps = data.map( (timeframe) => {
    return parseFloat(timeframe.timestamp)
  })
  return timestamps
}

function extractAges(data){
  let ages = {
    "0-20": 0,
    "20-30": 0,
    "30-40": 0,
    "40-50": 0,
    ">50": 0
  }
  let gender = data.map( (timeframe) => {
      if(timeframe.faces.length == 0)
        return timeframe.faces
      let aggGender = timeframe.faces.map( face => {
          if(face.age < 20){
            ages["0-20"]++
          }else if(face.age < 30){
            ages["20-30"]++
          }else if(face.age < 40){
            ages["30-40"]++
          }else if(face.age < 50){
            ages["40-50"]++
          }else{
            ages[">50"]++
          }
      })
  })

  var data = Object.keys(ages).map( key => {
    return [key, ages[key]]
  })

  return {
    type: 'pie',
    title: 'Age Distribution',
    data: data
  }
}