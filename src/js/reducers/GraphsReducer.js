function graph(state = [], action) {
  switch (action.type) {
    case 'ADD_GRAPH':
      return [
        ...state,
        action.payload.graph,
      ]
    case 'REMOVE_GRAPH':{
      let newState = [...state]
      newState.splice(action.payload.index, 1)
      return newState
    }
    // case 'INCREASE_TIMER':
    //   return state.map( (timer, index) => handleTimer(timer, index, action ))
    default:
      return [ ...state ]
  }
}

function handleGraph(timer, index, action){
  if(index === action.payload.index){
    return {
      ...timer,
      count: Math.round( ( timer.count + action.payload.interval )* 10 ) / 10,
    }
  }else{
    return {...timer}
  }
}

export default graph
