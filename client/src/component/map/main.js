import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

import {Panel, Glyphicon, Button} from 'react-bootstrap'

const AnyReactComponent = ({ text }) => <Button bsStyle="success"><Glyphicon glyph="flash" /></Button>;

class SimpleMap extends Component {
  static defaultProps = {
    center: {lat: 1.37, lng: 103.83},
    zoom: 11,
    greatPlaces: [
      {id: 'Aasfafafaf', lat: 1.367, lng: 105},
      {id: 'Basfafafafafas', lat: 10, lng: 88}
    ]
  };

  render() {

    const places = this.props.greatPlaces
      .map(place => {
        const {id, ...coords} = place;

        return (
          <AnyReactComponent
            key={id}
            {...coords}
            text={id}
          />
        );
      })

    return (
      <div style={{"height" : "500px", "width" : "1000px"}}>
      <GoogleMapReact
        defaultCenter={this.props.center}
        defaultZoom={this.props.zoom}
      >
        <AnyReactComponent
          lat={1.37}
          lng={103.83}
          text={'Kreyser Avrora'}
        />
      </GoogleMapReact>
      </div>
    );
  }
}

export default SimpleMap