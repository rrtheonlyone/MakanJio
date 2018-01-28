import axios from 'axios'
import qs from 'qs'

import history from '../history'
import {API_URL, EVENT_OBTAINED, EVENT_ERROR, ALL_OBTAINED} from '../action'

axios.defaults.baseURL = 'http://' + API_URL;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

function allEvent(event) {
	return {
		type: ALL_OBTAINED,
		event
	}
}

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

function eventCreate() {
	return {
		
	}
}

export function createEvent() {

}

export function getEvent(id) {
		return (dispatch) => {
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
		}
}

export function getAllEvent() {
		return (dispatch) => {
				axios({
						method: 'get',
						url: '/event',
					  })
					 .then((response) => {
					 	dispatch(allEvent(response.data));
					 })
					 .catch((error) => {
					 	console.log(error);
					 	const msg = (error.response) ? error.response.data : "Error Retrieving Events! Something went wrong";
					 	dispatch(eventError("msg"));
					 });
			}
		}




