import React, { Component } from 'react';
import './App.css';

import { Router, Route, Link } from 'react-router-dom'
import history from './history';

import Home from './component/start/main'
import NavBar from './component/common/navbar'


class App extends Component {
  render() {
    return (
      <div>
          <NavBar/>
          <Router history={history}>
            <div id="wrap">
              <Route exact path="/" component={Home} />
            </div>
          </Router>
      </div>
    );
  }
}

export default App;
