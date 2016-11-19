import React, { Component } from 'react';
import logo from './logo.svg';
import Graphs from './Graphs.js'
import './App.css';

class App extends Component {

  componentWillMount(){
  }

  render() {
    return (
      <div className="App line-chart">
        <Graphs/>
      </div>
    );
  }
}

export default App;
