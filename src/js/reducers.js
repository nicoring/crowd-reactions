import { routerReducer } from 'react-router-redux'
import { combineReducers } from 'redux'

import graphs from './reducers/GraphsReducer'
import settings from './reducers/settingsReducer'

const lastAction = (state = null, action) => action

export default combineReducers({
  graphs,
  settings,
  lastAction,
  routing: routerReducer,
})
