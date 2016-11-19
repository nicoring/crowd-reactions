import React, { PropTypes } from 'react'
import { connect } from 'react-redux'

import LineChart from '../components/LineChart.js'

const ContentLayout = React.createClass({
  propTypes: {
    timer: PropTypes.array,
  },

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
  },

  render() {
    return (
      <div className="content">
        <div className="graph">
        <LineChart 
          title="Some Title"
          categories={this.timeSeries}
          values={this.values}/>
        </div>
        <div className="graph">
          <LineChart 
            title="Some Title"
            categories={this.timeSeries}
            values={this.values}/>
        </div>
      </div>
    )
  },
})

const mapStateToProps = (state, _ownProps) => ({
  timer: state.timer
})

const mapDispatchToProps = (dispatch, _ownProps) => ({
})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ContentLayout)

 // {this.props.timer.map( (timer, index) => (
        //   <Timer 
        //     key={index}
        //     index={index}/>
        // ))}