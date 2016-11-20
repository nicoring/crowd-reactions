import React, { PropTypes } from 'react'
import { connect } from 'react-redux'

import LineChart from '../components/LineChart.js'
import PieChart from '../components/PieChart.js'

const ContentLayout = React.createClass({
  propTypes: {
    graphs: PropTypes.array,
  },

  componentWillMount(){
    console.log(this.props.graphs)
  },

  componentWillReceiveProps(newProps){
    // this.props.graphs = newProps.graphs
  },

  componentDidReceiveProps(newProps){
    // this.props.graphs = newProps.graphs
  },

  baseGraph(graph){

    switch(graph.type){
      case 'line':
        return (
          <LineChart
            title={graph.title}
            categories={graph.timeSeries}
            data={graph.data}
          />)
      case 'pie':
        return (
          <PieChart
            title={graph.title}
            data={graph.data}
          />)
      default:
        return
    }
  },

  render() {
    return (
      <div className="content">
        {this.props.graphs.map( (graph, index) => (
          <div className="graph" key={index}>
            { this.baseGraph(graph)}        
          </div>
        ))}
      </div>
    )
  },
})

const mapStateToProps = (state, _ownProps) => ({
  graphs: state.graphs
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