import React from 'react';
import logo from './logo.svg';
import './App.css';

import {Route, Link, BrowserRouter as Router, Switch} from 'react-router-dom'
import TestDash from "./components/test/testDash";
import Home from "./views/Home";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/test" exact component={TestDash} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
