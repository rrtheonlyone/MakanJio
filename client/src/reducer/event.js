import {EVENT_OBTAINED, EVENT_ERROR, ALL_OBTAINED } from '../action'

const initial_state = {}

function event_reducer(state = initial_state, action) {
	switch(action.type) {
		case ALL_OBTAINED:
			return Object.assign({}, state, {
					data: action.event
  				   });
		case EVENT_OBTAINED:
			return Object.assign({}, state, {
					event: action.event
  				   });
  		case EVENT_ERROR:
  			return Object.assign({}, state, {
					error: action.err
  			       })
  		default:
  			return state
	}
}

export default event_reducer;



