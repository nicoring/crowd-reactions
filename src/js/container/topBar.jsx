import React, { PropTypes } from 'react'
import { connect } from 'react-redux'

import {addGraph, loadInfos} from '../actions'
import Mock from './mockData.js'

const TopBar = React.createClass({
  propTypes: {
    addGraph: PropTypes.func.isRequired,
  },

  componentWillMount() {
    // var graphs = Mock.data()
    // graphs.map( graph => {
    //   this.props.addGraph(graph)
    // })
  },

  render() {
    return (
      <div className="top-bar">
        <a className="top-btn" onClick={ _ => this.props.load()}>
          Start
        </a>
      </div>
    )
  },
})

const mapStateToProps = (state, _ownProps) => ({
})

const mapDispatchToProps = (dispatch, _ownProps) => ({
  addGraph: (graph) => {
    dispatch(addGraph(graph))
  },
  load: (graph) => {
    dispatch(loadInfos())
  },
})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(TopBar)

