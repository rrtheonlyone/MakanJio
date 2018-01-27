import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

import {Panel, Glyphicon, Button} from 'react-bootstrap'

import { connect } from 'react-redux'
import {getEvent} from '../../action/event'


const AnyReactComponent = ({ text }) => <Button bsStyle="success"><Glyphicon glyph="cutlery" /></Button>;

class SimpleMap extends Component {
  static defaultProps = {
    center: {lat: 1.37, lng: 103.83},
    zoom: 11,
    greatPlaces: [
      {id: 'Aasfafafaf', lat: 1.367, lng: 105},
      {id: 'Basfafafafafas', lat: 10, lng: 88}
    ]
  };

  componentDidMount() {
    this.props.dispatch(getEvent())
  }

  render() {

    const places = this.props.greatPlaces
      .map(place => {
        return (
          <AnyReactComponent
            lat={place.lat}
            lng={place.lng}
          />
        );
      })

    return (
      <div style={{"height" : "500px", "width" : "1000px"}}>
      <GoogleMapReact
        defaultCenter={this.props.center}
        defaultZoom={this.props.zoom}
      >
        {places}
      </GoogleMapReact>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return { event: state.event.event };
}

export default connect(mapStateToProps)(SimpleMap)
