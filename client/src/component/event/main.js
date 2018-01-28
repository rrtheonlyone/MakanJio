import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

import {Panel, Glyphicon, Button, OverlayTrigger, Popover, Grid, Row, Col, Table} from 'react-bootstrap'

import { connect } from 'react-redux'
import {getEvent} from '../../action/event'

import OtherBar from '../common/otherbar'
import NavBar from '../common/navbar'

class EventDetail extends Component {

  constructor(props) {
    super(props)
  }

  componentDidMount() {
    this.props.dispatch(getEvent(this.props.match.params.event_id))
  }

  render() {

    const {event} = this.props;
    var centre = {lat: 1.37, lng: 103.83};

    const Marker = (props) => {return <h1 className="glyphicon glyphicon-cutlery"></h1> };

    return (
      <div>
        <OtherBar/>
        {event &&
        <Grid>
          <Row>
            <h2><Glyphicon glyph="list-alt" />&nbsp;Event Details</h2>
            <h4><Glyphicon glyph="time" />&nbsp;Date and Time: {event[6]}</h4>
          </Row>

          <hr/>

          <Row>
            <Col sm={6}>
              <Panel>
                <h4>&nbsp;<Glyphicon glyph="grain" />&nbsp;Hosted by: {event[13]}</h4>
                <br/>
                <h4>&nbsp;<u>Description:</u></h4>
                <p>{event[5]}</p>
              </Panel>
            </Col>

            <Col sm={6}>
             {centre && event &&
              <div style={{"height" : "300px", "width" : "500px"}}>
              <GoogleMapReact
                defaultCenter={centre}
                defaultZoom={10}
              >
                <Marker
                  lat={event[3]}
                  lng={event[2]}
                />
              </GoogleMapReact>
              </div>}
            </Col>
          </Row>

          <Row>
            <Col sm={6}>
              <h4><Glyphicon glyph="comment" />&nbsp;Feedback for the host</h4>
              <Table striped hover>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Rating (out of 5)</th>
                    <th>Review</th>
                  </tr>
                </thead>
                <tbody> 
                  {event[10] && event[10].map((data) => {
                          return <tr>
                                    <td>{data[0]}</td>
                                    <td>{data[2]}</td>
                                    <td>{data[1]}</td>
                                 </tr>
                        })}
                </tbody>
              </Table>
            </Col>

            <Col sm={6}>
              <h2><Glyphicon glyph="check" />&nbsp;Price: {event[4]}</h2>
              <Button bsStyle="primary" bsSize="large"><Glyphicon glyph="thumbs-up" />&nbsp;Join Event</Button>
              <p>Quota Remaining: 6 (Attendance List below)</p>
              <hr/>
              <Table bordered hover>
                <thead>
                  <tr>
                    <th>Name</th>
                  </tr>
                </thead>
                <tbody>
                  {event[9] && event[9].map((data) => {return <tr><td>{data}</td></tr>})}
                </tbody>
              </Table>
            </Col>
          </Row>
        </Grid>}
      </div>
    );
  }
}

function mapStateToProps(state) {
  return { event: state.event.event };
}

export default connect(mapStateToProps)(EventDetail)