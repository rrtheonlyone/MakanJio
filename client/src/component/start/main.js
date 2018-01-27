import React, { Component } from 'react';

import { Grid, Row, Col, Button, Jumbotron, Glyphicon, PageHeader, Panel, Table, Image } from 'react-bootstrap';
import { Link } from 'react-router-dom'

import SimpleMap from '../map/main'

class Home extends React.Component{

  constructor(props) {
    super(props);
  }    

  render() {
    return <div>
            <Jumbotron>
              <Grid>
              <h2>Makan Jio</h2>
              <p>Food Sharing Made more convenient. Scroll down for more details!</p>
              <Glyphicon glyph="chevron-down" />
              </Grid>
            </Jumbotron>

            <Grid>
              <Row>
                <h3>Find food near you!</h3>
                <SimpleMap/>
              </Row>

              <br/><br/>

              <Row>
                <h4>Who are we?</h4>
                <Col sm={4}>
                  <Panel>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et ligula lacus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus finibus id magna nec efficitur. Ut ultrices elit odio, in posuere ante tempor eget. Quisque rhoncus nunc eu lacus interdum, quis suscipit diam molestie. Aliquam ut justo sed lorem volutpat vehicula sit amet et ex. Phasellus tincidunt mauris at diam blandit hendrerit. Praesent condimentum sollicitudin ex ut accumsan.</p>
                  </Panel>
                </Col>

                <Col sm={4}>
                  <Panel>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et ligula lacus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus finibus id magna nec efficitur. Ut ultrices elit odio, in posuere ante tempor eget. Quisque rhoncus nunc eu lacus interdum, quis suscipit diam molestie. Aliquam ut justo sed lorem volutpat vehicula sit amet et ex. Phasellus tincidunt mauris at diam blandit hendrerit. Praesent condimentum sollicitudin ex ut accumsan.</p>
                  </Panel>
                </Col>

                <Col sm={4}>
                  <Panel>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et ligula lacus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus finibus id magna nec efficitur. Ut ultrices elit odio, in posuere ante tempor eget. Quisque rhoncus nunc eu lacus interdum, quis suscipit diam molestie. Aliquam ut justo sed lorem volutpat vehicula sit amet et ex. Phasellus tincidunt mauris at diam blandit hendrerit. Praesent condimentum sollicitudin ex ut accumsan.</p>
                  </Panel>
                </Col> 
              </Row>

              <Row>
                <h4>Contact us</h4>
                <Panel>
                    <p>orem ipsum dolor sit amet, consectetur adipiscing elit. Nam et ligula lacus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus finibus id magna nec efficitur. Ut ultrices elit odio, in posuere ante tempor eget. Quisque rhoncus nunc eu lacus interdum, quis suscipit</p>
                </Panel>
              </Row>
            </Grid>

          </div>
  }
};


export default Home;

