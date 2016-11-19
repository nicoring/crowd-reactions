import ReactHighcharts from 'react-highcharts';
import React, { Component, PropTypes } from 'react';


class LineChart extends Component {

  componentWillMount(){
    this.config = {
      chart: {
                zoomType: 'x'
            },
      title: {
          text: this.props.title
      },
      subtitle: {
          text: this.props.subtitle
      },
      xAxis: {
        categories: this.props.categories
      },
      plotOptions: {
            spline: {
                lineWidth: 1,
                marker: {
                    enabled: false
                }
            }
        },
      series: this.props.values
    };

    
  }
  

  render() {
    return (
      <ReactHighcharts className="line-chart" config={this.config}/>
    );
  }
}

LineChart.PropTypes = {
  title: PropTypes.string,
  subtitle: PropTypes.string
}

export default LineChart