import { combineReducers } from 'redux'

import event_reducer from './event';

const rootReducer = combineReducers({
  event: event_reducer,
})

export default rootReducer