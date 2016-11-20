import ReactHighcharts from 'react-highcharts';
import React, { Component, PropTypes } from 'react';


class LineChart extends Component {

  componentWillMount(){
    this.config = {
      chart: {
          plotBackgroundColor: null,
          plotBorderWidth: null,
          plotShadow: false,
          type: 'pie'
      },
      title: {
          text: this.props.title
      },
      tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
      },
      subtitle: {
          text: this.props.subtitle
      },
      plotOptions: {
            pie: {
              allowPointSelect: true,
              cursor: 'pointer',
              dataLabels: {
                  enabled: false
              },
              showInLegend: true
          }
        },
      series: [{
        name: 'Brands',
        colorByPoint: true,
        data: this.props.data.map( dataRow => ({
          name: dataRow[0],
          y: dataRow[1],
          sliced: true
        }))
      }]
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
  subtitle: PropTypes.string,
  data: PropTypes.array.required,
}

export default LineChart