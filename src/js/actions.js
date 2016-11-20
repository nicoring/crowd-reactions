// Action structure is compliant with FSA (https://github.com/acdlite/flux-standard-action) or
// it's a function to support redux-thunk
import * as api from './api'

export const selectTool = tool => ({ type: 'SELECT_TOOL', payload: { tool } })
export const addGraph = graph => ({type: 'ADD_GRAPH', payload: { graph } })
export const increaseTimer = (index, interval) => ({type: 'INCREASE_TIMER', payload: { index, interval } })


// TODO: Lock webapp until projects loaded
const infoStart = () => ({ type: 'INFO_START' })
// TODO: Throw an error in UI (alert)
const infoError = message => ({ type: 'INFO_ERROR', error: true, payload: { message } })
// Add projects to state and unlock webapp
const infoSuccess = data => ({ type: 'INFO_SUCCESS', payload: { data } })

export const loadInfos = () => ((dispatch) => {
  dispatch(infoStart())
  return api.fetchInformation()
    .then(
      r => dispatch(infoSuccess(r)),
      e => dispatch(infoError(e))
    )
})