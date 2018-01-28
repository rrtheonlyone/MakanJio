import React, { Component } from 'react';

import { Grid, Row, Col, Button, Jumbotron, Glyphicon, PageHeader, Panel, Table, Image } from 'react-bootstrap';
import { Link } from 'react-router-dom'

import SimpleMap from '../map/main'

import NavBar from '../common/navbar'

class Home extends React.Component{

  constructor(props) {
    super(props);
  }    

  render() {
    return <div>
            <NavBar/>
            <Jumbotron id="first">
              <Grid>
              <h1 id="mainHeader">Makan Jio</h1>
              <p>"The sharing of food is the social life"</p>
              <Button bsStyle="primary" bsSize="large"><Glyphicon glyph="plus" />&nbsp;Add an event today</Button>
              <br/><br/>
              </Grid>
            </Jumbotron>

            <Grid>
              <Row>
                <PageHeader><Glyphicon glyph="question-sign" />&nbsp;Find Food Near you <small>Hover for more details</small></PageHeader>
                <SimpleMap/>
              </Row>

              <br/><br/>

              <Row>
                <PageHeader><Glyphicon glyph="question-sign" />&nbsp;Who are we? <small>Not your average website</small></PageHeader>
                <Col sm={4}>
                  <Panel>
                    <p>Some people would pay and eat well. Others would eat and pay well. MakanJio is a platform that allows the matching of these people, allowing you to choose to dine with a variety of hosts as they invite you to their homes for a warmly dinner. 
                    </p>
                  </Panel>
                </Col>

                <Col sm={4}>
                  <Panel>
                    <p>As the cost of living of Singapore increases, eating out in fancy restaurants may slowly not be an option. Perhaps you would like a more homely dining experience with a fellow local? MakanJio provides the social aspect of dining, while empowering you to set your budget!</p>
                  </Panel>
                </Col>

                <Col sm={4}>
                  <Panel>
                    <p>Don't you enjoy the company of friends around a warmly dinner? How about meeting new friends at the same time? MakanJio is the platform where strangers can meet over a deliciously prepared meal and forge long lasting frendships.</p>
                  </Panel>
                </Col> 
              </Row>

              <Row>
                <PageHeader><Glyphicon glyph="earphone" />&nbsp;Contact us <small>Any questions?</small></PageHeader>
                <Panel>
                    <h5>&nbsp;Tel: +65 63825633</h5>
                    <h5>&nbsp;email: contact@makanjio.com</h5>
                </Panel>
              </Row>
            </Grid>

          </div>
  }
};


export default Home;

