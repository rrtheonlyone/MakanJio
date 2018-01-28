import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

import {Panel, Glyphicon, Button, OverlayTrigger, Popover, Grid, Row, Col, Table} from 'react-bootstrap'

import { connect } from 'react-redux'
import {getEvent} from '../../action/event'

class EventDetail extends Component {

  componentDidMount() {
    this.props.dispatch(getEvent(this.props.match.params.event_id))
  }

  render() {

    const {event} = this.props;
    const centre = {lat: 1.37, lng: 103.83};

    return (
      <div>
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
                <h4>&nbsp;<Glyphicon glyph="grain" />&nbsp;Hosted by: {event[12]}</h4>
                <br/>
                <h4>&nbsp;<u>Description:</u></h4>
                <p>{event[0]}</p>
              </Panel>
            </Col>

            <Col sm={6}>
              <div style={{"height" : "300px", "width" : "500px"}}>
              <GoogleMapReact
                defaultCenter={centre}
                defaultZoom={15}
              >
              </GoogleMapReact>
              </div>
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
                  <tr>
                    <td>1</td>
                    <td>Mark</td>
                    <td>Otto</td>
                  </tr>
                  <tr>
                    <td>2</td>
                    <td>Jacob</td>
                    <td>Thornton</td>
                  </tr>
                </tbody>
              </Table>
            </Col>

            <Col sm={6}>
              <h2><Glyphicon glyph="check" />&nbsp;Price: </h2>
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
                  <tr>
                    <td>Mark</td>
                  </tr>
                  <tr>
                    <td>Jacob</td>
                  </tr>
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