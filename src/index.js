import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

// Load Highcharts
var Highcharts = require('highcharts');

// Load a module
require('highcharts/modules/funnel')(Highcharts);
require('./HighchartTheme.js')


ReactDOM.render(
  <App />,
  document.getElementById('root')
);

