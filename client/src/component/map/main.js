import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

import {Panel, Glyphicon, Button, OverlayTrigger, Popover} from 'react-bootstrap'

import { connect } from 'react-redux'
import {getAllEvent} from '../../action/event'

import {Link} from 'react-router-dom'

class SimpleMap extends Component {
  static defaultProps = {
    center: {lat: 1.37, lng: 103.83},
    zoom: 11
  };

  componentWillMount() {
    this.props.dispatch(getAllEvent())
  }

  render() {

    const Marker = (props) => {return <OverlayTrigger trigger={['hover', 'focus']} placement="left" overlay={<Popover id="popover-positioned-left" title={props.data[7]}>
        <strong>Event Happening!</strong> {props.data[5]}
      </Popover>}>
                                    <Link to={'/event/' + props.data[0]}><Button bsStyle="success"><Glyphicon glyph="cutlery" /></Button></Link>
                                  </OverlayTrigger>
                              };

    const {data} = this.props;

    return (
      <div style={{"height" : "500px", "width" : "1000px"}}>
      <GoogleMapReact
        defaultCenter={this.props.center}
        defaultZoom={this.props.zoom}
      >
        {data && data.map((data) => {console.log(data);return <Marker lat={data[3]} lng={data[2]} key={data[0]} data={data}/>})}
      </GoogleMapReact>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return { data: state.event.data };
}

export default connect(mapStateToProps)(SimpleMap)
