import React, { Component } from 'react';
import './App.css';

import { Provider } from 'react-redux'
import configureStore from './store/configureStore'

import { Router, Route, Link } from 'react-router-dom'
import history from './history';

import Home from './component/start/main'
import NavBar from './component/common/navbar'
import EventDetail from './component/event/main'

const store = configureStore();

class App extends Component {
  render() {
    return (
      <Provider store={store}>
      <div>
          <NavBar/>
          <Router history={history}>
            <div id="wrap">
              <Route exact path="/" component={Home} />
              <Route path="/event/:event_id" component={EventDetail} />
            </div>
          </Router>
      </div>
      </Provider>
    );
  }
}

export default App;
