import axios from 'axios'
import qs from 'qs'

import history from '../history'
import {API_URL, EVENT_OBTAINED, EVENT_ERROR} from '../action'

axios.defaults.baseURL = 'http://' + API_URL;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

function eventSuccess(event) {
	return {
		type: EVENT_OBTAINED,
		event
	}
}

function eventError(err) {
	return {
		type: EVENT_ERROR,
		err
	}
}

export function getEvent(id=undefined) {
		return (dispatch) => {
			if (id) {
				axios({
						method: 'get',
						url: '/event/' + id,
					  })
					 .then((response) => {
					 	dispatch(eventSuccess(response.data));
					 })
					 .catch((error) => {
					 	const msg = (error.response) ? error.response.data : "Error Retrieving Events! Something went wrong";
					 	dispatch(eventError(msg));
					 });
			} else {
				axios({
						method: 'get',
						url: '/event',
					  })
					 .then((response) => {
					 	dispatch(eventSuccess(response.data));
					 })
					 .catch((error) => {
					 	const msg = (error.response) ? error.response.data : "Error Retrieving Events! Something went wrong";
					 	dispatch(eventError(msg));
					 });
			}
		}
}



