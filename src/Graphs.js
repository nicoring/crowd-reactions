import React, { Component } from 'react';
import logo from './logo.svg';
import LineChart from './LineChart.js'
import './App.css';

class Graphs extends Component {

  componentWillMount(){
    this.timeSeries = []
    for(var i=0; i<163; i++){
      this.timeSeries.push(i)
    }
    this.values = []
    var val = []
    for(var i=0; i<163; i++){
      val.push(Math.random() * 200 + i)
    }

     var val2 = []
    for(var i=0; i<163; i++){
      val2.push(Math.random() * 200 + i)
    }

    this.values.push({
      data: val,
      name: "some"})
    this.values.push({
      data: val2,
      name: "someother"})
  }

  render() {
    return (
      <div className="Graph">
        <LineChart 
          title="Some Title"
          categories={this.timeSeries}
          values={this.values}/>
      </div>
    );
  }
}

export default Graphs;
